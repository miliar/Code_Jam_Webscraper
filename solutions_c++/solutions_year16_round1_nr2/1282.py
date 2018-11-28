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
     freopen("B-large.in","r",stdin);
     freopen("output_small_b.txt","w",stdout);
//
      l t;
      cin>>t;
      for(l f=1;f<=t;f++){
            l cnt[2600];
            for(int i=1;i<2600;i++)
                cnt[i]=0;
            l n;
            cin>>n;
            for(l j=1;j<2*n;j++){
                for(l k=1;k<=n;k++){
                    l val;
                    cin>>val;
                    cnt[val]++;
                }
            }

        cout<<"Case #"<<f<<": ";
        for(int i=1;i<2600;i++){
            if(cnt[i]%2!=0)
                cout<<i<<" ";
        }

        cout<<"\n";
      }


      return 0;
  }









