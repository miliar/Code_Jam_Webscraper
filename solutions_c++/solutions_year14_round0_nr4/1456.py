#include<bits/stdc++.h>

using namespace std;

int main(){
	freopen("D-large.in","r", stdin);
	freopen("outputD.out","w",stdout);
	int t, n;
	int vb;
	float a[1100], b[1100];
	cin >> t;
	for (int k = 1; k <= t; k++){
		cin >> n;
		for (int i = 1; i <= n; i++)
			cin >> a[i];
		for (int i = 1; i <= n; i++)
			cin >> b[i];
		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);
		
		int i, j;
		int m = n;
		int nm = 0, ken = 0;
		for (i = n; i >= 1; i--){
			for (j = m; j >= 1; j--)
				if (b[j] > a[i]){
					ken++;
					m = j-1;
					break;
				}
		}
		m = n;
		for (i = n; i >= 1; i--){
			for (j = m; j >= 1; j--)
				if (a[j] > b[i]){
					nm++;
					m = j-1;
					break;
				}
		}
		cout << "Case #" << k << ": ";
		cout << nm << " " << n -ken << endl;
	}
}
