  #include<iostream>
  #include<stdio.h>
  #include<algorithm>
  #include<vector>
  #include<string>
  #include<map>
  #include<queue>
  #include<cmath>
  #include<stack>
  #include<sstream>
  #include<list>


  using namespace std;


  typedef long long ll;
  typedef long l;

  #define floop(i,n) for(ll i=0;i<n;i++)
  #define floopk(i,n,k) for(ll i=0;i<n;i+=k)
  #define si(n) scanf("%ld",&n)
  #define po(n) printf("%ld",n)


  int main()
  {
      //std::ios_base::sync_with_stdio(false);
      freopen("A-large.in","r",stdin);
      freopen("sol.txt","w",stdout);
      l t;
      si(t);
      for(l k=1;k<=t;k++){
            l n;
            si(n);
            l arr[n];
            floop(i,n)
               si(arr[i]);
            l sum1=0;
            for(l i=0;i<n-1;i++){
                if(arr[i]>arr[i+1])
                    sum1+=arr[i]-arr[i+1];
            }
            l maxx=0,sum2=0;
             for(l i=0;i<n-1;i++){
                if(arr[i]-arr[i+1]>maxx)
                    maxx=arr[i]-arr[i+1];
            }
            for(l i=0;i<n-1;i++){
                if(arr[i]<maxx)
                    sum2+=arr[i];
                else
                    sum2+=maxx;
            }


            cout<<"Case #"<<k<<": "<<sum1<<" "<<sum2<<"\n";




      }


      return 0;
  }







