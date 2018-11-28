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
#define  MAXN     20
#define  eps      1e-6
FILE *fin;
FILE *fout;
int r1,r2;
int a[MAXN][MAXN];
int b[MAXN][MAXN];
int main()
{
   	fin=fopen("A-small-attempt4.in","r");
	fout=fopen("output.txt","w");
	int T;
	fscanf(fin,"%d",&T);
    int rounds;
	for (rounds=1;rounds<=T;rounds++)
	{
        fscanf(fin,"%d",&r1);r1--;
        REP(i,4) REP(j,4)fscanf(fin,"%d",&a[i][j]);
        fscanf(fin,"%d",&r2);r2--;
        REP(i,4) REP(j,4)fscanf(fin,"%d",&b[i][j]);
        vector<int> vi;
        rep(shu,1,17)
        {
            int f1=false,f2=false;
            REP(j,4) if(a[r1][j]==shu) f1=true;
            REP(j,4) if(b[r2][j]==shu) f2=true;
            if(f1&&f2) vi.PB(shu);
        }
        if (SZ(vi)==1)
        {
            printf("Case #%d: %d\n",rounds,vi[0]);
            fprintf(fout,"Case #%d: %d\n",rounds,vi[0]);
        }
        else if(SZ(vi)>0)
        {
            printf("Case #%d: %s\n",rounds,"Bad magician!");
            fprintf(fout,"Case #%d: %s\n",rounds,"Bad magician!");

        }
        else
        {
            printf("Case #%d: %s\n",rounds,"Volunteer cheated!");
            fprintf(fout,"Case #%d: %s\n",rounds,"Volunteer cheated!");

        }
    }
}
