#include<stdio.h>
#include<iostream>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>

#define MOD 1000000007
#define INF 2000000000
double eps=1.0/10000000.0;

using namespace std;

int main()
{
    int t;
    
    double c,f,x;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&t);
    int save=t;
    
    while(t--)
    {
              scanf("%lf %lf %lf",&c,&f,&x);
              
              double cur=2.0;
              double ans=INF,tim=0,prev_ans;
              
              do
              {
                     prev_ans=ans;
                     ans=tim+(x/cur);
                     
                     tim+=c/cur;
                     cur+=f;
                     //printf("%lf\n",ans);
              }while((prev_ans-ans)>eps);
              
              printf("Case #%d: %0.7lf\n",save-t,prev_ans);
    }
    
    return 0;
}
