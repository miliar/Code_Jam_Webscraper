#include <iostream>
#include <cmath>
#include <cstdio>

#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int cs;
double c,f,x,r,n,m;

int main(){

  cin>>cs;
  rep(ii,cs){
    cin>>c>>f>>x; 
    m=r=x/2.0; n=0.0;
    
    while(1){
      r += c/(n*f+2.0)+x/((n+1)*f+2.0)-x/(n*f+2.0);
      if(r>m){
        printf("Case #%d: %.6f\n", ii+1, m);
        break;
      }
      m=r;
      n++;
    }
  }


}
