#include <iostream>
#include <algorithm>

using namespace std;

int main(){
  int cn, ci;
  int n, i;
  int a[1010]={0};
  int sumd, maxd, sum2;
  
  cin >> cn;

  
  
  for(ci=1; ci<=cn; ++ci){
    cin >> n;

    for(i=0; i<n; ++i){
      cin >> a[i];
    }

    //sum all decrement
    sumd=0;
    
    for(i=1; i<n; ++i){
      if(a[i-1] > a[i]){
	sumd += (a[i-1] - a[i]);
      }
    }

    //find largest decrement
    maxd=0;

    for(i=1; i<n; ++i){
      if((a[i-1] - a[i]) > maxd){
	maxd = a[i-1] - a[i];
      }
    }

    sum2=0;
    for(i=0; i<n-1; ++i){
      sum2 += min(a[i], maxd);
    }

    
    cout << "Case #" << ci << ": ";

    cout << sumd << " " << sum2;

    cout << "\n";
  }

  return 0;
}
