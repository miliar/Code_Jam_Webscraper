#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<map>
#include<string>
#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<cmath>
#include<ctype.h>
#include<deque>
#include<list>
#include<set>
#define inf (1<<30)
#define pi acos(-1.0)
#define LL long long int
#define LU unsigned long long int
#define eps 1e-9
#define mod 100000007
#define mem(a) memset(a,0,sizeof(a))
#define neg(a) memset(a,-1,sizeof(a))
#define pub(a) push_back(a)
#define pob(a) pop_back(a)
#define puf(a) push_front(a)
#define pof(a) pop_front(a)
#define mkp(a,b) make_pair(a,b)

using namespace std;
int n,m,i,j,k,l,aa[1000009],bb[1000009],pp[1000009],ans,cn,t,x,y,z,mx,mn,s;
char c[1000009],d[1000009],ch;
struct point
{
    int al,num;
}p[30];
bool operator<(point a,point b)
{
    return a.num<b.num;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        s=0;
        priority_queue<point>pq;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&p[i].num);
            s+=p[i].num;
            p[i].al=i;
            pq.push(p[i]);
        }
        printf("Case #%d:",l);
        while(pq.empty()==0)
        {
            s--;
            point u=pq.top();
            pq.pop();
            if(u.num>1)
            {
                u.num--;
                pq.push(u);
            }
            if(pq.top().num>s/2)
            {
                s--;
                point v=pq.top();
                pq.pop();
                if(v.num>1)
                {
                    v.num--;
                    pq.push(v);
                }
                printf(" %c%c",u.al+'A',v.al+'A');
            }
            else
            {
                printf(" %c",u.al+'A');
            }
        }
        printf("\n");
    }
    return 0;
}
