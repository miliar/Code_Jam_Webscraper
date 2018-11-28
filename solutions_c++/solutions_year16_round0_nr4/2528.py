#include <iostream>

using namespace std;

int main(){
  int t , k , c , student;
  cin >> t;
  for(int i = 0 ; i < t ; i++){
    cin >> k >> c >> student;
    cout << "Case #" << i+1 << ": ";
    if((c == 1 && student == k) || (c > 1 && k == 1)){
	for(int j = 1 ; j <= k ; j++)
	  cout << j << " ";
	cout << endl;
    }else if(c > 1 && student >= k-1){
      int x = 2;
      for(int j = 1 ; j < k ; j++){
	cout << x << " ";
	x += (k+1);
      }
      cout << endl;
    }else
      cout << "IMPOSSIBLE" << endl;
  }
  return 0;
}
