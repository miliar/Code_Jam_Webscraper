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
  typedef pair<int,char> PII;


  int main()
  {
      //std::ios_base::sync_with_stdio(false);
      freopen("A-large.in","r",stdin);
      freopen("output_large_a.txt","w",stdout);

      l t;
      cin>>t;
      for(int i=1;i<=t;i++){
          l n;
          cin>>n;
          priority_queue<PII> Q;
          for(int j=1;j<=n;j++){
            l val;
            cin>>val;
            Q.push(make_pair(val,64+j));
          }

          cout<<"Case #"<<i<<": ";
          while(!Q.empty()){
            PII x=Q.top();
            PII y;
            Q.pop();
            l cnt=0;
            if(!Q.empty()){
                y=Q.top();
                 Q.pop();
                 if(y.first==x.first){
                    if(x.first==1 && Q.size()==1){
                        cout<<x.second<<" ";
                        x.first--;
                        Q.push(y);
                        cnt++;
                    }
                    else{
                    y.first--;
                    x.first--;
                    cnt++;
                    cout<<x.second<<y.second<<" ";
                    if(y.first!=0){
                        Q.push(y);
                        Q.push(x);
                    }
                    }

                 }
                 else
                    Q.push(y);
            }
            if(cnt==0){
                cout<<x.second<<" ";
                x.first--;
                if(x.first!=0)
                Q.push(x);
                //Q.push(y);
            }
          }





        cout<<"\n";

      }

      return 0;
  }








