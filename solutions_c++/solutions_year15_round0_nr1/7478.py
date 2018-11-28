#include<iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    for(int k=0; k<T; k++)
    {
     int n;
     string s;
     cin>>n>>s;
     int cnt=0, req=0, req1=0;
     cnt= s[0]-'0';
     //cout<<cnt;
     for(int i=1; i<=n; i++)
     {
         if(i<=cnt)
         {
             cnt+= s[i]-'0';
         }
         else{
            req=(i-cnt);
            req1=req1+req;
            cnt+=req+s[i]-'0';
            //cout<<i<<" "<<req<<" "<<cnt<<endl;
         }
     }
     cout<<"Case #"<<k+1<<": "<<req1<<endl;

    }


 return 0;

}
