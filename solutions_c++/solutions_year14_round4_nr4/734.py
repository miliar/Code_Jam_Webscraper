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
int N,M;
string s[MAXN];
char cs[MAXN];
int r1,r2;
vector<int> vi[MAXN];
int cal(vector<int> &vi)
{
    set<string> si;
    if(SZ(vi)==0) return 0;
    si.insert("");
    REP(i,SZ(vi))
    {
        string sn=s[vi[i]];
        rep(i,1,sn.length()+1) si.insert(sn.substr(0,i));
    }
    return SZ(si);
}
void dfs(int idx)
{
    if(idx==M)
    {
        int cnt=0;
        REP(i,N)
        {
            cnt+=cal(vi[i]);
        }
        if(cnt>r1) r1=cnt,r2=1;
        else if(cnt==r1) r2++;
        return;
    }
    REP(i,N)
    {
        vi[i].PB(idx);
        dfs(idx+1);
        vi[i].pop_back();
    }
}
int main()
{
    fin=fopen("D-small-attempt1.in","r");
	fout=fopen("output.txt","w");
	int T;
	fscanf(fin,"%d",&T);
    int rounds;
	for (rounds=1;rounds<=T;rounds++)
	{
        fscanf(fin,"%d%d",&M,&N);
        REP(i,MAXN) vi[i].clear();
        REP(i,M)
        {
            fscanf(fin,"%s",cs); s[i]=string(cs);
        }
        r1=-1,r2=0;
        dfs(0);
            printf("Case #%d: %d %d\n",rounds,r1,r2);
            fprintf(fout,"Case #%d: %d %d\n",rounds,r1,r2);

    }
}
