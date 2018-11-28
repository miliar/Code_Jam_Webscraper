#include <bits/stdc++.h>
using namespace std;
int arr[1005];
int main(){
	int T;
	int d,temp;
	cin >> T;
	vector<int> plate;
	for(int i=1;i<=T;i++){
		cin >> d;
		plate.clear();
		int maxn = -1;
		int ans = 100000;
		for(int j=0;j<d;j++){
			cin >> temp;
			plate.push_back(temp);
			maxn = max(maxn,temp);
		}
		for(int j=1;j<=maxn;j++){
			temp = j;
			for(int k=0;k<d;k++){
				temp += plate[k]/j;
				if(!(plate[k]%j)) temp--;
			}
			ans = min(ans,temp);
		}
		cout << "Case #" << i << ": " << ans << "\n";
	}
	return 0;
}