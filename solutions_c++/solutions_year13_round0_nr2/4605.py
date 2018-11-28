#include <iostream>
#include <algorithm>
#include <cstring>

#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int cs,n,m,flag;
int b[110][110],colMax[110],rowMax[110];

int main(){
  cin>>cs;
  rep(ii,cs){
    cin>>n>>m;
    memset(colMax,0,sizeof(colMax));
    memset(rowMax,0,sizeof(rowMax));
    flag = 0;

    rep(i,n)rep(j,m){
      cin>>b[i][j];
      colMax[j] = max(colMax[j],b[i][j]);
      rowMax[i] = max(rowMax[i],b[i][j]);
    }
    rep(i,n)rep(j,m)if(b[i][j]!=colMax[j] && b[i][j] != rowMax[i])flag = 1;
    cout<<"Case #"<<ii+1<<": "<<(flag?"NO":"YES")<<endl;
    
  }
  return 0;

}
