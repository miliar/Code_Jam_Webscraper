#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <functional>
#include <math.h>
#include <assert.h>
#include <stdarg.h>
#include <time.h>
#include <limits.h>
#include <ctype.h>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <stack>
#include <bitset>
#include <fstream>
using namespace std;
// }}}
// #defines {{{
#define _CRT_SECURE_NO_WARNINGS
#define ALL(x) (x).begin(),(x).end()
#define ALL2(arr,x) (arr),(arr+x)
#define fl2(i,n) for(int i=0;i<(n);i++)
#define fl3(i,a,b) for(int i=(a);i<=(b);i++)
#define flx(i,a,x) for(int i=0;i<(a);i+=(x))
#define ifl2(i,n) for(int i=(n);i>=0;i--)
#define ifl3(i,a,b) for(int i=(a);i>=(b);i--)
#define iflx(i,a,x) for(int i=(a)-1;i>=0;i-=(x))
#define RI(x) scanf("%d",&x)
#define DRI(x) int x;RI(x)
#define InDAL(arr,x) int *arr=new int[x]
#define ChDAL(x) new char[x]
#define RII(x,y) scanf("%d %d",&x,&y)
#define DRII(x,y) int x,y;RII(x,y)
#define RIII(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define DRIII(x,y,z) int x,y,z;RIII(x,y,z)
#define PI(x) cout<<x
#define FLch(i,x) for(int i=0;x[i];i++)
#define F first
#define S second
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
#define INF INT_MAX
#define NINF INT_MIN
#define inF(s) freopen(s,"r",stdin)
#define outF(s) freopen(s,"w",stdout)
#define MOD 1000003
//#define INF 2000000000 // 2 billion
// If you need to recall how to use memset:
//#define MEMSET_INF 127 // about 2B
//#define MEMSET_HALF_INF 63 // about 1B
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); // useful to clear array of integers
int main(){	
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
		DRI(t);
		int x=t;
		while(t--)
		{
			DRI(sm);
			vi in(sm+1);
			char c;
			fl2(i,sm+1)			
			{
				cin>>c;
				in[i]=c-'0';
			}
			int f_counter=0,counter=in[0];
			for (int i=1;i<=sm;i++)
			{				
				if (counter<i) {
					f_counter+=(i-counter);
					counter+=(i-counter);
				}
				counter+=in[i];				
			}
			cout<<"Case #"<<x-t<<": "<<f_counter<<endl;			
		}
return 0;
}
