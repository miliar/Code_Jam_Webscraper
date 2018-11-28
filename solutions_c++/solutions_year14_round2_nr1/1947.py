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
#define rep(i, a, n) for(int i = a; i < n; i++)
#define rev(i, a, n) for(int i = a; i > n; i--)
#define FORALL(itr, c) for(itr = (c).begin(); itr != (c).end(); itr++)
#define ALL(A) A.begin(), A.end()
#define LLA(A) A.rbegin(), A.rend()
inline void inp( int &n )
{ 
	n=0;    int ch=getcx();int sign=1;   
	while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();} 
	while(  ch >= '0' && ch <= '9' )    
	n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
	n=n*sign;
}   	

int main()
{
	int t,i,j,n,k,x=1;
	inp(t);
	char a[105],b[105],sx[150],sy[150];
	int fx[150],fy[150];
	while(x<=t)
	{
		inp(n);
		scanf("%s",a);
		scanf("%s",b);
		int c=1;sx[0]=a[0];sy[0]=b[0];int p=0,q=0;
		for(i=1;a[i]!='\0';i++)
		{
			if(a[i]==a[i-1])c++;
			else
			{
				sx[p]=a[i-1];
				fx[p]=c;
				p++;
				c=1;
			}
		}
		sx[p]=a[i-1];fx[p++]=c;
		c=1;
		for(i=1;b[i]!='\0';i++)
		{
			if(b[i]==b[i-1])c++;
			else
			{
				sy[q]=b[i-1];
				fy[q]=c;
				q++;
				c=1;
			}
		}
		sy[q]=b[i-1];fy[q++]=c;
		int ans=0,f=0;
		printf("Case #%d: ",x++);
		/*rep(i,0,p)printf("%c",sx[i]);
		printf("\n");
		rep(i,0,q)printf("%c",sy[i]);*/
		if(p==q)
		{
			for(i=0;i<p;i++)
			{
				if(sx[i]==sy[i])
					ans+=ABS((fx[i]-fy[i]));
				else {f=1;break;}
			}
			if(f)printf("Fegla Won\n");
			else printf("%d\n",ans);
		}
		else printf("Fegla Won\n");
	}
	return 0;
}
