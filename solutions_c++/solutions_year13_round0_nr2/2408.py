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
#include <memory> // note: i will use memory leaks, if its easier

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

   for(int c=1; c<=numCases; c++) {
      int yin;
      in >> yin;

      int xin;
      in >> xin;

      vector<vector<int>> field(xin, vector<int>(yin));
      in.get();

      // lines
      for(int i=0; i<yin; i++) {
         string lineBuffer;
         getline(in, lineBuffer, '\n');
         istringstream line(lineBuffer);
         for(int j=0; j<xin; j++)
            line >> field[j][i];
      }


      // process ------------------------------

      for(int x=0; x<xin; x++) {
         for(int y=0; y<yin; y++) {
            bool existsBiggerX = false;
            bool existsBiggerY = false;
            int val = field[x][y];

            // check row
            for(int cur=0; cur<xin; cur++) {
               if(val < field[cur][y]) {
                  existsBiggerX = true;
                  break;
               }
            }

            // check col
            for(int cur=0; cur<yin; cur++) {
               if(val < field[x][cur]) {
                  existsBiggerY = true;
                  break;
               }
            }

            if(existsBiggerX && existsBiggerY)
               goto fail;
         }
      }

      cout << "Case #" << c << ": YES" << endl;
      continue;

      fail:
         cout << "Case #" << c << ": NO" << endl;
         continue;
   }

   return 0;
}
