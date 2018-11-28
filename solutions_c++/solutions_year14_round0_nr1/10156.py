#include<iostream>
#include<cstdio>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#define FOR(a,b,c) for(int a=b;a<=c;++a)
#include<cstring>
#include<bitset>
#include<cmath>
#include<iomanip>
#include<queue>
#define f cin
#define g cout
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ll long long
#define bit 20
#define inf (1<<30)
#define base 256
#define ba 255
#define N 100100
using namespace std;
int nrt,a[5][5],r,val,v[5],u[5],match,T;
int main ()
{
	#ifndef ONLINE_JUDGE
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    #endif
	
	f>>T;
	while(T--)
	{
		match=0;
		nrt++;
		f>>r;
		FOR(i,1,4)
		FOR(j,1,4)
		f>>a[i][j];
		
		v[1]=a[r][1]; v[2]=a[r][2]; v[3]=a[r][3]; v[4]=a[r][4];
		
		f>>r;
		FOR(i,1,4)
		FOR(j,1,4)
		f>>a[i][j];
		
		sort(v+1,v+5);
		
		FOR(i,1,4)
		u[i]=a[r][i];
		
		sort(u+1,u+5);
		match=0;
		FOR(i,1,4)
		FOR(j,1,4)
		{
			if(u[i]==v[j])
			{
				val=u[i];
				++match;
			}
		}
		if(!match)
			g<<"Case #"<<nrt<<": Volunteer cheated!";
		if(match>1)
			g<<"Case #"<<nrt<<": Bad magician!";
		if(match==1)
			g<<"Case #"<<nrt<<": "<<val;
		
		g<<"\n";
	}
	return 0;
}