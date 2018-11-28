#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<cmath>
using namespace std;

int main(){
  long long t=0, i=0;
  double c=0, f=0, x=0, sumatime=0, sucasnycasc=0, sucasnef=0, minulycasx=0, sucasnycasx=0;
  cin >> t;
  for(i=0; i<t; i++){
    sumatime=0;
    cin >> c >> f >> x;
    sucasnycasc=c/2;
    sucasnef=2+f;
    minulycasx=x/2;
    sucasnycasx=x/sucasnef;
//     cout << sucasnycasc << " < " << minulycasx << " - " << sucasnycasx << endl;
    while(sucasnycasc<minulycasx-sucasnycasx){
//       cout << sucasnycasc << " < " << minulycasx << " - " << sucasnycasx << endl;
      sumatime+=sucasnycasc;
      sucasnycasc=c/sucasnef;
      sucasnef+=f;
      minulycasx=sucasnycasx;
      sucasnycasx=x/sucasnef;
    }
    sumatime+=minulycasx;
    printf("Case #%lld: %.14lf\n", i+1, sumatime);
  }
  return 0;
}