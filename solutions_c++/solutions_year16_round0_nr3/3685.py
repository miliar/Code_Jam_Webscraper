#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include<climits>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,x,n) for(int i=x;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define OI(X) printf("%d",X);
#define RS(X) scanf("%s", (X))
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define LEN(X) strlen(X)
#define F first
#define S second
#define Swap(a, b) (a ^= b, b ^= a, a ^= b)
#define Dpoint  strcut node{int x,y}
#define cmpd int cmp(const int &a,const int &b){return a>b;}

 /*#ifdef HOME
    freopen("in.txt","r",stdin);
    #endif*/
const int MOD = 1e9+7;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
//#define HOME

int Scan()
{
	int res = 0, ch, flag = 0;

	if((ch = getchar()) == '-')				//判断正负
		flag = 1;

	else if(ch >= '0' && ch <= '9')			//得到完整的数
		res = ch - '0';
	while((ch = getchar()) >= '0' && ch <= '9' )
		res = res * 10 + ch - '0';

	return flag ? -res : res;
}
/*----------------PLEASE-----DO-----NOT-----HACK-----ME--------------------*/


int ans[35];
 int N,J;
 int check(long long int k)
 {  int m=sqrt(k);
     for(int i=2;i<=m;i++)
     {
         if(k%i==0)
            return i;
     }
     return -1;
 }
void dfs(int cur,long long int res2,long long int res3,long long int res4,long long int res5,long long int res6,long long int res7,long long int res8,long long int res9,long long int res10)
{
        if(J==0)
            return;
     if(cur==N)
{
    int t2=check(res2);
    int t3=check(res3);
    int t4=check(res4);
    int t5=check(res5);
    int t6=check(res6);
    int t7=check(res7);
    int t8=check(res8);
    int t9=check(res9);
    int t10=check(res10);
    if(t2!=-1&&t3!=-1&&t4!=-1&&t5!=-1&&t6!=-1&&t7!=-1&&t8!=-1&&t9!=-1&&t10!=-1)
    {
        for(int i=0;i<N;i++)
            printf("%d",ans[i]);
        printf(" %d %d %d %d %d %d %d %d %d\n",t2,t3,t4,t5,t6,t7,t8,t9,t10);
        J--;
    }
    return;
}
    ans[cur]=1;
    dfs(cur+1,res2*2+1,res3*3+1,res4*4+1,res5*5+1,res6*6+1,res7*7+1,res8*8+1,res9*9+1,res10*10+1);
    if(cur!=0&&cur!=N-1)
    {ans[cur]=0;
    dfs(cur+1,res2*2,res3*3,res4*4,res5*5,res6*6,res7*7,res8*8,res9*9,res10*10);}
}
int main()
{int T;
freopen("C-small-attempt3.in","r",stdin);
freopen("out.txt","w",stdout);
RI(T);
printf("Case #1:\n");
for(int t=1;t<=T;t++)
{

    RII(N,J);
    dfs(0,0,0,0,0,0,0,0,0,0);
}



        return 0;
}

