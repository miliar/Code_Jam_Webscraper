#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;
typedef long long LL;


main() {
	int T;
	cin >> T;
   std::string dummy;
   std::getline(std::cin, dummy);
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
      std::string inputS;
      std::getline(std::cin, inputS);
      std::vector<char> S;
      for (int i = 0; i < inputS.size(); i++)
         if ((inputS[i] >= 'A') && (inputS[i] <= 'Z'))
            S.push_back(inputS[i]);

      std::map<char, int> count;
      for (int i = 0; i < S.size(); i++)
         count[S[i]] = count[S[i]] + 1;
      std::map<int, int> result;
      while (1) 
      {
         if (count['Z'] != 0)
         {
            result[0] = result[0] + 1;
            count['Z']--;
            count['E']--;
            count['R']--;
            count['O']--;
            continue;
         }
         if (count['W'] != 0)
         {
            result[2] = result[2] + 1;
            count['T']--;
            count['W']--;
            count['O']--;
            continue;
         }
         if (count['U'] != 0)
         {
            result[4] = result[4] + 1;
            count['F']--;
            count['O']--;
            count['U']--;
            count['R']--;
            continue;
         }
         if (count['X'] != 0)
         {
            result[6] = result[6] + 1;
            count['S']--;
            count['I']--;
            count['X']--;
            continue;
         }
         break;
      }
      while (count['F'] != 0)
      {
         result[5] = result[5] + 1;
         count['F']--;
         count['I']--;
         count['V']--;
         count['E']--;
      }
      while (count['V'] != 0)
      {
         result[7] = result[7] + 1;
         count['S']--;
         count['E']--;
         count['V']--;
         count['E']--;
         count['N']--;
      }
      while (count['G'] != 0)
      {
         result[8] = result[8] + 1;
         count['E']--;
         count['I']--;
         count['G']--;
         count['H']--;
         count['T']--;
      }
      while (count['H'] != 0)
      {
         result[3] = result[3] + 1;
         count['T']--;
         count['H']--;
         count['R']--;
         count['E']--;
         count['E']--;
      }
      while (count['O'] != 0)
      {
         result[1] = result[1] + 1;
         count['O']--;
         count['N']--;
         count['E']--;
      }
      while (count['N'] != 0)
      {
         result[9] = result[9] + 1;
         count['N']--;
         count['I']--;
         count['N']--;
         count['E']--;
      }

      for (std::map<int, int>::iterator it = result.begin(); it != result.end(); ++it)
      {
         int num = it->first;
         int c = it->second;
         for (int j = 1; j <= c; j++)
            cout << num;
      }
      cout << std::endl;
   }
	exit(0);
}
