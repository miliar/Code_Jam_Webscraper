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

int n, ts, tests;
int used[100];
int cur;

void eval(int x)
{
	while (x)
	{
		used[x % 10]=1;
		x /= 10;
	}
}

bool all10()
{
	for (int i = 0; i < 10; i++)
	{
		if (used[i] == 0)
			return false;
	}
	return true;
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
		cin >> n;
		++ts;
		cout << "Case #" << ts << ": ";
		if (n == 0)
		{
			cout << "INSOMNIA" << endl;
			continue;
		}
		for (int i = 0; i < 10; i++)
			used[i] = 0;
		cur = n;
		while (true)
		{
			eval(cur);
			if (all10())
			{
				cout << cur << endl;
				break;
			}
			cur += n;
		}
	}

	cin.get(); cin.get();
	return 0;
}