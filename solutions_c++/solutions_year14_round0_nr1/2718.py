#if 1

#include <math.h>
#include <iostream>
#include <deque>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <string>
#include <ctime>
#include <vector>
using namespace std;
typedef long double LD; 
typedef long long LL; 

#define PROBLEM "A-small-attempt0"


void main()
{
	freopen(PROBLEM ".in","r",stdin); freopen(PROBLEM ".out","w",stdout);
	//freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
	time_t START = clock();

	int n; 
	cin >> n;
	int a1,a2;
	int q;
	vector <int> v1, v2;

	for (int t = 0; t < n; ++t)
	{
		v1.clear(); v2.clear();
		cin >> a1;
		for (int i = 0; i < 16; ++i)
		{
			cin >> q;
			if (i >= (a1-1) * 4 && i < a1 * 4)
			{
				v1.push_back(q);
			}
		}

		cin >> a2;
		for (int i = 0; i < 16; ++i)
		{
			cin >> q;
			if (i >= (a2-1) * 4 && i < a2 * 4)
			{
				v2.push_back(q);
			}
		}

		int cmp=0;
		int val;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				cmp += v1[i] == v2[j];
				if (v1[i] == v2[j])
					val = v1[i];
			}
		}

		cout << "Case #" << t+1 << ": ";
		switch (cmp)
		{
		case 0:
			cout << "Volunteer cheated!";
			break;
		case 1:
			cout << val;
			break;
		default:
			cout << "Bad magician!";
		}

		cout << endl;
	}

	time_t FINISH = clock(); 
	cerr << "Time = " << double(FINISH - START) / CLOCKS_PER_SEC << endl;
	return;
}
#endif