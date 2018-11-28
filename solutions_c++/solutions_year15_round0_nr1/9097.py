#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;

int main()
{
   freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
 int tc,ans,k,tmp;
 char s[1005];
 cin>>tc;
         for(int caseCounter=1;caseCounter<=tc;caseCounter++)
         {
                 ans =0;
                 tmp=0;
                 cin>>k;
                 
                cin>>s;
                tmp+=s[0]-'0';                
                 for(int i=1;i<strlen(s);i++)
                 {
                         if(tmp>=i)
                         {
                                          tmp+=s[i]-'0';
                         }else
                         {
                              ans+=i-tmp;
                              tmp+=i-tmp;
                              tmp+=s[i]-'0';
                         }
                 }       
                 cout<<"Case #"<<caseCounter<<": "<<ans<<endl;
         }
    
    return 0;   
}
