/*
Try Try & Try until you solve the problem...
Nothing is impossible for the problem solvers... :)
*/
/*

*/
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <numeric>

#include <cmath>
#include <cstdio>

#define IP(n) for(i=0;i<n;i++)
#define JP(n) for(j=0;j<n;j++)
#define KP(n) for(k=0;k<n;k++)

#define vi vector<int>
#define vi2 vector<vector<int>>
#define vs vector<string>

#define pb push_back
#define TC int t,check=1;cin>>t;while(check<=t)
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)
#define ms(x,a) memset(x,a,sizeof(x))
#define read(a) freopen(a,"r",stdin)
#define write(a) freopen(a,"w",stdout)

using namespace std;

int brd[105][105];
int row[105];
int col[105];
int n,m;

void setIt()
{
    ms(row,0);
    ms(col,0);

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        row[i]=max(row[i],brd[i][j]);
    }

    for(int j=0;j<m;j++)
    {
        for(int i=0;i<n;i++)
        col[j]=max(col[j],brd[i][j]);
    }
}

void input()
{
    scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        scanf("%d",&brd[i][j]);
    }
}

int solve()
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(brd[i][j]!=row[i] && brd[i][j]!=col[j])
            return 0;
        }
    }

    return 1;
}

int main()
{
    //read("Bs.in");
    //write("Bs.txt");
    int t,check=1;
    scanf("%d",&t);
    while(t--)
    {
        input();
        setIt();

        if(solve())
        printf("Case #%d: YES\n",check++);
        else
        printf("Case #%d: NO\n",check++);
    }
    return 0;
}
