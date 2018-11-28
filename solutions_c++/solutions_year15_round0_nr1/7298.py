#include<iostream>
using namespace std;

int main()
{
  int t,smax;
cin>>t;
int ans[t];
for(int i=0;i<t;i++)
 {
  cin>>smax;
  char c[smax+1];
  cin>>c;
  int st=0,fr=0;
  for(int j=0;j<smax+1;j++)
   {
     if(st>=j)
         st+=c[j]-'0';
     else
      {
        int less=j-st;
        st+=less+c[j]-'0';
        fr+=less;
      }
    }
ans[i]=fr;
//cout<<fr<<"\n";

 }
for(int j=0;j<t;j++)
 {
  cout<<"Case #"<<j+1<<": "<<ans[j]<<"\n";
 }

}






