#include<iostream>
#include<unordered_set>
#include<cstring>
using namespace std;
bool arr[11];
#undef int
int main() {
#define int long long
	ios::sync_with_stdio(0); cin.tie(0);
	int ts; cin>>ts;
	for(int tt = 1; tt <= ts; tt++) {
		memset(arr, 0, sizeof arr);
		int n; cin >> n;
		int res =0;
		bool ress = false;
		int resss =0;
		for (int i = 0; i < 10000; i++) {
			int tm = i * n;
			while(tm){
				int rm = tm%10;
				tm /=10;
				if (!arr[rm]) { arr[rm] =true; res++;}
				if (res == 10){ ress = true; break;};
			}
			if (ress) { resss = n*i; break;}
		}
		cout << "Case #" << tt << ": ";
		if (ress) cout << resss << "\n";
		else cout << "INSOMNIA" << "\n";
	}

}
