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
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define pb push_back
#define clean(a,b) memset(a,b,sizeof(a))
#define oo 1<<20
#define dd double
#define ll long long
#define ull unsigned long long
#define ff float
#define EPS 10E-10
#define fr first
#define sc second
#define MAXX 100000
#define PRIME_N 1000000
#define INFI 1<<30
#define SZ(a) ((int)a.size())
#define all(a) a.begin(),a.end()
#define MODD 1000000007
#define bpcnt(a) __builtin_popcount(a)
#define REP(i,n) for (i=0;i<n;i++)
#define FOR(i,p,k) for (i=p; i<k;i++)

//int rx[] = {0,-1,0,1,1,-1,-1,0,1}; //four direction x
//int ry[] = {0,1,1,1,0,0,-1,-1,-1};   //four direction y
//int rep[] = {1,1,4,4,2,1,1,4,4,2}; //repet cycle for mod
//void ullpr(){printf("range unsigned long long : %llu\n",-1U);} //for ull
//void ulpr(){printf("range unsigned long : %lu\n",-1U);} //for ull
//void upr(){printf("range unsigned : %u\n",-1U);} //for ull


int reqGrid[102][102];
int grid[102][102];
int reqrow[102];
int reqcol[102];
int prerow[102];
int precol[102];

struct node
{
    int val,r,c;
    node(int i,int j,int k)
    {
        val = i,r = j,c = k;
    }
};

vector<node>v;

bool cmp(node a,node b)
{
    return a.val>b.val;
}

int main()
{
    freopen("bl.in","r+",stdin);
    freopen("out.out","w+",stdout);
    int row,col;

    int tcase,cas=1;

    scanf(" %d",&tcase);
    while(tcase--)
    {
        scanf(" %d %d",&row,&col);
        clean(reqrow , 0);
        clean(reqcol , 0);
        int mx = 0;
        int pos = 1;
        v.clear();
        ///taking input ..........
        for(int i = 1; i<=row ; i++)
        {
            for(int j = 1; j<=col ; j++)
            {
                scanf(" %d",&reqGrid[i][j]);
                reqrow[i] = max(reqrow[i] , reqGrid[i][j]);
                reqcol[j] = max(reqcol[j] , reqGrid[i][j]);
                mx = max(mx , max(reqrow[i] , reqcol[j]));
                v.pb(node(reqGrid[i][j] , i,j));
            }
        }
        ///making the grid
        for(int i = 1 ; i<=row ; i++ )
        {
            for(int  j = 1 ; j<=col ; j++)
            {
                grid[i][j] = mx+1;
//                prerow[i] = mx+1;
//                precol[j] = mx+1;
            }
        }

        ///sort the value

        sort(all(v) , cmp);
//        cout<< " v0 "<<" - "<<v[0].val<<endl;

        for(int i = 0 ; i<SZ(v) && pos; i++)
        {
            if(grid[v[i].r][v[i].c]==v[i].val) continue;
            int rchk = 1,cchk = 1;
            for(int j = 1 ; j<=col  ; j++)
            {
                if(grid[v[i].r][j]>=v[i].val && v[i].val>=reqGrid[v[i].r][j]) continue;
                else
                {
                    rchk = -1;break;
                }
            }

            if(rchk!=-1)
            {
                for(int j = 1 ; j<=col ; j++)
                    grid[v[i].r][j] = v[i].val;
            }
            for(int j = 1 ; j<=row ; j++)
            {
                if(grid[j][v[i].c]>=v[i].val && v[i].val>=reqGrid[j][v[i].c]) continue;
                else
                {
                    cchk = -1;break;
                }
            }

            if(cchk!=-1)
            {
                for(int j = 1  ; j<=row ; j++)
                    grid[j][v[i].c] = v[i].val;
            }

            if(cchk==-1 && rchk==-1)
                pos = 0;
        }

        if(pos==1)
        {
            for(int i = 1; i<=row && pos; i++)
                for(int j = 1 ; j<=col&& pos ; j++)
                    if(grid[i][j]!=reqGrid[i][j]) {pos = 0;}
        }

        printf("Case #%d: ",cas++);
        if(pos) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
