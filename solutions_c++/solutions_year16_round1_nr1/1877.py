#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <vector>
#include <string>
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

      std::vector<char> result;
      for (int i = 0; i < S.size(); i++)
      {
         if (result.size() == 0)
            result.push_back(S[i]);
         else if (S[i] >= result[0])
            result.insert(result.begin(), S[i]);
         else 
            result.push_back(S[i]);
      }
      for (int i = 0; i < result.size(); i++)
         cout << result[i];
      std::cout << std::endl;
   }
	exit(0);
}
