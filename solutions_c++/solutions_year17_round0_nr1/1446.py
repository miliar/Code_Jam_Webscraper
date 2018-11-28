#include <bits/stdc++.h>
#define endl '\n';
using namespace std;
typedef long long int LL;

int main()
{
  ios_base::sync_with_stdio(false);cin.tie(0);

  //freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

  int tc;cin>>tc;for(int t=1;t<=tc;t++)
  {    
     cout<<"Case #"<<t<<": ";
     
     string s;
     int k;    
     cin>>s>>k;

     int res=0;

     for(int i=0;i+k-1<s.size();i++)
     {
     	if(s[i]=='-')
     	{
     	   res++;
          for(int j=i;j<=i+k-1;j++)
            s[j] = (s[j]=='-') ? '+' : '-';     
     	}
     }
     bool fnf=true;
     for(int i=0;i<s.size();i++)
     {
     	if(s[i]=='-'){
     		fnf=false;
     		cout<<"IMPOSSIBLE"<<endl;
     		break;
     	}
     }
     
     if(fnf)
     cout<<res<<endl;
  }
          
  return 0;
}