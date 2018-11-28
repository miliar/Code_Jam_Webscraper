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
int sum[10001000];

bool check(LL x)
{
	char str[20];
	sprintf(str, "%lld", x);
	int sz = (int)strlen(str);
	int i=0, j=sz-1;
	while(i<j)
	{
		if (str[i]!=str[j]) return false;
		i++; j--;
	}
	return true;
}

void init()
{
	sum[0]=1;
	FOR(a,1,10000000)
	{
		sum[a]=sum[a-1];
		if (check(a))
			if (check((LL)a*a))
				sum[a]++;
	}
	cerr << "init ok\n";
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	init();

	int T, cur_t=0;
	RE("%d", &T);
	FOR(z,1,T)
	{
		cur_t++;
		
		LL A, B;
		cin >> A >> B;
		int ans = 0;
		for (LL a = (LL)sqrt((double)B)+10; ; a--)
			if (a*a <= B)
			{
				ans += sum[(int)a];
				break;
			}
		LL tmp = (LL)sqrt((double)A)-10;
		if (tmp<0) tmp = 0;
		for (LL a = tmp; ; a++)
			if (a*a >= A)
			{
				ans -= sum[(int)a-1];
				break;
			}

		cout << "Case #" << cur_t << ": ";
		cout << ans;
		cout << "\n";
	}

	return 0;
}
