#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000

void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

int n;

void sol()
{
	if (n==0)
	{
		cout << "INSOMNIA";
		return;
	}
	LL tmp = 0;
	bool digs[10];
	CLR(digs);
	int cnt = 0;
	FOR(a,1,1000000)
	{
		tmp += n;
		LL t2 = tmp;
		while (t2>0)
		{
			if (!digs[t2%10])
			{
				cnt++;
				if (cnt==10)
				{
					cout << tmp;
					return;
				}
			}
			digs[t2%10] = true;
			t2/=10;
		}
	}

	cout << "INSOMNIA";
	cerr << n << " " << "ins?\n";
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	FOR(z,1,T)
	{
		cin >> n;
		cout << "Case #" << z << ": ";
		sol();
		cout << "\n";
	}

	return 0;
}
