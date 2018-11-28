#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cassert>

using namespace std;

#define ERROR(message) cout << message << endl; return 1;

class Test {
public:
   size_t shyest;
   vector<size_t> shyCounts;
};

bool lineToTest(string line, Test& test) {
   size_t spacepos = line.find(' ');
   if (spacepos == string::npos)
      return false;

   string shyeststr = line.substr(0, spacepos);
   string counts = line.substr(spacepos+1);

   cout << "  " << shyeststr << " is the shyest" << endl;
   cout << "  " << counts << " are the counts" << endl;

   stringstream ss;
   ss << shyeststr;
   ss >> test.shyest;

   if (counts.size() != test.shyest + 1)
      return false;

   test.shyCounts.clear();
   for(size_t i = 0; i < counts.size(); i++) {
      int count = stoi(counts.substr(i, 1));
      test.shyCounts.push_back(count);
   }

   return true;
}

size_t dotest(Test t) {
   size_t numStanding = 0;
   size_t numFriends = 0;
   for (size_t i = 0; i < t.shyCounts.size(); i++) {
      //i is the number of required standing people to get these people to stand
      cout << "  Test l " << i << ", " << t.shyCounts[i] << endl;
      cout << "    " << numStanding << " standing." << endl;

      if (numStanding >= i) {
         numStanding += t.shyCounts[i];
      }

      if (numStanding < i) {
         size_t friendsInvite = i - numStanding;
         cout << "    Inviting " << friendsInvite << " friends." << endl;
         numFriends += friendsInvite;
         numStanding += t.shyCounts[i];
         numStanding += friendsInvite;
      }
   }

   cout << "  Must invite " << numFriends << " friends." << endl;
   return numFriends;
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

   int numTests;
   stringstream ss;
   ss << line;
   ss >> numTests; 
   cout << numTests << " tests" << endl;

   //Read and do each test
   std::vector<size_t> testResults;
   for (size_t i = 0; i < numTests; i++) {
      if (!getline(inputfile, line)) {
         ERROR("Not enough lines in the file.");
      }
      cout << "Case #" << i+1 << ": " << line << endl;
      Test t;
      if (!lineToTest(line, t)) {
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
      outputfile << "Case #" << i+1 << ": " << testResults[i] << endl;
   }



   return 0;
}