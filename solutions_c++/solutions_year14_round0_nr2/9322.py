#include<iostream> 
#include<cstdio> 

#include<cstdlib> 
#include<algorithm> 
#include<cmath> 
#include<cstring>
 #include<string> 
 #include<map>
  #include<set>
   #include<stack>
    #include<list> 
    #include<vector>
     #include<queue> 
     #include<deque> 
     #include<ctype.h> 

using namespace std; 

#define MOD 1000000007
 #define PI acos(-1) 
 #define MP make_pair
  #define PB push_back
   #define VI vector<int> 
   #define PII pair<int,int> 
   #define LL long long #define SI(x) scanf("%d",&x) 
   #define PRI(x) printf("%d\n",x) 
   #define PRLL(x) printf("%lld\n",x) 
   #define SLL(x) scanf("%lld",&x) 
   #define MEM(v,i) memset(v,i,sizeof(v)) 

   #define REP(i,n) for(int i=0;i<(n);i++) 
   #define FOR(i,a,b) for (int i=(a);i<=(b);i++) 
   #define DEBUG(x) cout<<#x<<"="<<x<<endl 
   #define getcx getchar_unlocked 
double C,F,X;
 double ans,rate;
  int main(){ 
  	int T,k=0;
  	 cin>>T; 
  	while(T--){ 
  		k++;
  		ans=0.0;
  		 rate=2.0; 
  		 cin>>C>>F>>X; 
  		 while(1){ 
  		 	double A=X/rate; 
  		 	double B=C/rate+X/(rate+F);
  		 	 if(B<A){ ans+=C/rate; rate+=F; } 
  		 	 else{ ans+=X/rate; break; } } 
  		 	 cout<<"Case #"<<k<<':'<<' '<<ans<<endl; } 
  		 	 return 0; }