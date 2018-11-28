#include<bits/stdc++.h>
 using namespace std;

 int usd[100],k,i,n,j,mx,t,tt;

 inline void add(int x)
 {
     if(!usd[x])
     {
         usd[x] = 1;
         ++k;
     }
 }

  int main()
  {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);

     cin>>tt;
      for(t=1;t<=tt;++t)
      {
          cin>>n;
          cout<<"Case #"<<t<<": ";
          if(n==0)cout<<"INSOMNIA"; else
          {
              memset(usd,0,sizeof(usd));
              k = 0;
              for(i=1;i>0;++i)
              {
                  j = i * n;
                   while(j)
                   {
                       add(j % 10);
                       if(k==10)break;
                      j/=10;
                   }
                   if(k==10)
                   {
                       cout<<n * i;
                       break;
                   }
              }
          }
          cout<<endl;
      }

    return 0;
  }
