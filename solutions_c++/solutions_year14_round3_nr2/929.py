//============================================================================
// Name        : code.cpp
// Author      : vlade087
// Version     : 1.0
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include<stdio.h>
#include<iostream>
#include<sstream>
#include<math.h>
#include<ctype.h>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<string.h>
#include<algorithm>
#include <complex>
#include <numeric>
#include<list>
#include<deque>
#include <stdlib.h>
#define printnVector(R) cout<<R.size()<<endl;for(int i =0;i<R.size();i++) cout<<R[i]<<" ";
#define mod 1000000007
#define inf 200000000000000L
#define countbits __builtin_popcount
#define sz sizeof
#define mp make_pair
#define pb push_back
#define ll long long
#define ull unsigned long long
#define mset memset
#define sz sizeof
#define maxn 32005
#define EPS 1e-9
#define par pair<int,int>
using namespace std;
int n,k,tt,x,y,t, r,p;
string cad,aux;
vector<int> P;
vector<string> C;
bool use[27];
int main()
{
	ios_base::sync_with_stdio(0);
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	cin>>tt;
	while(tt--)
	{
		cin>>n;
		P.clear();
		C.clear();
		bool check = true;
		for(int i = 0; i < n;i++)
		{
			P.pb(i);
			cin>>cad;
			aux = "";
			mset(use,0,sz(use));
			for(int i = 0; i < cad.length();i++)
			{
				if(!use[cad[i]-'a'])
				{
					use[cad[i]-'a'] = 1;
				}else
				{
					if(i && cad[i]!=cad[i-1]) check = 0;
				}
				if(i == 0 || cad[i]!=cad[i-1])
					aux+=cad[i];
			}
			C.pb(aux);
		}
		if(!check)
		{
			printf("Case #%d: 0\n",++t);
			continue;
		}
		int res = 0;
		do{
			cad = "";
			for(int i = 0; i < n;i++)
				cad+=C[P[i]];
			mset(use,0,sz(use));
			use[cad[0]-'a']=1;
			int ok = 1;
			for(int i = 1; i < cad.length();i++)
			{
				if(!use[cad[i]-'a'])
				{
					use[cad[i]-'a'] = 1;
				}else
				{
					if(cad[i]!=cad[i-1]) ok = 0;
				}
			}
			res+=ok;
		}while(next_permutation(P.begin(),P.end()));
		printf("Case #%d: %d\n",++t,res);
	}
	return 0;
}
