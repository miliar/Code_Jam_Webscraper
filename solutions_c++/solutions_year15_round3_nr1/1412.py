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
      l t;
     freopen("A-large.in","r",stdin);
     freopen("sol.txt","w",stdout);
      si(t);
      for(l v=1;v<=t;v++){
            l r,c,w;
            si(r),si(c),si(w);
            l ans;
            l cnt=0;

                ans=(c/w)+w-1;
                if((c%w)!=0)
                    ans++;

                ans+=(r-1)*(c/w);







            cout<<"Case #"<<v<<": "<<ans<<"\n";
      }


      return 0;
  }







