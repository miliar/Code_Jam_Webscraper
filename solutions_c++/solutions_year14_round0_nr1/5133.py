#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>
#include <fstream>

using namespace std;

ifstream fin("U:/work/input.in");
ofstream fout("U:/work/output.txt");

#define cin fin
#define cout fout

int T, p = 1, a, b, d;

int main()
{
	cin >> T; 
	while(T--)
	{
		vector<int>first, second;
		cin >> a; 
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
			{
				cin >> d;
				if(i == a)
					first.push_back(d);
			}

		cin >> b;
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
			{
				cin >> d;
				if(i == b)
					second.push_back(d);
			}


		vector<int>merged;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				if(first[i] == second[j])
					merged.push_back(first[i]);
		int ss = merged.size();
		if(ss == 0)
			cout << "Case #" << p++ << ": Volunteer cheated!\n";
		else if(ss == 1)
			cout << "Case #" << p++ << ": " << merged[0] << "\n";
		else
			cout << "Case #" << p++ << ": Bad magician!\n";
	}

	cout.close();
	cin.close();
	return 0;
}