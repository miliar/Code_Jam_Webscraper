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

LL T,L,X;
string s;
int trans[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int a[10000],rv[10000],rv2[10000];
int translate(int i,int j){
   int sign=1;
   if(i<0){
      sign*=-1;
   }
   if(j<0){
      sign*=-1;
   }
   return trans[abs(i)][abs(j)]*sign;
}
bool solve(int a[],int n){
   for(int i=0;i<n-2;i++){
      int middle=1;
      for(int j=i+2;j<n;j++){
	 middle=translate(middle,a[(j-1)%L]);
	 if(rv[i]==2&&middle==3&&rv2[j]==4){
	    return true;
	 }
      }
   }
   return false;
}
int main(){
   cin>>T;
   F(t,T){
      cin>>L>>X>>s;
      F(i,s.size()){
	 if(s[i]=='1'){
	    a[i]=1;
	 }
	 else if(s[i]=='i'){
	    a[i]=2;
	 }
	 else if(s[i]=='j'){
	    a[i]=3;
	 }
	 else{
	    a[i]=4;
	 }
      }
      int cur=1;
      for(int i=0;i<L*X;i++){
	 rv[i]=translate(cur,a[i%L]);
	 cur=rv[i];
      }
      cur=1;
      for(int i=L*X-1;i>=0;i--){
	 rv2[i]=translate(a[i%L],cur);
	 cur=rv2[i];
      }
      cout<<"Case #"<<t+1<<": ";
      if(solve(a,L*X)){
	 cout<<"YES"<<endl;
      }
      else{
	 cout<<"NO"<<endl;
      }
   }
   return 0;
}
