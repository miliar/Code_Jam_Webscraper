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
#define  MAXN     5
#define  eps      1e-6
FILE *fin;
FILE *fout;
int R,C,M;
vector<string> vs;
bool G[MAXN][MAXN];
int dfs(vector<string> &vt,int r,int c)
{
    int cnt=0,ret=1;
    rep(dx,-1,2) rep(dy,-1,2)
    {
        int nr=r+dx,nc=c+dy;
        if(nr<0||nr>=R||nc<0||nc>=C) continue;
        if(vt[nr][nc]=='*') cnt++;
    }
    if(cnt>0) return ret;
    rep(dx,-1,2) rep(dy,-1,2)
    {
        int nr=r+dx,nc=c+dy;
        if(nr<0||nr>=R||nc<0||nc>=C) continue;
        if(!G[nr][nc]&&vt[nr][nc]!='*') G[nr][nc]=true,ret+=dfs(vt,nr,nc);
    }
    return ret;
}
bool checkok(vector<string> &vt,int r,int c)
{
    clr(G);G[r][c]=true;
    int cnt=dfs(vt,r,c);
    return cnt==R*C-M;
}
void output(vector<string> &vt)
{
    REP(i,SZ(vt))
    {
        printf("%s\n",vt[i].c_str());
        fprintf(fout,"%s\n",vt[i].c_str());
    }
}
int main()
{
   	fin=fopen("C-small-attempt2.in","r");
	fout=fopen("output.txt","w");
	int T;
	fscanf(fin,"%d",&T);
    int rounds;
	for (rounds=1;rounds<=T;rounds++)
	{
        fscanf(fin,"%d%d%d",&R,&C,&M);
        int n=R*C;
        string s="";REP(i,C) s+=".";
        vs.clear();
        REP(i,R) vs.PB(s);
        REP(i,1<<n)
        {
            int cnt=0;
            REP(j,n) if(i&(1<<j)) cnt++;
            if(cnt==M)
            {
                vector<string> vt=vs;
                REP(r,R) REP(c,C)
                {
                    int pos=r*C+c; if(i&(1<<pos)) vt[r][c]='*';
                }
                REP(r,R) REP(c,C) if(vt[r][c]=='.')
                {
                    if(checkok(vt,r,c))
                    {
                        printf("Case #%d:\n",rounds);
                        fprintf(fout,"Case #%d:\n",rounds);
                        vt[r][c]='c';
                        output(vt);
                        goto next;
                    }
                }
            }
        }
        printf("Case #%d:\n",rounds);
        fprintf(fout,"Case #%d:\n",rounds);
        printf("Impossible\n");
        fprintf(fout,"Impossible\n");
        next:;
    }
}
