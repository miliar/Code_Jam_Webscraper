#include <bits/stdc++.h>
using namespace std;
 
#define gc getchar
#define pi(n) printf("%d",n)
#define pin(n) printf("%d\n",n)
#define pis(n) printf("%d ",n)
#define pll(n) printf("%d",n)
#define plls(n) printf("%lld ",n)
#define plln(n) printf("%lld\n",n)
#define ps printf(" ")
#define pn printf("\n")
#define si(n) scanf("%d",&n)
#define sii(n,m) scanf("%d %d",&n,&m)
#define siii(k,n,m) scanf("%d %d %d",&k,&n,&m)
#define rep(i,n) for(i=0;i<n;i++)
#define fu(i,a,n) for(i=a;i<=n;i++)
#define fd(i,n,a) for(i=n;i>=a;i--)
#define ll long long
#define ii pair<int,int>
#define iii pair<ii,int>
#define ff first 
#define ss second
#define mod 1000000007
#define MAXN 100005 

int valid(string s){
     // printf("IN ");
     // cout<<s<<endl;
     int i,j,l;
     string s1;
     while(s.size()!=1){
          l=s.size();    
          s1.clear();
          // cout<<s<<endl;
          for(i=0;i<l;i+=2){
               if((s[i]=='P' && s[i+1]=='R') || (s[i+1]=='P' && s[i]=='R'))
                    s1+='P';
               if((s[i]=='R' && s[i+1]=='S') || (s[i+1]=='R' && s[i]=='S'))
                    s1+='R';
               if((s[i]=='S' && s[i+1]=='P') || (s[i+1]=='S' && s[i]=='P'))
                    s1+='S';
               else if(s[i]==s[i+1])
                    return 0;
          }
          s.clear();
          s=s1;
     }
}

int main()
{
     freopen ("A-small-attempt0.in","r",stdin);
     freopen ("A-small-attempt0.out","w",stdout);
     int i,j,n,t,qw,P,R,S;
     string s;
     si(t);
     fu(qw,1,t){
          printf("Case #%d: ",qw);
          si(n);
          siii(R,P,S);

          s.clear();
          rep(i,P)
               s+='P';
          rep(i,R)
               s+='R';
          rep(i,S)
               s+='S';
          do {
               if(valid(s)){
                    std::cout << s << '\n';
                    goto here;
               }
          } while(std::next_permutation(s.begin(), s.end()));
          printf("IMPOSSIBLE\n");
          here:;
     }

    
    return 0;
}    