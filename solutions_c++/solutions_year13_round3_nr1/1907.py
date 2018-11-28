#include<iostream>
#include<cstring>
using namespace std;

int isConsonant(char c)
{
    if(c!='a' && c!='e' && c!='i' && c!='o' && c!='u')
                                              return 1;
    return 0;
}
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.out","w", stdout);   
    int t,x=1;
    scanf("%d",&t);
    
    while(t--)
    {
              char name[110];
              int n;
              int ans=0,cnt=0, lasti=0;
              
              scanf("%s %d",&name,&n);
              
              int len = strlen(name);
              for(int i=0;i<len;i++)
              {       //cout<<i<<" "<<ans<<name[i]<<endl;
                      cnt=0;
                      if(isConsonant(name[i]))
                      {
                                             while(i<len && cnt<n && isConsonant(name[i]))
                                             {
                                                                       cnt++;
                                                                       i++;
                                                                       
                                             }
                                             if(cnt==n)
                                             {          
                                                        ans += (i-lasti-n+1)*(len-i+1);
                                                        lasti = i-n+1;
                                             
                                                        while(i<len && isConsonant(name[i]))
                                                        {
                                                                        i++;
                                                                        ans += (i-lasti-n+1)*(len-i+1);
                                                                        lasti = i-n+1;
                                                        }
                                             }                 
                      }
                                        
              }
              printf("Case #%d: %d\n",x++,ans);
    }
}
