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
      freopen("A-small-attempt2.in","r",stdin);
      freopen("sol.txt","w",stdout);
      l t;

      si(t);
      for(l j=1;j<=t;j++){
            l n;
            si(n);
            cout<<"hell";
            char ch[n+1];
            cin>>ch;
            l sum=ch[0]-48;
            l tot=0;
            for(l i=1;i<=n;i++){
                    if(i>sum && (ch[i]-48)!=0){
                        tot+=i-sum;
                        sum=i;
                    }
                    sum+=ch[i]-48;


            }
            cout<<"Case #"<<j<<": "<<tot<<"\n";



      }


      return 0;
  }






