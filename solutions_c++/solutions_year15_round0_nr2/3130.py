#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; ++tc){
		int D;
		cin >> D;
		int P[D];
		int mx = 0;
		for (int i = 0; i < D; ++i){
			cin >> P[i];
			if(P[i]>mx)
				mx = P[i];
		}
		int min_mins = mx;
		for(int i=1; i<mx; i++){
			int cur_mins = i;
			for(int j=0; j<D; j++){
				if(P[j]%i==0)
					cur_mins += (P[j]/i - 1);
				else
					cur_mins += P[j]/i;
			}
			if(cur_mins < min_mins)
				min_mins = cur_mins;
		}
		cout << "Case #" << tc << ": ";
		cout << min_mins << endl;
	}
	return 0;
}