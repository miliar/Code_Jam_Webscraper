#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

int ans[1000006];
int vis[1000006];

int rev(int a)
{
    int ret=0;
    
    while(a)
    {
            ret*=10;
            ret+=a%10;
            a/=10;
    }
    return ret;
}

queue<int> q,val;
void bfs(int st)
{
     
     q.push(st);
     val.push(1);
     vis[1]=1;
     
     while(!q.empty())
     {
                      int x=q.front();
                      int v=val.front();
                      q.pop();
                      val.pop();
                      ans[x]=v;
                      //cout<<x<<endl;
                      if(!vis[x+1] && x+1<=1000000)
                      {
                                   q.push(x+1);
                                   val.push(v+1);
                                   vis[x+1]=1;
                      }
                      if(rev(x)<=1000000 && !vis[rev(x)])
                      {
                                      q.push(rev(x));
                                      val.push(v+1);
                                      vis[rev(x)]=1;
                      }
     }
     
     return;
}
                      
                      

int main()
{
    bfs(1);
    freopen("A_in_small.txt","r",stdin);
    freopen("A_out_small_brute.txt","w",stdout);
    int t,n;
    
    scanf("%d",&t);
    int sv=t;
    while(t--)
    {
              scanf("%d",&n);
              
              printf("Case #%d: %d\n",sv-t,ans[n]);
    }
    //system("pause");
    return 0;
}
