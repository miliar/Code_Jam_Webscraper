#include <iostream>
#include <algorithm>
using namespace std;
int sim(int *p,int d,int height){
  int count = 0;
  for (int i = 0; i < d; ++ i){
    if (p[i]>height){
      count += (p[i]-1)/height;
    }
  }
  //  cout << height <<" " << count << endl;
  return count + height;
}

int main(){
  int t;
  cin >> t;
  for (int casecnt = 1; casecnt <= t; ++ casecnt){
    cout << "Case #"<< casecnt<<": ";
    int d;
    int p[1100];
    cin >> d;
    for (int i = 0; i < d; ++i ){
      cin >> p[i];
    }
    int ans = 1000;
    for (int i = 1000; i >= 1; --i){
      int total = sim(p,d,i);
      if (total < ans) {
	ans = total;
      }
    }
    cout << ans << endl;
  }
}
