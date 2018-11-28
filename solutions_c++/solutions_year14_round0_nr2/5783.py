#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#define EPS 1e-9
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;

struct node
{
       double t,pers,current;
};
bool operator <(const node &a,const node &b)
{
     return a.t>b.t;
}


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    
    int tc,tc_c;
    double c,f,x;
    cin>>tc;
    for(tc_c=1;tc_c<=tc;tc_c++)
    {
             cin>>c>>f>>x;
             double ans;
             
             node cur,tmp;
             priority_queue <node> q;
             cur.current=0;
             cur.t=0;
             cur.pers=2;
             q.push(cur);
             while(!q.empty())
             {
                         cur = q.top();
                         q.pop();
                         if((x-cur.current)<=EPS)
                         {
                                                 ans = cur.t;
                                                 break;
                         }else if(cur.current>x) continue;
                         
                         // Suddenly get all;
                         tmp.t = cur.t + (x-cur.current)/cur.pers;
                         tmp.current = cur.current + (x-cur.current);
                         tmp.pers = cur.pers;
                         q.push(tmp);     
                         //Buy a new unit;
                         tmp.t = cur.t + (c-cur.current)/cur.pers;
                         tmp.current = 0;
                         tmp.pers = cur.pers + f;
                         q.push(tmp);
                         //Go anther second;
                         /*
                         tmp.t = cur.t+1;
                         tmp.current = cur.current + cur.pers;
                         tmp.pers = cur.pers;
                         q.push(tmp);
                         */
             }
             printf("Case #%d: %.7lf\n",tc_c,ans);
    }
    
    return 0;   
}
