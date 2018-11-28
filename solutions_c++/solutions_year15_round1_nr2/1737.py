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
  #define si(n) scanf("%lld",&n)
  #define po(n) printf("%ld",n)
  ll gcd(ll a,ll b){
       while (b!=0){
      ll t = b;
       b = a % b;
       a = t;
       }
    return a;



  }


  int main()
  {
      //std::ios_base::sync_with_stdio(false);
      freopen("B-small-attempt4.in","r",stdin);
      freopen("sol.txt","w",stdout);
      ll t;
      si(t);
      for(l k=1;k<=t;k++){
            ll n,m;
            si(n);si(m);
            ll arr[n];
            ll ava[n];
            floop(i,n){
               si(arr[i]);
               ava[i]=0;
            }
            ll res=arr[0];
            for(l h=1;h<n;h++){
                res=gcd(res,arr[h]);
            }
            ll mult=1;
            floop(i,n){

              mult*=arr[i];
            }
            ll lcm=mult/res;
            ll tot=0;
            floop(i,n){
               tot+=(lcm/arr[i]);
            }
            m=m%tot;
            if(m==0)
                m=tot;

            ll ind=1;
            ll j=0;
            while(j!=m){

                for(l p=0;p<n;p++){
                    if(ava[p]==0){
                        ava[p]=arr[p];
                        j++;
                        if(j==m){
                          ind=p+1;
                          break;
                        }
                       // cout<<ind<<" ";
                    }


                    if(ava[p]>0)
                        ava[p]--;


                }


            }




            cout<<"Case #"<<k<<": "<<ind<<"\n";




      }


      return 0;
  }







