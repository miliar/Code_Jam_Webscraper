
#include <string>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <functional>
#include <stack>
#include <set>
#include <queue>
#include <cmath>
#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

typedef long long ll;
const double eps = 1e-6;
const int maxint = -1u>>2;

int n;
int a[1100];
int b[1100];
int c[1100];

int ans ;
int maxpos;

int calc(int lt, int rt)
{
//    printf("lt:%d rt:%d\n", lt, rt);
//    for(int i=lt;i<=rt;i++)
//    {
//        printf("%d ", c[i]);
//    }
//    printf("\n");
//    getchar();
    int ret = 0;
    for(int i=rt;i>=1;i--)
    {
        for(int j=1;j<i;j++)
        {
            if(c[j] > c[j+1])
            {
                swap(c[j], c[j+1]);
                ret++;
            }
        }
    }
    return ret;
}

int doit(int lt, int rt, int ort)
{
    if(lt >= rt)
    {
        return 0;
    }
    if(ort == 1)
    {
        int k,i;
        for(i=lt, k=1; i<=rt;i++, k++)
        {
            c[k] = b[i];
        }
        return calc(1, k-1);
    }
    else
    {
        int k,i;
        for(i=rt, k=1;i>=lt;i--, k++)
        {
            c[k] = b[i];
        }
        return calc(1, k-1);
    }

}

struct NODE
{
    int x, pos;
}node[1100];


bool cmp(NODE a, NODE b)
{
    return a.x < b.x;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            node[i].pos = i;
            node[i].x = a[i];
        }
        sort(node+1, node+n+1, cmp);
//        for(int i=1;i<=n;i++)
//        {
//            printf("%d %d\n",node[i].x, node[i].pos);
//        }
        ans = 0;

        int lt = 1, rt = n;
        int tmp;
        for(int i=1;i<=n;i++)
        {
            if(abs(node[i].pos - lt) <= abs(node[i].pos - rt))//left
            {
                ans += node[i].pos - lt;
                //printf("lt: ans:%d\n", ans);

                for(int j=1;j<=n;j++)
                {
                    if(node[j].pos >= lt && node[j].pos < node[i].pos)
                    {
                        node[j].pos ++;
                    }
                }
                lt++;
            }
            else
            {
                ans += rt - node[i].pos;
                //printf("rt: ans:%d\n", ans);
                for(int j=1;j<=n;j++)
                {
                    if(node[j].pos <= rt && node[j].pos > node[i].pos)
                    {
                        node[j].pos --;
                    }
                }
                rt--;
            }
        }

        //sort(1, n)

        printf("Case #%d: %d\n", cas, ans);
    }

    return 0;
}

