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

int T;
int n;
string s;
int main(){
   cin>>T;
   F(t,T){
      cin>>n>>s;
      int rv=0;
      int cur=0;
      F(i,s.size()){
	 if(i>cur&&s[i]!='0'){
	    rv+=i-cur;
	    cur+=i-cur;
	 }
	 cur+=(int)(s[i]-'0');
      }
      cout<<"Case #"<<t+1<<": "<<rv<<endl;
   }
   return 0;
}
