#include<iostream>
#include<algorithm>
#include<map>
#include<sstream>

using namespace std;

int main(){
  map<int,long long> nums;
  int t,tt,i,j,k,flag;
  long long n,nn;
  string sn;
  ostringstream convert;
  scanf("%d",&t);
  tt=t;
  while(t--){
    flag=0;
    scanf("%lld",&n);
    nn=n;
    if(n==0){
      printf("Case #%d: INSOMNIA\n",tt-t);
      continue;
    }
    while(1){
      flag=1;
      convert<<n;
      sn = convert.str();
      for(i=0;i<sn.length();i++){
        nums[sn[i]]++;
      }
      for(i=48;i<58;i++){
        if(!nums[i]){
          flag=0;
        }
      }
      if(flag){
        break;
      }
      n += nn;
      //printf("%lld ",n);
    }
    printf("Case #%d: %lld\n",tt-t,n);
    //for (std::map<int,long long>::iterator it=nums.begin(); it!=nums.end(); ++it)
      //  std::cout << it->first << " => " << it->second << '\n';
    nums.clear();
    convert.str("");
    convert.clear();
  }
  return 0;
}
