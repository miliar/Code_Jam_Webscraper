/*
	NISHANT GUPTA
	CSE-MNNIT ALLAHABAD
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <algorithm>
#include <vector>
#include <cstring>
#include <stack>
#include <cctype>
#include <utility>
#include <map>
#include <string>
#include <climits>
#include <set>
#include <string>
#include <sstream>
#include <utility>
#include <ctime>
#include <cassert>
#include <fstream>
using namespace std;
 
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> II;
typedef vector<long long> VLL;
typedef vector<bool> VB;
 
#define SZ(A) ((int)A.size())
#define LEN(A) ((int)A.length())
#define MS(A) memset(A, 0, sizeof(A))
#define MSV(A,a) memset(A, a, sizeof(A))
#define MAX(a,b) ((a >= b) ? (a) : (b))
#define MIN(a,b) ((a >= b) ? (b) : (a))
#define ABS(a) (((a) > 0) ? (a) : (-a))
#define MP make_pair
#define X first
#define Y second
#define PB push_back
#define FOUND(A, x) (A.find(x) != A.end())
#define getcx getchar_unlocked
#define INF (int(1e9))
#define INFL (LL(1e18))
#define EPS 1e-12
 
#define chkbit(s, b) (s & (1<<b))
#define setbit(s, b) (s |= (1<<b))
#define clrbit(s, b) (s &= ~(1<<b))
#define rep(i, a, n) for(i = a; i < n; i++)
#define rev(i, a, n) for(i = a; i > n; i--)
#define FORALL(itr, c) for(itr = (c).begin(); itr != (c).end(); itr++)
#define ALL(A) A.begin(), A.end()
#define LLA(A) A.rbegin(), A.rend()

inline void inp( int &n ) 
{
    n=0;
    int ch=getcx();int sign=1;
    while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}
    while(  ch >= '0' && ch <= '9' )
            n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
    n=n*sign;
}   
	
int main()
{
	double naomi[1010],ken[1010];
	int i,j,k,x=1,t,n;
	inp(t);
	while(x<=t)
	{
		inp(n);
		rep(i,0,n)
			scanf("%lf",&naomi[i]);
		rep(i,0,n)
			scanf("%lf",&ken[i]);
		
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		//deceitful war
		k=n-1;int dw=0,w=0;
		for(i=n-1;i>=0;i--)
		{
			while(k>=0)
			{
				if(naomi[i]>ken[k])
				{k--;dw++;break;}
				k--;
			}
			if(k<0)break;
		}
		//war
		k=0;
		for(i=0;i<n;i++)
		{
			while(k<n)
			{
				if(naomi[i]<ken[k])
				{k++;w++;break;}
				k++;
			}
			if(k>=n)break;
		}
		w=n-w;
		printf("Case #%d: %d %d\n",x++,dw,w);
	}
	return 0;
}
