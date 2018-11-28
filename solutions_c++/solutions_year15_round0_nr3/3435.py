#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cassert>

using namespace std;

#define ERROR(message) cout << message << endl; return 1;

struct Test {
   size_t L;
   size_t X;
   string orig;
   string test;
};

//Use character to represent a quaternion number
//bit 0 is sign, 1 is negative, 0 is positive. quat >> 0 & 1
//1 is bit 1, quat >> 1 & 1
//i is bit 2, quat >> 2 & 1
//j is bit 3, quat >> 3 & 1
//k is bit 4, quat >> 4 & 1
//bits 5-7 unused
typedef char quat;
static const size_t idx1 = 0;
static const size_t idxi = 1;
static const size_t idxj = 2;
static const size_t idxk = 3;

static const quat one = 0x02;
static const quat i = 0x04;
static const quat j = 0x08;
static const quat k = 0x10;

#if 0
#define TRACE(x) cout << x << endl;
#else
#define TRACE(x)
#endif

// |1 is negative
static const quat multTable[][4] = {
   {one, i, j, k},
   {i, one|1, k, j|1}, 
   {j, k|1, one|1, i},
   {k, j, i|1, one|1}
};

size_t idxFromQuat(quat a) {
   if (a & one)
      return idx1;
   else if (a & i)
      return idxi;
   else if (a & j)
      return idxj;
   else if (a & k)
      return idxk;
   assert(false);
   return 0;
}

quat neg(quat a) {
   return a | 1;
}

quat charToQuat(char c) {
   if (c == 'i')
      return i;
   if (c == 'j')
      return j;
   if (c == 'k')
      return k;
   TRACE("BAD QUAT " << c);
   assert(false);
   return one;
}

//Multiply quaternions as characters
quat mult(quat a, quat b) {
   quat out;
   //Get sign, bitmask with 1 to get only sign bit, xor is sign
   out = (a & 1) ^ (b & 1);
   size_t idxa = idxFromQuat(a);
   size_t idxb = idxFromQuat(b);
   quat multOut = multTable[idxa][idxb];
   out = out ^ multOut;
   return out;
}

bool lineToTest(string testLine1, string testLine2, Test& test) {
   size_t spacepos = testLine1.find(' ');
   if (spacepos == string::npos)
      return false;

   test.orig = testLine2;
   test.L = stoi(testLine1.substr(0, spacepos));
   test.X = stoi(testLine1.substr(spacepos+1));

   if (test.orig.size() != test.L)
      return false;

   test.test.clear();
   for (size_t i = 0; i < test.X; i++) {
      test.test += test.orig;
   }

   return true;
}

static const size_t NOT_FOUND = size_t(-1);
//Returns the index of the character at which was found, inclusive
size_t findQuat(const string& s, size_t startIndex, quat soFar, quat toFind) {
   if (soFar == toFind)
      return startIndex;

   if (startIndex >= s.size())
      return NOT_FOUND;

   soFar = mult(soFar, charToQuat(s[startIndex]));
   return findQuat(s, startIndex+1, soFar, toFind);
}

bool dotest(const Test& test) {
   //Preprocess to make sure that we aren't in an obviously impossible case
   //Only one character can't make all three of ijk
   if (test.L <= 1) {
      TRACE("  Eliminated for 1 char.");
      return false;
   }
   char first = test.orig[0];
   bool allSame;
   for (size_t i = 1; i < test.L; i++) {
      if (test.orig[i] != first) {
         allSame = false;
         break;
      }
   }
   if (allSame) {
      TRACE("  Eliminated for all same.");
      return false;
   }

   //Now do the real test
   TRACE("  Testing " << test.test);

   size_t foundIndexI = findQuat(test.test, 0, one, i);

   if (foundIndexI == NOT_FOUND) {
      TRACE("  Couldn't find i");
      return false;
   }
   else {
      TRACE("  Found i at " << foundIndexI << " as " \
           << test.test.substr(0, foundIndexI));
   }

   size_t foundIndexJ = findQuat(test.test, foundIndexI, one, j);
   if (foundIndexJ == NOT_FOUND) {
      TRACE("  Couldn't find j");
      return false;
   }
   TRACE("  Found j at " << foundIndexJ << " as " \
        << test.test.substr(foundIndexI, foundIndexJ - foundIndexI));

   size_t foundIndexK = findQuat(test.test, foundIndexJ, one, k);
   if (foundIndexK == NOT_FOUND) {
      TRACE("  Couldn't find k");
      return false;
   }

   if (foundIndexK != test.test.size()) {
      string remaining = test.test.substr(foundIndexK);
      TRACE("  Found k at " << foundIndexK << ". Remainder " << remaining);
      quat soFar = one;
      for (char c : remaining) {
         soFar = mult(soFar, charToQuat(c));
      }
      if (soFar != one) {
         TRACE("  Found k, but non-one remainder at the end.");
         return false;
      }
   }
   TRACE("  Found k at " << foundIndexK << " as " \
      << test.test.substr(foundIndexJ, foundIndexK - foundIndexJ));

   return true;
}

void testMultiplication() {
   assert(mult(one, one) == one);
   assert(mult(one, i) == i);
   assert(mult(one, j) == j);
   assert(mult(one, k) == k);
   assert(mult(i, one) == i);
   assert(mult(i, i) == neg(one));
   assert(mult(i, j) == k);
   assert(mult(i, k) == neg(j));
   assert(mult(j, one) == j);
   assert(mult(j, i) == neg(k));
   assert(mult(j, j) == neg(one));
   assert(mult(j, k) == i);
   assert(mult(k, one) == k);
   assert(mult(k, i) == j);
   assert(mult(k, j) == neg(i));
   assert(mult(k, k) == neg(one));
}

int main(int argc, char** argv) {
   if (argc != 2) {
      ERROR("Specify the goddamn input file!");
   }

   //Open up the test cases file
   string filename = argv[1];
   cout << "Input " << filename << endl;
   ifstream inputfile;
   inputfile.open(filename);
   assert(inputfile.is_open());

   //Figure out how many tests there are
   string line;
   bool gotNumTests = getline(inputfile, line);
   assert(gotNumTests);

   int numTests = stoi(line);
   cout << numTests << " tests" << endl;

   testMultiplication();

   //Read and do each test
   std::vector<bool> testResults;
   string testLine1, testLine2;
   for (size_t i = 0; i < numTests; i++) {
      bool gotLine1 = getline(inputfile, testLine1);
      bool gotLine2 = getline(inputfile, testLine2);
      if (!(gotLine1 && gotLine2)) {
         ERROR("Not enough lines in the file.");
      }
      TRACE("Case #" << i+1 << ": " << endl << \
         "  " << testLine1 << endl << \
         "  " << testLine2);
      Test t;
      if (!lineToTest(testLine1, testLine2, t)) {
         ERROR("Test " << i << " improperly formatted.");
      }
      testResults.push_back(dotest(t));
   }
   assert(testResults.size() == numTests);

   string outputfilename = filename.substr(0, filename.find('.')) + ".out";
   cout << "Putting output in " << outputfilename << endl;
   ofstream outputfile(outputfilename);
   if (!outputfile.is_open()) {
      ERROR("Couldn't open output file.");
   }

   for (size_t i = 0; i < testResults.size(); i++) {
      outputfile << "Case #" << i+1 << ": " << (testResults[i] ? "YES" : "NO") << endl;
   }

   return 0;
}