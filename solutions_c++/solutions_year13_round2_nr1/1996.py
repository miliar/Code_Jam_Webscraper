// taskA.cpp:
// By Andrew Moskalchuk (HorgH) 
//

#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <set>
#pragma comment(linker,"/STACK:16777216")
using namespace std;

//Loops
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define MEM(a,b) memset((a),(b),sizeof(a))

//Constants
#define inf 1000000000
#define pi 2*acos(0.0)
#define N 100010
#define eps 1e-9

//Functions
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sz(x) int((x).size())
#define sqr(a) (a)*(a)

//Pairs
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

//Input-Output
#define FREOPEN(a,b) freopen(a,"r",stdin); freopen(b,"w",stdout);

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;

int a[N]={0},dp1[N]={0},dp2[N]={0};
int rec(int pos,int n,int m)
{
	int d,res=0,s;
	if(pos < n)
	{
		if(a[pos]<m)return rec(pos+1,n,m+a[pos]);
		if(m==1)res=n-pos+1; else 
		{
				s=0;
				while(m<=a[pos])
				{
					s++;
					m=2*m-1;
				}
				res=min(n-pos+1,s+rec(pos+1,n,m+a[pos]));
		}
		return res;
	} else
	{
		if(a[pos]<m)return 0; else return 1;
	}
}
int main()
{
    FREOPEN("input.txt","output.txt");
	int test,ans=0,res,add,d,n,m;
	scanf("%d",&test);
	rep(tt,test)
	{
		scanf("%d%d",&m,&n);
		FOR(i,1,n)scanf("%d",&a[i]);
	    sort(a+1,a+n+1);
		if(a[n]>=m)
		{
			if(m==1)ans=n; else
			{
				add=0; ans=inf;
				FOR(i,1,n)
				{
					if(a[i]<m)m+=a[i]; else
					{
						ans=min(ans,add+n-i+1);
						while(m<=a[i])
						{
							add++;
							m=2*m-1;
						}
						m+=a[i];
					}
				}
				ans=min(ans,add);
			}
		} else ans=0;
		printf("Case #%d: %d\n",tt+1,ans);
	}
    return 0;   
}