#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>

using namespace std;

int main(){

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int a, b, n;
		cin >> a >> n;
		int ans = n, cnt = 0;
		vector<int> v;
		for(int i = 0; i < n; i++){
			cin >> b;
			v.push_back(b);
		}
		sort(v.begin(), v.end());
		for(int i = 0; i < n; i++){
			if(a > v[i])
				a += v[i];
			else{
				if(a == 1)
					break;
				a += (a - 1);
				cnt++;
				i--;
			}
			ans = min(ans, cnt + (n - i - 1));
		}
		cout << "Case #" << i + 1 << ": ";
		cout << ans << endl;
	}
	return 0;
}

