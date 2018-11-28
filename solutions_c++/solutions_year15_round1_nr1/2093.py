#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <utility>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i){
		int n;
		cin >> n;
		vector<int> arr(n);
		for(int j = 0; j < n; ++j){
			cin >> arr[j];
		}
		int ans1 = 0, ans2 =0;
		for(int j = 1; j < n; ++j){
			if(arr[j] < arr[j-1]){
				//cout << "in " << j << endl;
				ans1 += arr[j-1] - arr[j];
			}
		}
		double ate;
		double rate=0;
		for(int j = 1; j < n; ++j){
			if(arr[j] < arr[j-1]){
				int tmp = arr[j-1] - arr[j];
				double t2 = tmp/10.0;
				if(t2 > rate)
					rate = t2;
			}
		}
		ate = rate*10;
		//printf("ate = %lf\n",ate);
		for(int j = 1; j < n; ++j){
			//if(arr[j] < arr[j-1]){
				ans2 += min(ate,(double)arr[j-1]);
			//}
			//else{

			//}
		}
		cout << "Case #" << i << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}