#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
int main()
{
  freopen("jamQaque.txt","r",stdin);
  freopen("jamQa.txt","w",stdout);
  int t,count;
  cin>>t;
  for(count=1;count<=t;count++) {
     string s;
     long long i,j,n,m,ans=0,maxm,temp=0,num;
     cin>>maxm>>s;
     for(i=0;i<=maxm;i++) {
       num = s[i]-'0';
       if(temp<i) {
          ans+=(i-temp);
          temp = i + num;
       }
       else temp+=num;
     }
     cout<<"Case #"<<count<<": ";
     cout<<ans<<"\n";
  }
//  system("pause");
  return 0;
}
