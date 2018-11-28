#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;
long long p,q;
long double temp1,temp2;
int tc;
char xx;
long long gcd(long long a,long long b){
    if(a==0) return b;
      return gcd(b%a,a);
}
bool is2pow(long long x){
  long long a=1;
  while(a<x){
    a*=2;
    if(a==x) return true;
  }
  return false;
}
int main(){
  cin>>tc;
  int gen;
  for(int tcc=1;tcc<=tc;tcc++){
    cout<<"Case #"<<tcc<<": ";
    cin>>p>>xx>>q;
    long long temp=gcd(p,q);
    p=p/temp;
    q=q/temp;
    //cout<<p<<"  "<<q<<endl;
    long double p1=p;
    int gen=0;
    while(p1<q){
      p1*=2;
      //cout<<p1<<"  ";
      gen++;
    }
    temp2=p1*1.0/q;
    temp1=p*1.0/q;
    temp2=temp1;
    bool ok=false;
    long long lltemp;
    for(int i=0;i<40;i++){
      lltemp=temp2;
      //cout<<i<<"  "<<lltemp<<"  "<<temp2<<endl;
      if(lltemp==temp2){
        ok=true;
        //cout<<"kkk\n";
        break;
      }
      temp2*=2;
    }
    //cout<<temp1<<endl;
    if(ok&&temp1<=1){
      cout<<gen<<endl;
    }else {
      cout<<"impossible\n";
    }
  }
  return 0;
}
