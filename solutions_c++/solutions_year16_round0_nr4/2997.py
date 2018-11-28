    #include <bits/stdc++.h>
    using namespace std;
     
    int main() {
    unsigned long long int t,i,k,c,s,j,a,b,d,e;
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        // freopen("output.txt","w",stdout);
      #endif
    cin>>t;
    for(i=1;i<=t;i++)
    {
      cin>>k>>c>>s;
       cout<<"Case #"<<i<<":";
    if(k<=s){ for(j=1;j<=k;j++)
      {
        cout<<" "<<j;
      }}
      else
      {
         a=k-c+1;
         if(k==2) a=2;
         if(a>s) cout<<" "<<"IMPOSSIBLE";
         else{ 
          a=k-c+1;j=pow(k,c);e=j/2+j%2;if(a%2!=0) {cout<<" "<<e;a--;}
          for(b=1;b<=a/2;b++)
          { 
           cout<<" "<<e-b<<" "<<e+b;
          }
         }
      }
      cout<<"\n";
    }
      return 0;
    }