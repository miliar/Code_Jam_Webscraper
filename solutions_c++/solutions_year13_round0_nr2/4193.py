#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;
vector< vector<int> > lawn;
int main(){
  int N,a,b,i,j,c,t=0;
  int k,m;
  char poss = 1;
  char posa,posb;
  cin>>N;
  for(c=1;N--;c++){
    cin>>a>>b;
    lawn.resize(a);
    for(i=0;i<a;i++){
      lawn[i].resize(b);
      for(j=0;j<b;++j){
        cin>>lawn[i][j];
      }
    }
    poss = 1;
    for(i=0;i<a;i++){
      for(j=0;j<b;++j){
        posa = posb = 1;

        for(k=0;k<a;++k){
          if(lawn[k][j] > lawn[i][j]){
            posa = 0;
            break;
          }
        }
        for(k=0;k<b;++k){
          if(lawn[i][k] > lawn[i][j]){
            posb = 0;
            break;
          }
        }
        if(!posa && !posb){
          poss = 0;
          break;
        }
      }
      if(!poss) break;
    }
    if(poss)  printf("Case #%d: YES\n",c);
    else      printf("Case #%d: NO\n",c);
  }
  return 0;
}
