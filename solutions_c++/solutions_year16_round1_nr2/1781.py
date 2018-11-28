#include <iostream>
using namespace std;

int main(){
  int t;
  cin >> t;
  for (int c = 1; c <= t; c++){
  	int n;
    cin >> n;
    
    int sum[2501];
    for (int i = 1; i <= 2500; i++){
    	sum[i] = 0;
	}
	for (int i = 0; i < 2 * n - 1; i++){
		for (int j = 0; j < n; j++){
			int h;
			cin >> h;
			sum[h]++;
		}
	}
	
	cout << "Case #" << c << ":";
	for (int i = 1; i <= 2500; i++){
    	if (sum[i]% 2 != 0){
    		cout << " " << i;
		}
	}
	cout << endl;
  }
}
