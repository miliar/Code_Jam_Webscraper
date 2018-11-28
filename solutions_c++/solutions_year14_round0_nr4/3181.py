#include <iostream>
#include <algorithm>
using namespace std;

double a[1100];
double b[1100];

int main(){
  int z,t,n,i,j,dw,w;
  cin >> t;
  for(z=1;z<=t;z++){
    cin >> n;
    dw=w=0;
    for(i=1;i<=n;i++){
      cin >> a[i];
    }
    for(i=1;i<=n;i++){
      cin >> b[i];
    }
    sort(a+1,a+n+1);
    sort(b+1,b+n+1);
    i=j=1;
    while(i<=n && j<=n){
      if(a[i]>b[j]){
        dw++;i++;j++;
      }
      else
        i++;
    }
    i=j=n;
    while(i>=1&&j>=1){
      if(a[i]>b[j]){
        w++;
        i--;
      }
      else{
        i--;j--;
      }
    }
    cout << "Case #" << z << ": " << dw << " " << w << endl;
  }
  return 0;
}