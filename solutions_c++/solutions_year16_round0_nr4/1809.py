//#pragma comment(linker, "/STACK:16777216")
#define _CRT_SECURE_NO_WARNINGS

#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <ctime>
#include <memory.h>
#include <assert.h>

#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
#define norm asdfasdgasdgsd

#define eps 1e-9
#define M_PI 3.141592653589793
#define bs 1000000007
#define bsize 256

using namespace std;

const int N = 300031;

int tests;
int ts;
long long K, C, S;
vector<long long> taken;

long long where_starts(long long id, int levels)
{
	while (levels)
	{
		id *= K;
		levels--;
	}
	return id;
}

bool used(int x)
{
	for (int i = 0; i < taken.size(); i++)
	{
		if (taken[i] == x)
			return true;
	}
	return false;
}

long long fun()
{
	for (int i = 1;; i++)
	{
		if (used(i))
			continue;
		return i;
	}
}

int main(){
	//freopen("fabro.in","r",stdin);
	//freopen("fabro.out","w",stdout);
	freopen("F:/in.txt", "r", stdin);
	freopen("F:/output.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	//cin.tie(0);

	cin >> tests;
	for (; tests; --tests)
	{
		++ts;
		cout << "Case #" << ts << ": ";
		cin >> K >> C >> S;
		if (C == 1)
		{
			if (S == K)
			{
				for (int i = 1; i <= K; i++)
				{
					if (i > 1)
						cout << " ";
					cout << i;
				}
				cout << endl;
			}
			else
			{
				cout << "IMPOSSIBLE" << endl;
			}
			continue;
		}
		if (S * 2 < K)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		taken.clear();

		for (int i = 1; i <= S; i++)
		{
			if (i * 2 - 1 > K)
			{
				long long val = fun();
				taken.push_back(val);
				continue;
			}
			long long val = where_starts(i * 2 - 2, C - 1);
			if (i * 2 - 1 == K)
				taken.push_back(val + i * 2 - 1);
			else
				taken.push_back(val + i * 2);
		}
		for (int i = 0; i < taken.size(); i++)
		{
			if (i)
				cout << " ";
			cout << taken[i];
		}
		cout << endl;
	}

	cin.get(); cin.get();
	return 0;
}