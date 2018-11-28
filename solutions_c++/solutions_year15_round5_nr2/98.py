#include <bits/stdc++.h>
using namespace std;

int n,k;
int a[1<<20];

void main2(){
	cin >> n >> k;
	for (int i=0; i<n-k+1; i++)
		cin >> a[i];
	int f0 = 0;
	vector< pair<int,int> > Q;
	for (int i=0; i<k; i++){
		int diff = 0;
		int mini = 0, maxi = 0;
		for (int j=i+1; j<n-k+1; j+=k){
			diff+= a[j]-a[j-1];
			mini = min(mini, diff);
			maxi = max(maxi, diff);
		//	cerr << i << " : " << diff << endl;
		}
		f0 = max(f0, maxi-mini);
		Q.push_back(pair<int,int>(mini, maxi));
	}
	int ans = 1<<30;
	for (int i=0; i<k; i++){
		int lo = f0, hi = 1<<28;
		while (lo <= hi){
			int mid = (lo + hi) / 2;
			bool flag = false;
			long long mins = 0;
			long long maxs = 0;
			for (int j=0; j<k; j++) if (j != i){
				int upper = Q[i].second - Q[j].second;
				int lower = Q[i].second - Q[j].first - mid;
				if (upper < lower){
					flag = true;
					break;
				}
				mins+= lower;
				maxs+= upper;
			}
			if (mins > a[0]){
				int l = (mins-a[0])/k;
				mins-= k*l;
				maxs-= k*l;
				while (mins > a[0]) mins-= k, maxs-=k;
			}
			if (maxs < a[0]){
				int l = (a[0]-maxs)/k;
				mins+= k*l;
				maxs+= k*l;
				while (maxs < a[0]) maxs+= k, mins+= k;
			}
			if (flag==false && mins<=a[0] && a[0]<=maxs)
				ans = min(ans, mid), hi = mid-1;
			else
				lo = mid+1;
		}
	}
	cout << ans << endl;
}

int main(){
	int t; cin >> t;
	for (int i=1; i<=t; i++){
		cout << "Case #" << i << ": ";
		main2();
	}
	return 0;
}
