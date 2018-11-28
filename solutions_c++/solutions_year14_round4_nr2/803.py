#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
using namespace std;
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(int i=(a);i<(int)(b);i++)
#define   per(i,a,b)  for(int i=((a)-1);i>=(int)(b);i--)
#define   PER(i,n)     per(i,n,0)
#define   REP(i,n)     rep(i,0,n)
#define   FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define   clr(a)      memset((a),0,sizeof (a))
#define   SZ(a)         ((int)((a).size()))
#define   CLEAR(a, v)    memset((a), (v), sizeof(a))
#define   ALL(v)          (v).begin(), (v).end()
#define   mabs(a)       ((a)>0?(a):(-(a)))
#define   PB push_back
#define   FI     first
#define   SE     second
#define   MP     make_pair
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
typedef long long int64;
#define   inf         1000000001
#define  MAXN     1020
#define  eps      1e-6
FILE *fin;
FILE *fout;
int N;
int a[MAXN];
int main()
{
   	fin=fopen("B-large.in","r");
	fout=fopen("output.txt","w");
	int T;
	fscanf(fin,"%d",&T);
    int rounds;
	for (rounds=1;rounds<=T;rounds++)
	{
        fscanf(fin,"%d",&N);
        REP(i,N) fscanf(fin,"%d",a+i);
        int l=0,r=N-1,ret=0;
        REP(i,N-1)
        {
            int mv=inf,mi=-1;
            rep(j,l,r+1) if(a[j]<mv) mv=a[j],mi=j;
            if(mi-l<r-mi)
            {
                ret+=mi-l;
                for(int j=mi;j>l;j--) swap(a[j],a[j-1]);
                l++;
            }
            else
            {
                ret+=r-mi;
                for(int j=mi;j<r;j++) swap(a[j],a[j+1]);
                r--;
            }
        }
            printf("Case #%d: %d\n",rounds,ret);
            fprintf(fout,"Case #%d: %d\n",rounds,ret);

    }
}
