#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<map>
#include<vector>
#include<deque>
#include<sstream>
using namespace std;
int t;
unsigned long long a,b;
vector <unsigned long long> sq;
vector <unsigned long long>::iterator it,en;
unsigned long long revn(unsigned long long n){
  unsigned long long rev=0;
  while(n>9){          
    rev=(rev+(n%10))*10;
    n=n/10;
  }
  rev+=n;
  return rev;
}
bool isPalin(unsigned long long a){
  if(a==revn(a)){
    return true;
  }
  return false;
}
void pre(){
  for(unsigned long long i=1;i<10000000;i++){
    if(isPalin(i)&&isPalin(i*i)){
      sq.push_back(i*i);
      //cout<<i*i<<"  ";
    }
  }
  en=sq.end();
}
int main(){
  pre();
  //cout<<endl<<sq.size()<<endl;
  int ans;
  unsigned long long temp;
  scanf("%d",&t);
  for(int tc=1;tc<=t;tc++){
    ans=0;
    cin>>a>>b;
    for(it=sq.begin();it!=en;it++){
      temp=*it;
      if(temp>b)break;
      if(temp>=a&&temp<=b){
        ans++;
        //cout<<temp<<"<="<<b<<"   ";
      }
    }
    printf("Case #%d: ",tc);
    printf("%d\n",ans);
  }
  return 0;
}
