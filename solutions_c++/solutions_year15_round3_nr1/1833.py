#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

int main(){
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++){
		int r,c,w;
		cin >> r >> c >> w;
		cout << "Case #" << i << ": ";
		int ans = w + ceil(c/(double)w) - 1;
		cout << ans*r << endl;
		
	}
	return 0;
}