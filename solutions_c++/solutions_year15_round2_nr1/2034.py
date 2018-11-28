#include <iostream>
#include <stdio.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <queue>
#include <sstream>
#include <stdlib.h>

using namespace std;

#define MAXN 1000005

int dp[MAXN];

void init(){
  dp[0]=0;
  for(int i=1; i<MAXN; ++i){
    stringstream ss;
    ss<<i;
    string str=ss.str(),str3=ss.str();
    reverse(str.begin(),str.end());
    int num;
    istringstream strm(str);
    strm>>num;
    stringstream ss2;
    ss2<<num;
    string str2=ss2.str();
    reverse(str2.begin(),str2.end());
    if(num>=i || str3!=str2) dp[i]=dp[i-1]+1;
    else dp[i]=min(dp[i-1],dp[num])+1;
  }
}

int main(){
  freopen("A-small-attempt1.in.txt","r",stdin);
  freopen("txt.out","w",stdout);
  int t,n;
  scanf("%d",&t);
  init();
  for(int j=1; j<t+1; ++j){
    scanf("%d",&n);
    //for(int i=0; i<n; ++i) printf("dp[%d] == %d\n",i,dp[i]);
    printf("Case #%d: %d\n",j,dp[n]);
  }
  return 0;
}
