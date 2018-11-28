#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
int main(){
  int tc;
  scanf("%d",&tc);
  rep(num,tc){
    int n,x,cnt=0;
    scanf("%d",&n);
    if(n==0)printf("Case #%d: INSOMNIA\n",num+1);
    else {
      set<int>s;
      while(s.size()<10){
        cnt++;
        x=cnt*n;
        while(x>0){
          s.insert(x%10);
          x/=10;
        }

      }

      printf("Case #%d: %d\n",num+1,cnt*n);
      
    }
  }

  return 0;
}