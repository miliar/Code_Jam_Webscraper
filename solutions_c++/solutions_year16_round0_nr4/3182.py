#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
int main(){
	freopen("D.in", "r", stdin);
	freopen("myoutD.out", "w", stdout);
	int T;
	cin >> T;
	
	for(int k = 1; k <= T; ++k){
		int K, C, S;
		cin >> K >> C >> S;
	    cout << "Case #" << k << ":";
	    for(int i = 1; i <= S; ++i){
	    	cout << " " << i;
		}
		cout << endl;
	}
	return 0;
}
