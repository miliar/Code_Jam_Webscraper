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


  int main()
  {
      //std::ios_base::sync_with_stdio(false);
      freopen("D-small-attempt0.in","r",stdin);
      freopen("output_small_d.txt","w",stdout);

      l t;
      cin>>t;
      for(int i=1;i<=t;i++){
        ll k,c,s;
        cin>>k>>c>>s;
        ll val=pow(k,c-1);
        ll temp=1;
        cout<<"Case #"<<i<<": ";
        for(l j=0;j<s;j++){
            cout<<temp<<" ";
            temp+=val;
        }
        cout<<"\n";


      }

      return 0;
  }







