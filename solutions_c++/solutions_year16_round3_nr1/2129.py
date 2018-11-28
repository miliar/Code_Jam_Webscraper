#include <bits/stdc++.h>
using namespace std;
#define int long long 

#undef int
int main(){
	#define int long long 
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int i,j,k,n,m,c;
	cin >> c;
	for (i = 1; i <= c; i++){
		cin >> n;
		vector<pair<int, char>> vect;
		int total = 0;
		for (j = 0; j < n; j++){
			cin >> k;
			total += k;
			vect.emplace_back(make_pair(-k, 'A' + j));
		}
		sort(vect.begin(), vect.end());
		bool fP = true;
		cout << "Case #" << i << ": ";
		while (vect[0].first < 0){
			if (!fP) cout << " ";
			if (vect[0].first % 2 == -1){
				cout << vect[0].second;
				if (vect[1].first == vect[0].first){
					if (vect.size() > 2){
						if (vect[2].first == 0){
							cout << vect[1].second;
							vect[1].first++;
						}
					}else{
						cout << vect[1].second;
						vect[1].first++;
					}
				}
				else if (vect[0].first < -1){
					vect[0].first++;
					cout << vect[0].second;
				}		
			}else{
				cout << vect[0].second;
				if (vect[1].first < 0 && vect[1].first == vect[0].first){
					cout << vect[1].second;
					vect[1].first++;
				} 
			}
			vect[0].first++;
			fP = false;
			sort(vect.begin(), vect.end());
		}
		//print ans here
		cout << "\n";
	}
	return 0;
}