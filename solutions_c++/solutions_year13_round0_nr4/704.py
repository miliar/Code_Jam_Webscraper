#include <iostream>
#include <sstream>
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <unordered_map>
#include <fstream>
#include <stdexcept>
#include <limits>
#include <array>
#include <memory> // note: i will use memory leaks, if its easier
#include "Solver.hpp"

using namespace std;

int main(int argc, char** argv) {
   // Read input
   if(argc != 2)
      throw invalid_argument("no input: ./a.out [filename]");
   string str(argv[1]);
   ifstream in(str);
   if(!in.good() || !in.is_open())
      throw invalid_argument("file not found");

   int numCases;
   in >> numCases;

   vector<unique_ptr<TreasureMap>> work;

   for(int c=1; c<=numCases; c++) {
      unique_ptr<TreasureMap> test(new TreasureMap);

      test->testNum = c;

      uint32_t chestCount;
      in >> test->numKeys;
      in >> chestCount;

      for(uint32_t i=0; i<test->numKeys; i++) {
         uint32_t d;
         in >> d;
         test->keys[d]++;
      }

      for(uint32_t i=0; i<chestCount; i++) {
         unique_ptr<Chest> chest(new Chest());
         chest->id = i + 1;
         in >> chest->requiredKey;

         uint32_t numContainingKeys;
         in >> numContainingKeys;

         for(uint32_t k=0; k<numContainingKeys; k++) {
            uint32_t key;
            in >> key;
            chest->containedKeys.push_back(key);
         }
         test->chests.push_back(::move(chest));
      }
      work.push_back(::move(test));
   }

   for(auto& iter : work) {
      Solver solver(*iter);
      string result = solver.solve();
      cout << result << endl;
   }

   return 0;
}
