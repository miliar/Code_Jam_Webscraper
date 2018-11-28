#include<iostream>
using namespace std;
main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long n,m;
        int cnt[10]={0},l=1,ctr=0;
        cin>>n;
        m=n;
        if(n>0)
        while(true)
        {
          long x=n;
          while(x>0)
          {
              if(cnt[x%10]==0)
              {
                  cnt[x%10]=1;
                  ctr++;
              }
              x=x/10;
          }
          if(ctr==10) break;
          l++;
          n=l*m;
          cout<<n<<" ";
        }
        if(ctr==0)
        cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        else
        cout<<"Case #"<<i<<": "<<n<<endl;
     }
return 0;
}
