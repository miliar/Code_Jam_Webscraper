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

#define PROBLEM "D-large"

vector <double> a, b;

int W()
{
	map <int, int> usedB;
	bool Bwin;
	int Awin = 0;
	for (int i = a.size()-1; i >= 0; --i)
	{
		Bwin = 0;
		for (int j = b.size()-1; j >= 0 && !Bwin; --j)
		{
			if (b[j] > a[i] && !usedB[j])
			{
				Bwin = 1;
				usedB[j] = 1;
			}
		}
		Awin += !Bwin;
	}

	return Awin;
}

int DW()
{
	map <int, int> usedA;
	bool Awin;
	int Bwin = 0;
	for (int i = 0; i < b.size(); ++i)
	{
		Awin = 0;
		for (int j = 0; j < a.size() && !Awin; ++j)
		{
			if (a[j] > b[i] && !usedA[j])
			{
				Awin = 1;
				usedA[j] = 1;
			}
		}
		Bwin += !Awin;
	}

	return a.size() - Bwin;
}

void main()
{
	freopen(PROBLEM ".in","r",stdin); freopen(PROBLEM ".out","w",stdout);
	//freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
	time_t START = clock();

	int n; 
	cin >> n;
	int cnt;

	for (int t = 1; t <= n; ++t)
	{
		cin >> cnt;
		a.resize(cnt);
		b.resize(cnt);

		for (int i = 0; i < cnt; ++i)
			cin >> a[i];
		for (int i = 0; i < cnt; ++i)
			cin >> b[i];

		sort(a.begin(), a.end());
		sort(b.begin(), b.end());

		/*for (int i = 0; i < cnt; ++i)
		{
			printf("%.6f		%.6f\n", a[i], b[i]);
		}*/

		cout << "Case #" << t << ": " << DW() << ' ' << W() << endl;
	}

	time_t FINISH = clock(); 
	cerr << "Time = " << double(FINISH - START) / CLOCKS_PER_SEC << endl;
	return;
}
#endif