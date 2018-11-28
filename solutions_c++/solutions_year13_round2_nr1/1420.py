#pragma comment (linker, "/STACK:10000000")

#include <string>
#include <vector>
#include <list>
#include <iostream>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <map>

#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))  
#define RFOR(i,a,b) for(int (i) = (a)-1; (i) >= (b); --(i))  
#define CLEAR(a) memset((a),0,sizeof(a))  
#define INF 1000000000  
#define PB push_back  
#define ALL(c) (c).begin(), (c).end()  
#define pi acos(-1.0)  
#define SQR(a) (a)*(a)  
#define MP make_pair  
#define MAX 100000
#define MOD 1000000007
#define PII pair<double,double>

using namespace std;

int t,n,m,sol;
int a[101];

int main()
{    

#ifdef	ONLINE_JUDGE
// freopen(fin,"r",stdin);
// freopen(fout,"w",stdout);
#else
 //freopen("input.txt","r",stdin);
 //freopen("output.txt","w",stdout);
#endif

 cin >> t;
 FOR(test,0,t)
 {
 cin >> m >> n;
   sol=1000000000;
   FOR(i,0,n) cin >> a[i];
   sort(a,a+n);

 
		FOR(j,0,n+1)
		{
			int can=m;
			int r=n-j;
			int now=0;
			while (now<j)
			{
				if (a[now]<can)
				{
					can+=a[now];
					now++;
				}
				else
				{
					r++;
					if (can!=1) can+=can-1;
					else
					{
						r=1000000000;
						break;
					}
				}				
			}

			sol=min(sol,r);
		}


    cout << "Case #" << test+1 <<": "<< sol << endl;
 }



   return 0;
}