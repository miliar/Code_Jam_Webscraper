#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<algorithm>
#include<stack>
#include<queue>
#include<list>

using namespace std;

int main(){
  freopen("in","r",stdin);
  freopen("out","w",stdout);
  int T;
  cin>>T;

  for(int tt=1; tt<=T; tt++){
    printf("Case #%d: ",tt);
    int x,r,c;
    cin>>x>>r>>c;
    int p = r * c;
    int m = p % x;
//    cerr<<"Case #"<<tt<<endl;
//    cerr<<"modulo "<<m;
//cerr<<x<<" "<<r<<" "<<c<<endl;
    if((x-2 == r)||(x-2 == c)) m = -1;
    if(m == 0){
      int pm[x];
      for(int i = 0; i < x; i++){
        pm[i] = 0;
      }
      int k = 0;
      for(int i = 1; i <= x; i++){
        if(x%i == 0){
          pm[k++] = i;
  //        cerr<<"pm["<<k-1<<"] "<<pm[k-1]<<endl;
        }
      }
    //  cerr<<"k "<<k<<endl;
      int ml[k];
      k = 0;
      for(int i = 0; i < x; i++){
        if(pm[i] != 0){
          ml[k++] = pm[i];
        }
      }
      int t = 0;
      bool flag = true;
//      cerr<<"m size "<<k<<endl;
      for(int i = 0; i < k; i++){
        for(int j = t; j < k; j++){
          if(ml[i]*ml[j] == x){
            if(((ml[i]<=r)&&(ml[j]<=c))||((ml[j]<=r)&&(ml[i]<=c))){
            //
            }else{
              flag = false;
            }
          }
        }
        t++;
      }
      if(flag) cout<<"GABRIEL"<<endl;
      else cout<<"RICHARD"<<endl;
    }else{
      cout<<"RICHARD"<<endl;
    }
  }

  return 0;
}
