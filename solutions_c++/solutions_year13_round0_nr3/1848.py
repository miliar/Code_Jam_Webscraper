#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
using namespace std;

int T,C=1,res;
long long int a,b;
char str[16];
vector<long long int> pals,ans;

void gera(int pos, int size){
  if(pos==(size+1)/2){
    str[size]=0;
    long long int pot=1;
    long long int n=0;
    for(int i=size-1;i>=0;i--,pot*=10)
      n += (str[i]-'0')*pot;
    pals.push_back(n);
    return;
  }
  for(int i=(pos==0?1:0);i<=9;i++){
    str[pos]=str[size-1-pos]=i+'0';
    gera(pos+1,size);
  }
}

int main(){

  for(long long int i=1;i<=9;i++) pals.push_back(i);
  for(long long int i=1;i<=9;i++) pals.push_back(i+i*10);
  for(int i=3;i<14;i++)
    gera(0,i);
  for(int i=0;i<(int)pals.size();i++){
    long long int quad = pals[i]*pals[i];
    if(binary_search(pals.begin(),pals.end(),quad))
      ans.push_back(quad);
  }
  sort(ans.begin(),ans.end());

  scanf("%d",&T);
  while(T--){
    scanf("%lld %lld",&a,&b);
    res=0;
    for(int i=0;i<(int)ans.size();i++){
      if(ans[i]<a) continue;
      if(ans[i]>b) break;
      res++;
    }
    printf("Case #%d: %d\n",C++,res);
  }

  return 0;
}
