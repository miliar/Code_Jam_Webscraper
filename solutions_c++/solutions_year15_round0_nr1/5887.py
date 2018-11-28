#include <bits/stdc++.h>
#define f(x) for(int j=0;j<x;++j)


using namespace std;

int main()
{
 freopen("A-large.in","r",stdin);
 freopen("out.out","w",stdout);
    int t;
    cin>>t;


    for(int i=1;i<=t;++i)

    {

       cout<<"Case #"<<i<<": ";

            int ans=0;
           int smax;
           cin>>smax;
           string s;
           cin>>s;
           int sum=s[0]-'0';
           for(int m=1;m<smax+1;++m)
           {

               if(sum<m){ans+=m-sum;sum=m;}
               sum+=s[m]-'0';

           }






         cout<<ans<<endl;
    }



    return 0;
}
