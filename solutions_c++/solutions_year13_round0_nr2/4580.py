#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <ctime>
#include <cstring>
#define rep(i,n) for(int i=0;i<n;i++)
#define A frist
#define B second
#define mp make_pair
#define LL long long
#define pb push_back
using namespace std;

int a[105][105],v[205];
int n,m;
struct node
{
    int num,i,j;
    node(int numm,int ii,int jj)
    {
        num = numm;
        i = ii;
        j = jj;
    }
};
vector <node> p;

bool cmp(node a,node b)
{
    return a.num > b.num;
}
vector <int> q;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("large_out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    rep(cas,T)
    {
        p.clear();
        q.clear();
        scanf("%d%d",&n,&m);
        rep(i,n)rep(j,m)scanf("%d",&a[i][j]);
        rep(i,n)rep(j,m)p.pb(node(a[i][j],i,j));
        sort(p.begin(),p.end(),cmp);
        memset(v,0,sizeof(v));

        int pre = -1;
        int flag=0;

        for(int i=0; i<p.size(); i++)
        {
            if(pre == p[i].num)
            {
                if(v[p[i].i] && v[p[i].j + n])
                {
                    flag=1;
                    break;
                }
                q.pb(p[i].i);
                q.pb(p[i].j + n);
            }
            else
            {
                rep(j,q.size())
                v[q[j]] = 1;
                q.clear();
                pre = p[i].num;
                i--;
            }
        }
        printf("Case #%d: ",cas+1);
        if(flag == 0)
        {
            puts("YES");
        }
        else puts("NO");
    }
}









