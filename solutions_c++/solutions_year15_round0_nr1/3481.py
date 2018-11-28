#include <iostream>
#include<algorithm>
using namespace std;
int main()
{
  int t;
   
   cin>>t;
   for(int t1=1;t1<=t;t1++)
  {
   char ch[20000];
    int n;
    cin>>n>>ch;
    int cur=ch[0]-'0',ans=0;
    for(int i=1;i<=n;i++)
    {
      if(cur>=i)
      {
        cur+=(ch[i]-'0');
      }
      else
      {
        ans=ans+(i-cur);
        cur=i+ch[i]-'0'; 
       }
    }
 
   cout<<"Case #"<<t1<<": "<<ans<<endl;
   }
}
