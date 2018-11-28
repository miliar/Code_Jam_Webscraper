#include "Counting_Sheep.h"
#include <iostream>
#include<string>
#include <algorithm>
#include<fstream>
#include <vector>
#include<cstdio>
#include<math.h>
#include<utility>
#include<queue>
#include<iomanip>



using namespace std;


int main(){
	int T; cin >> T;
	for (int k = 0; k < T; k++)
	{
		int i;
		cin >> i;
		if (i == 0){
			cout <<"Case #"<<k+1<< ": INSOMNIA" << endl;
			continue;
		}
		bool ok = true;
		bool* used = new bool[10];
		int z = 1;
		long long x;
		while (ok)
		{
			x = i *z;
			string s  = to_string(x);
			for (int j = 0; j < s.size(); j++)
			{
				used[(s[j] - '0')] = true;
			}
			for (int j = 0; j < 10; j++)
			{
				if (used[j] == true){
					if (j == 9)ok = false;
				}
				else break;
			}
			z++;
		}
		cout << "Case #" << k + 1 << ": " << x << endl;
	}
	
	
}