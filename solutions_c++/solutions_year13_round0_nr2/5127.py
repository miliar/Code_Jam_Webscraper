/*
uva :
author : rafsan
algo :
*/
#include<iostream>
#include<algorithm>
#include<bitset>
#include<cctype>
#include<cmath>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<climits>
#include<functional>
#include<istream>
#include<iterator>
#include<iomanip>
#include<list>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<utility>
#include<vector>

using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b-1);i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)

#define INF INT_MAX/3
#define PB push_back
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define SET(a,c) memset(a,c,sizeof a)
#define CLR(a) memset(a,0,sizeof a)
#define PII pair<int,int>
#define PCC pair<char,char>
#define PIC pair<int,char>
#define PCI pair<char,int>
#define FST first
#define SEC second
#define VS vector<string>
#define VI vector<int>
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define MIN(a,b) (a>b?b:a)
#define MAX(a,b) (a>b?a:b)
#define PI acos(-1.0)
#define RADIANS(x) (((1.0 * x * PI) / 180.0))
#define DEGREES(x) (((x * 180.0) / (1.0 * pi)))
#define SINE(x) (sin(RADIANS(x)))
#define COSINE(x) (cos(RADIANS(x)))
#define SETBIT(x, i) (x |= (1 << i))
#define TANGENT(x) (tan(RADIANS(x)))
#define ARCSINE(x) (DEGREES((asin(x))))
#define RESETBIT(x, i) (x &= (~(1 << i)))
#define ARCCOSINE(x) (DEGREES((acos(x))))
#define ARCTANGENT(x) (DEGREES((atan(x))))
#define INFILE() freopen("B-large.in","r",stdin)
#define OUTFILE()freopen("B_large.out","w",stdout)
#define IN scanf
#define OUT printf
#define LL long long
#define ULL unsigned long long
#define EPS 1e-9
#define MOD 10007
#define LIM 4

//int dx[]= {0,0,1,-1};
//int dy[]= {-1,1,0,0};

int g[110][110];
int mark[110][110];
priority_queue<int>pq;
int main()
{
    int ks,m,n,val,state;
    INFILE();
    OUTFILE();
    cin>>ks;
    FOR(cas,1,ks+1)
    {

        IN("%d %d",&n,&m);
        FOR(i,0,n)
        FOR(j,0,m)
        {
            cin>>g[i][j];
            mark[i][j]=100;
            pq.push(g[i][j]);
        }

        while(!pq.empty())
        {
            val=pq.top();
            pq.pop();
            for(int i=0; i<n; i++)
            {
                state=0;
                for(int j=0; j<m; j++)
                    if(g[i][j]>val)
                    {
                        state=1;
                        break;
                    }
                if(state==0)
                {
                    FOR(j,0,m)mark[i][j]=val;
                }

            }

            for(int i=0; i<m; i++)
            {
                state=0;
                for(int j=0; j<n; j++)
                    if(g[j][i]>val)
                    {
                        state=1;
                        break;
                    }
                if(state==0)
                {
                    FOR(j,0,n)mark[j][i]=val;
                }

            }
        }
        //cout<<"__________________________________\n";
        //FOR(i,0,n){FOR(j,0,m)cout<<mark[i][j]<<" ";cout<<endl;}
        state=0;
        FOR(i,0,n)
        {
            FOR(j,0,m)
            if(g[i][j]!=mark[i][j])
            {
                state=1;
                break;
            }
            if(state)break;
        }


    cout<<"Case #"<<cas<<": ";
    if(state==0)cout<<"YES\n";
    else cout<<"NO\n";
    }
    return 0;
}
/*

*/
