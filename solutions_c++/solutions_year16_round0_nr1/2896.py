
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

      freopen("A-large.in","r",stdin);
      freopen("output_large_a.txt","w",stdout);

      l t;
      cin>>t;
      for(int j=1;j<=t;j++){
        ll x;
        cin>>x;
        ll temp=x;
        bool ck[10];
        for(int i=0;i<10;i++)
            ck[i]=false;
        if(x==0){
            cout<<"Case #"<<j<<": INSOMNIA\n";
        }

        else{
                int cnt=0;
                while(cnt!=10){
                    cnt=0;
                    ll v=x;
                    while(v!=0){
                        ck[v%10]=true;
                        v/=10;
                    }
                    for(int i=0;i<10;i++){
                        if(ck[i])
                            cnt++;
                    }
                    if(cnt==10)
                        cout<<"Case #"<<j<<": "<<x<<"\n";

                    x+=temp;

                }

        }
      }


      return 0;
  }






