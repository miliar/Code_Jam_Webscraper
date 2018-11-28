#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<utility>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>

using namespace std;

typedef unsigned long long LL;

bool palindrome(LL x){
  string num="";
  while(true){
    num+=x%10+'0';
    x/=10;
    if(!x)break;
  }
  string rev=num;
  reverse(rev.begin(),rev.end());
  if(num[0]=='0')for(int i=1;i<num.size();i++)num[i-1]=num[i];
  if(rev[0]=='0')for(int i=1;i<rev.size();i++)rev[i-1]=rev[i];
  return num==rev;
}
int main(){
  int T;
  LL A,B;
  cin>>T;
  for(int c=1;c<=T;c++){
    cin>>A>>B;
    A=ceil(sqrt(A));
    B=sqrt(B);
    int ans=0;
    for(LL i=A;i<=B;i++)if(palindrome(i)&&palindrome(i*i))ans++;
    printf("Case #%d: %d\n",c,ans);
  }
  return 0;
}