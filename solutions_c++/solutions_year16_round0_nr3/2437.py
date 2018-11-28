  #include<iostream>
  #include<cstdio>
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

  ll prime(ll v){
       for(ll i=2;i*i<=v;i++){
        if(v%i==0)
            return i;
       }

       return 0;
  }


  int main()
  {
      //std::ios_base::sync_with_stdio(false);
      freopen("C-small-attempt3.in","r",stdin);
      freopen("output_small_c.txt","w",stdout);
      ll t;
      cin>>t;
     // l ind=0;
      //ll sss[55];

       ll n,k;
       cin>>n>>k;
       cout<<"Case #"<<"1"<<":\n";
       l cnt=0;
       map<ll,bool>mp;
       while(cnt!=50){
            ll str[16];
            str[0]=1;str[15]=1;
            ll val[11];
            ll temp[11];
            for(int i=2;i<=10;i++){
               val[i]=1;
               temp[i]=1;
            }
            for(ll i=2;i<=15;i++){
                ll x=rand()%2;
                str[i-1]=x;
                for(ll j=2;j<=10;j++){
                   temp[j]*=j;
                   val[j]+=temp[j]*x;
                }
            }

            for(ll j=2;j<=10;j++){
                temp[j]*=j;
                val[j]+=temp[j];
            }

            bool flag=true;
            ll ans[11];
            for(ll j=2;j<=10;j++){
                ll z=prime(val[j]);
                if(z==0){
                    flag=false;
                    break;
                }
                ans[j]=z;
            }
            if(flag && mp[val[2]]==false){
                    cnt++;
                   // sss[ind]=val[2];
                    //ind++;
                    mp[val[2]]=true;
                    for(ll j=15;j>=0;j--)
                        cout<<str[j];
                    cout<<" ";
                  //  cout<<" "<<val[2]<<" ";
                    for(ll j=2;j<=10;j++)
                         cout<<ans[j]<<" ";
                    cout<<"\n";

            }


       }
     /*  sort(sss,sss+k);
       for(int i=0;i<k;i++)
        cout<<sss[i]<<"\n";*/


      return 0;
  }







