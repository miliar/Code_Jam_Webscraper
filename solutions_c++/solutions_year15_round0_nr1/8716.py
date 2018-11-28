#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
using namespace std;

int main()
{
  int T;
  int s;
  string states;
  int sum = 0;
  int ans = 0;
  cin >> T;
  for(int i=1;i<T+1;++i){
    cin >> s >> states;
    sum=0;
    ans=0;
    for(int j=0;j<s+1;++j){
      int num = states[j]-'0';
      if(sum<j){
	ans+=(j-sum);
	sum=j;
      }
      sum+=num;     
    }
    cout << "Case #" << i << ": " << ans << endl;
  }
  
  return 0;
}
