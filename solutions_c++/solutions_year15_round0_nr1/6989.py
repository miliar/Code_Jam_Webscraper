#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
          int t,max,cnt,ans,j;
          string s;
          cin>>t;
          j=0;
          freopen("output.txt", "w", stdout);
          while(j<t)
          {
                    cnt=0;ans=0;
                    cin>>max>>s;
                    for(int i=0;i<max+1;i++)
                    {
                              if(cnt>=i)
                              {
                                        cnt+=(int)(s[i]-'0');
                              }
                              else
                              {
                                        ans+=i-cnt;
                                        cnt+=i-cnt+(int)(s[i]-'0');

                              }
                    }

                    printf("Case #%d: %d\n",j+1,ans);
                    j++;

          }

          return 0;
}
