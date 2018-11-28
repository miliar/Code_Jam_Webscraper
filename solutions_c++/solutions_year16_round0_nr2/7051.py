#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
#define ld done 
#define user hardik
#define hmm ios_base::sync_with_stdio(0);
  ll t,count1,i,turn;
bool done;
char s[300];
int main()
{
  
       turn=1;
    scanf("%lld",&t);
 
    while(t--)
{
        
        char c;
        scanf("%s",s);
        int l=strlen(s);;
        done=false;
        
        count1=0;
        while(done==false)
{
            c=s[0];
            i=0;
            if(c=='+')
{
            
                while(i<l && s[i]!='-')
                    i++;
                if(i==l)
{
                    printf("Case #%lld: %lld\n",turn++,count1);
                    done=true;
                }
else
{
                    count1++;
                
                    memset(s,'-',sizeof(char)*i);
                }
            }
else
{
               
                
                count1++;
                while(i<l && s[i]!='+')
                    i++;
                if(i==l)
{
                    printf("Case #%lld: %lld\n",turn++,count1);
                    done=true;
                }
else
{
                    memset(s,'+',sizeof(char)*i);
                }
            }
        }
    }
    return 0;
}