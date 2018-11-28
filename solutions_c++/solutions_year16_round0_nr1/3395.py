#include<bits/stdc++.h>
using namespace std;

int main()
 {
   freopen("A-large.in","r",stdin);
     freopen("output.txt","w",stdout);

   int t;
   cin>>t;
   //cout<<t<<endl;

   int p;

   for(p=1;p<=t;p++)
    {
     //if(p>t)
        // break;
     int n;
     cin>>n;
     //cout<<n<<"  "<<p<<"  "<<t;
     int arr[10]={0};
     int i=1,ctr=0,d;
     long long copy;
     if(n==0)
       printf("Case #%d: INSOMNIA\n",p);
     else
       {
           while(ctr<10)
            {
                copy=n*1LL*i;
                 while(copy>0)
                  {
                      d=copy%10;
                      copy/=10;
                      if(arr[d]==0)
                       {
                         ctr++;
                       }
                       //cout<<arr[d];
                       arr[d]++;
                       if(ctr==10)
                         break;
                  }
                  if(ctr==10)
                     break;


                  i=i+1;

            }
            printf("Case #%d: %lld\n",p,n*1LL*i);

       }

    }


 }
