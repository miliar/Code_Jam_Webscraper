#include<stdio.h>
#include<iostream>
#include<cstring>
#include<string>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
typedef long long int ll;
typedef long double ld;
#define SLL(x) scanf("%lld",&(x))
#define REP(i,n) for(i=0;i<(n);i++)
#define SI(x) scanf("%d",&(x))
using namespace std;
void pp(ld x){
  printf("%Lf ",x);
}
int main(){
  int i,j,k,n;
  int T,t;
  cin>>T;
  REP(t,T){
    int decc=0,nc=0;
    SI(n);
    vector<ld> a(n),b(n);
    REP(i,n)cin>>a[i];
    REP(i,n)cin>>b[i];
    sort(a.begin(),a.end());sort(b.begin(),b.end());
    int a_l=0,b_i=n-1,a_r=n-1;
    for(i=0;i<n;i++){
      ld x=a[a_r];ld y=b[b_i];
      if(x>y)
	decc++,a_r--;//pp(x);
      else {
	a_l++;	
      }//pp(y-0.000002l);
      
      b_i--;
    }
    int a_i=0;b_i=0;
    for(i=0;i<n;i++){
      ld x=a[a_i];
      if(x>b[b.size()-1]){
	b.erase(b.begin());
	nc++;
      }else{
	vector<ld>::iterator it=upper_bound(b.begin(),b.end(),x);
	b.erase(it);
      }
      a_i+=1;
    }
    printf("Case #%d: %d %d\n",1+t,decc,nc);
  }
  return 0;
}
