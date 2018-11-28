#include <iostream>
#include <map>
#include <vector>

using namespace std;

int getAns(vector<int>& arr) {
	for(int i=arr.size()-1; i>=0; i--) {
		if(arr[i] > 0) return i;
	}
	return 0;
}

void print(vector<int>& arr) {
	for(int i=0; i<arr.size(); i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
}

int solve(vector<int>& arr) {
	int ans = INT_MAX;
	int maxp = 0;
	// first check if we need to change anything
	for(int i=0; i<arr.size(); i++) {
		if(arr[i] > 0) maxp = max(maxp, i);
	}

	for(int j=arr.size()-1; j>=0; j--) {
		// try out the various ways of splitting
		if(j>3 && arr[j]>0) {
			int num = j;
			int bestd = num/2;
			int bestnd = num-num/2;
			for(int d=2; d<=num/2; d++) {
				arr[d]++;
				arr[num-d]++;
				arr[num]--;
			//	ans = min(ans, 1+solve(arr));
				int ans2 = min(ans, 1+solve(arr));
				if(ans2 < ans) {
					bestd = d;
					bestnd = num-d;
					ans = ans2;
				}
				arr[d]--;
				arr[num-d]--;
				arr[num]++;
			}
			//arr[bestd]++;
			//arr[bestnd]++;
			///arr[num]--;
			break;
		}
	}
	return min(ans, maxp);
}

int main(int argc, char** argv)
{
	int T, D, p;
	cin >> T;

	for(int i=0; i<T; i++)
	{
		cin >> D;
		vector<int> ps;
		int maxp = 0;
		for(int d=0; d<D; d++) {
			cin >> p;
			ps.push_back(p);
			maxp = max(p, maxp);
		}
		// make array of size maxp+1
		vector<int> arr(maxp+1, 0);
		// initialise counts of each diner
		for(int j=0; j<ps.size(); j++) {
			arr[ ps[j] ]++;
		}

		int ans = solve(arr);

		cout << "Case #" << i+1 << ": " << ans << endl;
	}

	return 0;
}
