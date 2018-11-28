#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	// your code goes here
	int t, N, i = 0;
	cin >> t; 
	while(i++ < t){
		cin >> N;
		if(N == 0){
			cout<< "Case #" << i << ": " << "INSOMNIA" <<endl;
			continue;
		}
		vector<int> v(10, 0);
		int allone, mlt;
		long long val = 0;
		allone = 0; 
		mlt = 1;
		while(allone == 0){ //for loop
			val = N * mlt++;
			while(val > 0){
				v[val%10] = 1;
				val /= 10;
			}
			allone = 1;
			for(int i = 0; i < v.size(); i++) {
				allone *= v[i];
			}
			//cout << val <<endl;
		}
		cout<<"Case #" << i << ": " << N*(mlt-1) <<endl;
		v.clear();
	}
	return 0;
}