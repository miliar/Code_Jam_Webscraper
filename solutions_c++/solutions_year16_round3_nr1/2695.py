#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <cstdlib>

using namespace std;

bool toSpaceOrNah(int numSinceLastSpace, int totalMembers, vector<int> partyMembers) {
   //if someone else now has the majority that something was removed, don't space
   if (totalMembers == 0)
      return false;
   for (int k = 0; k < partyMembers.size(); k++) {
      if ((double)partyMembers[k] / (totalMembers) > .5)
         return false;
   }
   cout << " ";
   return true;
   /*
   if (numSinceLastSpace > 1) {
      cout << " ";
      return true;
   } else {
      if (totalMembers == 0)
         return false;
      //if on next round (double)partyMembers[k] / (totalMembers-1) > .5 is false for all
      //AND if first non-zero party is decremented and totalmembers is decremented
      //a majority is given, then space after 1 output is needed
      bool majority = false;
      for (int k = 0; k < partyMembers.size(); k++) {   
         if ((double)partyMembers[k] / (totalMembers-1) > .5)
            majority = true;
      }
      if (!majority) {
         int fakeDecremement = 0;
         //find first non-zero
         for (int k = 0; k < partyMembers.size(); k++) {
            if (partyMembers[k] > 0) {
               fakeDecremement = k;
               partyMembers[k]--;
               break;
            }
         }
         for (int k = 0; k < partyMembers.size(); k++) {
            if ((double)partyMembers[k] / (totalMembers-1) > .5)
               cout << " ";
               return true;
         }
      }
   }
   return false;
   */
}

int main() {
   string line;
   ifstream iFile("input.txt");
   if (!iFile.is_open()) {
      cout << "Input file not found." << endl;
      return 1;
   }
   getline(iFile, line);
   int numCases = strtol(line.c_str(),0,10);
   for (int i = 0; i < numCases; i++) {
      getline(iFile, line);
      int numParties = strtol(line.c_str(),0,10);
      getline(iFile, line);
      istringstream iss(line);
      vector<string> tokens;
      vector<int> partyMembers;
      int totalMembers = 0;
      copy(istream_iterator<string>(iss),
           istream_iterator<string>(),
           back_inserter(tokens));
      for (int j = 0; j < tokens.size(); j++) {
         partyMembers.push_back(strtol(tokens[j].c_str(),0,10));
         totalMembers += partyMembers[j];
      }
      int numSinceLastSpace = 0;
      cout << "Case #" << i+1 << ": ";
      while (totalMembers > 0) {
         for (int j = 0; j < partyMembers.size(); j++) {
            if (totalMembers == 1)
               break;
            if ((double)partyMembers[j] / (totalMembers-1) > .5) {
               cout << (char)(j+65);
               totalMembers--;
               partyMembers[j]--;
               numSinceLastSpace++;
               //Decide whether or not to space
                if(toSpaceOrNah(numSinceLastSpace, totalMembers, partyMembers))
                   numSinceLastSpace = 0;
               j = -1;
            }
         }
         if (totalMembers != 0) {
            //If you've reached here it doesn't matter no one will get majority
            //take out the first non 0 party member
            for (int j = 0; j < partyMembers.size(); j++) {
               if (partyMembers[j] > 0) {
                  cout << (char)(j+65);
                  totalMembers--;
                  partyMembers[j]--;
                  numSinceLastSpace++;
                  //Decide whether or not to space
                   if(toSpaceOrNah(numSinceLastSpace, totalMembers, partyMembers))
                      numSinceLastSpace = 0;
                  break;
               }
            }
         }
      }
      for (int j = 0; j < partyMembers.size(); j++) {
    //     cout << partyMembers[j] << " ";
      }
      cout << endl;
   }
   iFile.close();
   return 0;
}
