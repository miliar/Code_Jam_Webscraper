#include <set>
//#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;
//typedef long long LL;
typedef __int64 LL;
//typedef long double DB;
//typedef unisigned __int64 LL;
//typedef unsigned long long ULL;
#define EPS  1e-8
#define MAXN 1600
#define MAXE 300000
#define INF  0x3f3f3f3f
#define PI   acos(-1.0)
#define MOD  99991
//#define MOD  99990001
//#define MOD  1000000007
#define max(a,b) 	((a)>(b)?(a):(b))
#define min(a,b) 	((a)<(b)?(a):(b))
#define max3(a,b,c) (max(max(a,b),c))
#define min3(a,b,c) (min(min(a,b),c))
#define mabs(a) 	((a<0)?(-a):a)
//#define L(t) 		(t << 1)  //Left son t*2
//#define R(t) 		(t << 1 | 1) //Right son t*2+1
//#define Mid(a,b) 	((a+b)>>1) //Get Mid
//#define lowbit(a) (a&-a) //Get Lowbit
//int gcd(int a,int b){return b?gcd(b,a%b):a;}
//int lcm(int a,int b){return a*b/gcd(a,b);}
//std::ios::sync_with_stdio(false);
bool judge(int a) //is a n^2 ?
{
	int p = sqrt((double)a);
	if(p*p == a)
        return true;
    return false;
}
bool judge2(int a)
{
    int p[10],cnt=0;
    while(a){
        p[cnt++]=a%10;
        a/=10;
    }
    int i=cnt-1;
    while(p[cnt-1-i] == p[i] && i){i--;}
    if(i==0)
        return true;
    return false;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for(int t = 1; t <= T; t++)
	{
		int a,b;
		cin>>a>>b;
		int cnt = 0;
		for(int i = a; i<= b; i++)
        {
            int p = sqrt((double)i);
            if(judge(i) && judge2(i) && judge2(p))
            {
                //cout<<i<<endl;
                cnt++;
            }
        }
        printf("Case #%d: %d\n",t,cnt);
	}
    return 0;
}
