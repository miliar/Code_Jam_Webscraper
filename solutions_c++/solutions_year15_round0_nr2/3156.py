#include<iostream>
#include<vector>
using namespace std;

int fun(vector<int> arr, int val) {
	int answer = 0, maxi = -1;
	for(int i = 0; i < arr.size(); i++) {
		maxi = max(maxi, arr[i]);
		if(arr[i] > val){
			answer += (arr[i]/val);
			if(arr[i] % val == 0)
				answer --;
		}
	}
	answer += val;

	return answer;
}

int main() {
	
	int t, d, temp, arrmax = 0, ans;
	int l, r, m1, m2;
	vector<int> in;
	
	cin >> t;
	
	for(int j = 0; j < t; j++) {
		ans = 10001;
		cin >> d;
		in.clear();
		arrmax = 0;
		for(int i = 0; i < d; i++) {
			cin >> temp;
			if(temp > arrmax) {
				arrmax = temp;
			}
			in.push_back(temp);
		}
		for (int i = 1; i <= arrmax; i++) {
			temp = fun(in, i);
			if(temp < ans)
				ans = temp;
		}
		
		cout << "Case #" << j+1 << ": " << ans << "\n";

	}
	return 0;
}
