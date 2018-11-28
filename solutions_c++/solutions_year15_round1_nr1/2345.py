#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mt make_tuple
#define mp make_pair
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORR(i,a,b) for(int i=(b);i>=(a);i--)
#define F(i,n) for(int i=0;i<(n);i++)
#define FR(i,n) for(int i=(n)-1;i>=0;i--)
#define R(a,i,b) (a<=i&&i<=b)
typedef tuple<int,int,int> TIII;
typedef tuple<int,int> TII;
typedef pair<int,int> PII;
typedef long long LL;

int T,N,a[1000];
int main(){
   cin>>T;
   F(t,T){
      cin>>N;
      F(i,N){
	 cin>>a[i];
      }
      int rv1=0,rv2=0,maximum=0;
      F(i,N-1){
	 if(a[i]>a[i+1]){
	    rv1+=a[i]-a[i+1];
	    maximum=max(maximum,a[i]-a[i+1]);
	 }
      }
      F(i,N-1){
	 rv2+=(a[i]<=maximum)?a[i]:maximum;
      }
      cout<<"Case #"<<t+1<<": "<<rv1<<" "<<rv2<<endl;
   }
   return 0;
}
