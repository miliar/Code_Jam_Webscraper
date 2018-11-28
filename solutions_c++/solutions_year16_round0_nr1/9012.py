#include<bits/stdc++.h>
using namespace std;
set < int > s;
int main()
{
    long long int tmp,ans,i,j,n,m,v=1,t;
    freopen("output.txt", "w", stdout);
    cin>>t;
    while(t--)
    {
        cin>>n;
        if(n==0)cout<<"Case #"<<v++<<": INSOMNIA"<<endl;
        else
        {


        m=1;
        do{
                tmp=n*(m++);
                ans=tmp;
          while(tmp)
          {
              s.insert(tmp%10);
              tmp/=10;
          }


        }while(s.size()<10);

     cout<<"Case #"<<v++<<": "<<ans<<endl;
    s.clear();
    }

    }
}
