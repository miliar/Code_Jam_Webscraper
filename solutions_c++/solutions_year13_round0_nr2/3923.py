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

int main(){
  int T,N,M;
  cin>>T;
  for(int c=1;c<=T;c++){
    cin>>N>>M;
    string ans="YES";
    int grass[N][M];
    for(int i=0;i<N;i++)for(int j=0;j<M;j++)cin>>grass[i][j];
    for(int i=0;i<N;i++){
      int flag;
      for(int j=0;j<M;j++){
        int h=grass[i][j];
        flag=1;
        for(int k=1;i+k<N;k++)if(grass[i+k][j]>h){flag=0;break;}
        for(int k=1;i-k>=0;k++)if(grass[i-k][j]>h){flag=0;break;}
        if(flag)continue;
        flag=1;
        for(int k=1;j+k<M;k++)if(grass[i][j+k]>h){flag=0;break;}
        for(int k=1;j-k>=0;k++)if(grass[i][j-k]>h){flag=0;break;}
        if(flag)continue;
        ans="NO";
        break;
      }
      if(!flag)break;
    }
    printf("Case #%d: %s\n",c,ans.c_str());
  }
}