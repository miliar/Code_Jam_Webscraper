
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

     freopen("B-large.in","r",stdin);
      freopen("output_large_b.txt","w",stdout);

      l t;
      cin>>t;
      for(int i=1;i<=t;i++){
        string str;
        cin>>str;
        l len=str.length();
        if(len==1){
                if(str[0]=='+')
                     cout<<"Case #"<<i<<": "<<"0"<<"\n";
                else
                     cout<<"Case #"<<i<<": "<<"1"<<"\n";
        }
        else{
                l cnt=0;
                for(int j=0;j<len-1;j++){
                    if(str[j]!=str[j+1])
                        cnt++;
                }

                if(str[0]=='+'){
                    if(cnt%2==1)
                        cnt++;
                    cout<<"Case #"<<i<<": "<<cnt<<"\n";

                }
                else{
                    if(cnt==0)
                       cout<<"Case #"<<i<<": "<<"1"<<"\n";
                   else{
                    cnt--;
                    if(cnt%2==1)
                        cnt++;
                    cout<<"Case #"<<i<<": "<<cnt+1<<"\n";
                   }

                }

        }


      }



      return 0;
  }







