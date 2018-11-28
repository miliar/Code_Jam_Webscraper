
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <memory.h>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#pragma comment(linker,"/STACK:16777216")
 
using namespace std;
 
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define MEM(a,b) memset((a),(b),sizeof(a))
#define N 6250010
#define inf 1000000000
#define pi 2*acos(0.0)
#define eps 1e-9
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sz(x) int((x).size())
#define mp(a,b) make_pair((a), (b))
#define FREOPEN(a,b) freopen(a,"r",stdin); freopen(b,"w",stdout);
 
typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;


char f[12][12]={0},ans[12][12];
int  u[12][12]={0};
int dx[8]={1,-1,0,0,1,1,-1,-1};
int dy[8]={0,0,1,-1,1,-1,1,-1};
bool ok;
int mines(int x,int y)
{
	int cnt=0;
	rep(i,8)
		if(f[x + dx[i]][y + dy[i]] == '*')cnt++;
	return cnt;
}
void make_click(int r,int c,int x,int y)
{
	if(x < 1 || y < 1 || x > r || y > c || u[x][y] || f[x][y] == '*')return;
	u[x][y]=true;
	if(!mines(x,y))
	{
		rep(i,8)make_click(r,c,x + dx[i],y + dy[i]);
	}
}
bool can(int m,int r,int c,int x,int y)
{
	int cnt=0;
	MEM(u,0);
	make_click(r,c,x,y);
	FOR(i,1,r)
		FOR(j,1,c)cnt+=u[i][j];
	return cnt == r * c - m;
}
void rec(int k,int m,int r,int c,int ind,char c1,char c2)
{
	//printf("%d %d %d %d\n",r,c,k,ind);
	if(r * c -  ind < k || ok)return;
	if(!k)
	{
		FOR(i,1,r)
		{
			FOR(j,1,c)
				if(f[i][j] == '.' && can(m,r,c,i,j))
				{
					f[i][j]='c';
					ok=true;
					break;
				}
			if(ok)break;
		}
		if(ok)
		{
	
			FOR(i,1,r)
				FOR(j,1,c)ans[i][j]=f[i][j];
		}
		return;
	}
	FOR(i,ind+1,r * c)
	{
		int x=(i - 1) / c,y=i % c;
		x++;
		if(!y)y=c;
		f[x][y]=c1;
		rec(k-1,m,r,c,i,c1,c2);
		if(ok)break;
		f[x][y]=c2;
	}
}
void fillMatr(int k,int m,int r,int c,int ind,char c1,char c2)
{
	MEM(f,0);
	FOR(i,1,r)
		FOR(j,1,c)f[i][j]=c2;
	int x=(ind - 1) / c,y=ind % c;
	x++;
	if(!y)y=c;
	f[x][y]=c1;
	rec(k-1,m,r,c,ind,c1,c2);
}
int main()
{
    FREOPEN("input.txt","output.txt");
	int test;
	int r,c,m,k,res;
	char c1,c2;
	/*
	3 5 7
	****.
	*....
	*.c..
	
	r=3; c=5; m=7;
	f[1][1]=f[1][2]=f[1][3]=f[1][4]=f[2][1]=f[3][1]='*';
	res=can(m,r,c,3,2);
	printf("%d\n",res);
	*/
	
	scanf("%d",&test);
	rep(t,test)
	{
		scanf("%d%d%d",&r,&c,&m);
		if(!m)
		{
			FOR(i,1,r)
				FOR(j,1,c)ans[i][j]='.';
			ans[1][1]='c';
			printf("Case #%d:\n",t+1);
			FOR(i,1,r)
			{
				FOR(j,1,c)printf("%c",ans[i][j]);
				printf("\n");
			}
		} else
		{
			ok=false;
			if(m < r * c - m)c1='*',c2='.',k=m; else
							 c1='.',c2='*',k=r * c - m;
			FOR(ind,1,r * c - k + 1)
			{
					fillMatr(k,m,r,c,ind,c1,c2);
					if(ok)break;
			}
			printf("Case #%d:\n",t+1);
			if(!ok)puts("Impossible"); else
			{
				FOR(i,1,r)
				{
					FOR(j,1,c)printf("%c",ans[i][j]);
					printf("\n");
				}
			}
		}
	}
	
	return 0;   
} 
