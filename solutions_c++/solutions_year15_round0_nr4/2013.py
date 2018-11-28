
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

      l t;
     freopen("D-small-attempt0.in","r",stdin);
     freopen("sol.txt","w",stdout);
      si(t);
      for(l x=1;x<=t;x++){
            l n,r,c;
            si(n);si(r);si(c);
            if(r*c%n!=0)
                cout<<"Case #"<<x<<": "<<"RICHARD\n";
            else{
                    if(r+c>=2*n-1)
                       cout<<"Case #"<<x<<": "<<"GABRIEL\n";
                    else
                        cout<<"Case #"<<x<<": "<<"RICHARD\n";



            }



        }






      return 0;
  }






