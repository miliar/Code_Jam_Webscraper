#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <thread>


using namespace std;

bool Findijk (const vector<char>& str);
bool FindLetter(vector<char>&, char);
void FindijkThread (const vector<char>& str, unsigned int testCaseNumber);

const unordered_map<string,pair<bool,char>> table = {
   {"11", make_pair(true,'1')},
   {"1i", make_pair(true,'i')},
   {"1j", make_pair(true,'j')},
   {"1k", make_pair(true,'k')},
   {"i1", make_pair(true,'i')},
   {"ii", make_pair(false,'1')},
   {"ij", make_pair(true,'k')},
   {"ik", make_pair(false,'j')},
   {"j1", make_pair(true,'j')},
   {"ji", make_pair(false,'k')},
   {"jj", make_pair(false,'1')},
   {"jk", make_pair(true,'i')},
   {"k1", make_pair(true,'k')},
   {"ki", make_pair(true,'j')},
   {"kj", make_pair(false,'i')},
   {"kk", make_pair(false,'1')}
};

unsigned int* results;

int main()
{
   unsigned int testCases;
   cin >> testCases;
   results = new unsigned int [testCases+1];
   for( size_t m = 1; m <= testCases; ++m ) {
      results[m] = 0;
   }
   vector<std::thread> resultThreads;
//   vector<pair<unsigned int,boost::future<bool>>> futures;

   for( size_t m = 1; m <= testCases; ++m ) {
      //Gather input
      unsigned int characters, repetitions;
      cin >> characters >> repetitions;
      cin.ignore(); //ignore new-line

      vector<char> strinput;
      for( size_t n = 1; n <= characters; ++n ) {
	 char c;
	 cin.get(c);
	 strinput.push_back(c);
      }
      //str will hold the true string (with replicates)
      vector<char>str;
      str.reserve(strinput.size() * repetitions);
      for( size_t n = 1; n <= repetitions; ++n ) {
	 str.insert(str.begin(),strinput.begin(),strinput.end());
      }

      //Main Program Logic
//      FindijkThread(str, m);
      thread temp(FindijkThread, str, m);
      resultThreads.push_back(move(temp));

//      futures.push_back(make_pair(m, boost::packaged_task<bool>(Findijk,str)));
//      futures.push_back(make_pair(m, boost::async(Findijk,str)));
//      bool resultbool = Findijk(str);

      //Printing
//      string result;
//      if (resultbool)
//	 result = "YES";
//      else
//	 result = "NO";
//      cout << "Case #" << m << ": " << result << endl;
   }
//   for( auto &e : futures ) {
   //for( thread t : resultThreads ) {
   for( size_t m = 0; m < resultThreads.size(); ++m ) {
      resultThreads.at(m).join();
   }
   for( size_t m = 1; m <= testCases; ++m )
//      cout << "Case #" << e.first << ": " << (e.second.get_future()?"YES":"NO") << endl;
      cout << "Case #" << m << ": " << (*(results+m) == 1?"YES":(*(results+m) == 2? "NO":"ERROR")) << endl;

   return 0;
}

void FindijkThread (const vector<char>& str, unsigned int testCaseNumber) {
   bool foundi = false;
   bool foundj = false;
   bool foundk = false;
   vector<char>* analyzeLetter = new vector<char>();
   size_t startOfk;
   for( size_t n = 0; n < str.size() && !foundj; ++n ) {
      analyzeLetter->push_back(str.at(n));
      if( !foundi ) {
	 if(FindLetter(*analyzeLetter, 'i')) {
	    foundi = true;
	    analyzeLetter->clear();
	 }
      } else {  // !foundj
	 if(FindLetter(*analyzeLetter, 'j')) {
	    foundj = true;
	    analyzeLetter->clear();
	    startOfk = n+1;
	 }
      }
   }
   delete analyzeLetter;
   if( foundi && foundj && startOfk != str.size()) {
      analyzeLetter = new vector<char>(str.begin()+startOfk, str.end());
      if (FindLetter(*analyzeLetter, 'k')) {
	 foundk = true;
      }
      delete analyzeLetter;
   }
   if( foundi && foundj && foundk ) {
      *(results+testCaseNumber) = 1;
   } else {
      *(results+testCaseNumber) = 2;
   }
}

bool Findijk (const vector<char>& str) {
   bool foundi = false;
   bool foundj = false;
   bool foundk = false;
   vector<char>* analyzeLetter = new vector<char>();
   size_t startOfk;
   for( size_t n = 0; n < str.size() && !foundj; ++n ) {
      analyzeLetter->push_back(str.at(n));
      if( !foundi ) {
	 if(FindLetter(*analyzeLetter, 'i')) {
	    foundi = true;
	    analyzeLetter->clear();
	 }
      } else {  // !foundj
	 if(FindLetter(*analyzeLetter, 'j')) {
	    foundj = true;
	    analyzeLetter->clear();
	    startOfk = n+1;
	 }
      }
   }
   delete analyzeLetter;
   if( foundi && foundj && startOfk != str.size()) {
      analyzeLetter = new vector<char>(str.begin()+startOfk, str.end());
      if (FindLetter(*analyzeLetter, 'k')) {
	 foundk = true;
      }
      delete analyzeLetter;
   }
   return foundi && foundj && foundk;
}

bool FindLetter(vector<char>& array, char target) {
   char current = array.at(0);
   bool positive = true;
   for( auto i = array.begin(); i != array.end(); ++i ) {
      if( i == array.begin() )
	 continue;
      string toSearch;
      toSearch.push_back(current);
      toSearch.push_back(*i);
      auto result = table.find (toSearch);

      if( result != table.end() ) {
	 //cout << "result of " << toSearch[0] << " and " << toSearch[1] << " = " << (result->second.first?"":"-") << result->second.second << endl;
	 current = result->second.second;
	 positive = !positive^result->second.first;
      } else {
	 cout << "ERROR";
	 cerr << "ERROR";
      }
   }
   return (current == target) && positive;
}
