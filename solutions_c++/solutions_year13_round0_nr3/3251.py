#include <cstdio>
#include <iostream>

using namespace std;

const int t[5]={1,4,9,121,484};
int tc;
int cases=1;

int main(){
  scanf("%d ",&tc);
  while(tc--){
    int ans =0;
    int a,b;
    scanf("%d %d ",&a,&b);
    for(int i=0;i<5;i++){
      if(a<=t[i] && b>=t[i]) ans++;
    }
    printf("Case #%d: %d\n",cases,ans);
    cases++;
  }
  return 0;
}