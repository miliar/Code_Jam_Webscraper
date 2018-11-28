#include <iostream>
#include <sstream>
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <fstream>
#include <stdexcept>
#include <memory>

using namespace std;

uint32_t asd(vector<uint32_t>& motes, uint32_t arminsMote, uint32_t position) {
   if(arminsMote == 1)
      return motes.size();
   if(position >= motes.size())
      return 0;

   uint32_t nextMote = motes[position];
   if(nextMote < arminsMote)
      return asd(motes, arminsMote+nextMote, position + 1);

   if(nextMote < arminsMote + arminsMote - 1)
      return 1 + asd(motes, arminsMote + arminsMote -1 + nextMote, position + 1);

   // Try remove
   uint32_t rmOps = 1 + asd(motes, arminsMote, position + 1);
   uint32_t addOps = 1 + asd(motes, arminsMote + arminsMote - 1, position);

   if(rmOps < addOps)
      return rmOps;
   else
      return addOps;
}

int main(int argc, char** argv) {
   // Read input
   if(argc != 2)
      throw invalid_argument("no input: ./a.out [filename]");
   string str(argv[1]);
   ifstream in(str);
   if(!in.good() || !in.is_open())
      throw invalid_argument("file not found");

   // Read number of cases
   uint32_t numCases;
   in >> numCases;

   for(uint32_t testCase=0; testCase<numCases; testCase++) {

      uint32_t arminsMote;
      in >> arminsMote;
      uint32_t numOtherMotes;
      in >> numOtherMotes;
      vector<uint32_t> motes(numOtherMotes);
      for(auto& iter : motes) {
         in >> iter;
      }

      sort(motes.begin(), motes.end());

      uint32_t operations = asd(motes, arminsMote, 0);

      cout << "Case #" << testCase+1 << ": " << operations << endl;
   }

   return 0;
}
