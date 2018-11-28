//g++ -std=c++11 -Wall -Wextra -O2 -o a a.cpp
#include <algorithm>
#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
   int T;
   array<int, 4> v, w; 

   cin >> T;
   for(int idx = 1; idx <= T; ++idx)
   {
		int r1, r2, x;
		cin >> r1;
		for(int i = 1; i <= 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				if(r1 == i) cin >> v[j];
				else cin >> x;
			}
		}
		
		cin >> r2;
		for(int i = 1; i <= 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				if(r2 == i) cin >> w[j];
				else cin >> x;
			}
		}
		
		int count = 0, sol = -1;
		for(int i = 0;  i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				if(v[i] == w[j]) ++count, sol = v[i];
			}
		}
		
		cout << "Case #" << idx << ": "; 
		if(0 == count) cout << "Volunteer cheated!\n";
		else if(1 == count) cout << sol << '\n';
		else cout << "Bad magician!\n";
   }
   
   return EXIT_SUCCESS;
}