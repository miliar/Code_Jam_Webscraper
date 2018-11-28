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

using namespace std;

int main()
{
    int t,i,j,a,b;
    
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&t);
    int save=t;
    
    while(t--)
    {
              scanf("%d",&a);
              
              int x,ans1[10],ans2[10];
              
              for(i=1;i<=4;i++)
              {
                              for(j=1;j<=4;j++)
                              {
                                              scanf("%d",&x);
                                              if(i==a)
                                              {
                                                      ans1[j]=x;
                                              }
                              }
              }
              
              scanf("%d",&b);
              
              for(i=1;i<=4;i++)
              {
                               for(j=1;j<=4;j++)
                               {
                                                scanf("%d",&x);
                                                if(i==b)
                                                {
                                                        ans2[j]=x;
                                                }
                               }
              }
              
              int ans,cnt=0;
              
              for(i=1;i<=4;i++)
              {
                               for(j=1;j<=4;j++)
                               {
                                                if(ans1[i]==ans2[j])
                                                {
                                                                    ans=ans1[i];
                                                                    cnt++;
                                                }
                               }
              }
              printf("Case #%d: ",save-t);
              
              if(cnt==0)
              {
                        printf("Volunteer cheated!\n");
              }
              else if(cnt>1)
              {    
                   printf("Bad magician!\n");
              }
              else
              {
                  printf("%d\n",ans);
              }
    }
    
    return 0;
}
