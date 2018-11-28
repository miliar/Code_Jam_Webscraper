/*************************************************************************
      > File Name: a.cpp
    > Author: caoyu01
    > Mail: yalecyu@gmail.com 
    > Created Time: 16/4/30 23:56:26
 ************************************************************************/
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <stdlib.h>
#include <map>
#include <vector>
#define rep(i,n) for(i=0;i<n;i++)
#define cle(x) memset(x,0,sizeof(x))
 
#define ll long long
const int maxn=2000+5;
using namespace std;
int u[maxn],n;
char s[maxn];
map<char,int>mp;
void solve()
{
	mp.clear();
	for(int i=0;i<n;i++)mp[s[i]]++;
	u[0]=mp['Z'];mp['E']-=mp['Z'],mp['R']-=mp['Z'],mp['O']-=mp['Z'];mp['Z']=0;
	u[2]=mp['W'];mp['T']-=mp['W'],mp['O']-=mp['W'];mp['W']=0;
	u[4]=mp['U'];mp['F']-=mp['U'],mp['O']-=mp['U'],mp['R']-=mp['U'],mp['U']=0;
	u[5]=mp['F'];mp['I']-=mp['F'],mp['V']-=mp['F'],mp['E']-=mp['F'],mp['F']=0;
	u[8]=mp['G'];mp['E']-=mp['G'],mp['I']-=mp['G'],mp['H']-=mp['G'],mp['T']-=mp['G'];mp['G']=0;	
	u[1]=mp['O'];mp['N']-=mp['O'],mp['E']-=mp['O'],mp['O']=0;
	u[3]=mp['T'];mp['H']-=mp['T'],mp['R']-=mp['T'],mp['E']-=2*mp['T'],mp['T']=0;
	u[6]=mp['X'];mp['S']-=mp['X'],mp['I']-=mp['X'],mp['X']=0;
	u[7]=mp['S'];mp['E']-=2*mp['S'],mp['V']-=mp['S'],mp['N']-=mp['S'],mp['S']=0;
	u[9]=mp['I'];
}
int main()
{
#ifndef ONLINE_JUDGE
     freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
#endif
	int T;cin>>T;
	for(int ca=1;ca<=T;ca++){
		scanf("%s",s);n=strlen(s);memset(u,0,sizeof u);
		solve();
		printf("Case #%d: ",ca);
		for(int i=0;i<10;i++)while(u[i]--)printf("%d",i);printf("\n");
	}
    return 0;
}
