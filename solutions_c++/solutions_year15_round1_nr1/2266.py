#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
const int mxn = 1001;
int num[mxn];
int main(){
	ios::sync_with_stdio(false);
	int casenum;
	cin >> casenum;
	for(int casei = 1;casei <=casenum;casei++){
		int n;
		cin >> n;
		for(int i=0;i<n;i++)
			cin >> num[i];
		long long sum = 0,maxx = 0;
		for(int i=0;i<n-1;i++){
			if(num[i] > num[i+1]){
				sum += num[i] - num[i+1];
				maxx = max(maxx,(long long)num[i] - num[i+1]);
			}
		}
		long long ans2 = 0;
		for(int i=0;i<n-1;i++){
			if(num[i] - maxx >= 0)
				ans2 += maxx;
			else 
				ans2 += num[i];
		}
		cout << "Case #" << casei << ": " << sum << " " << ans2 << endl;
	}
	return 0;
}
