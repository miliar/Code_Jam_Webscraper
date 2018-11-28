#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <cstdio>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <cassert>
#include <sstream>
#include<limits>
using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef stringstream SS;

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define ABS(a) MAX(a,-(a))

#define ss(a) scanf("%d",&a)
#define SZ(a) ((int)a.size())
#define pb(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define MOD 1000000007
#define INF (1<<31)

#define EPS 1e-12
void solve(int );
int matrix1[5][5];
int matrix2[5][5];
int hash[20];
int main()
{
    int n;
    ss(n);
    REP(i,n)
    {
        solve(i+1);
    }
    return 0;
}
void solve(int k)
{
    //static int case=1;
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    REP(i,17)
    {
        hash[i]=0;
    }
    int n,m;
    ss(n);
    REP(i,4)
    {
        REP(j,4)
        {
            ss(matrix1[i][j]);
            if(i==n-1)
            {
                hash[matrix1[i][j]]++;
            }
        }
    }
    ss(m);
    REP(i,4)
    {
        REP(j,4)
        {
            ss(matrix2[i][j]);
            if(i==m-1)
            {
                hash[matrix2[i][j]]++;
            }
        }
    }

    int count=0;
    int ans=0;
    FOR(i,1,16)
    {
        if(hash[i]==2)
        {
            ans=i;
            count++;
        }
    }
    if(count==0)
    {
        printf("Case #%d: Volunteer cheated!\n",k);
    }
    else if(count==1)
    {
        printf("Case #%d: %d\n",k,ans);
    }
    else
    {
        printf("Case #%d: Bad magician!\n",k);
    }
}
