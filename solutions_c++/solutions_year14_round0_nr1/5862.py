#include<iostream>
#include<unordered_map>
using namespace std;

int main() {
	int n, x, y, p;
	string junk;
	cin >> n;
	//cout << n << "*****\n";
	for (int i = 0; i < n; ++ i) {
		unordered_map<int,int> m;
		
		cin >> x;
		getline(cin, junk);
		//cout << x << "@@@@@\n";
		for (int j = 0; j < 4; ++j) {
			if (j == x-1) {
				for (int k = 0; k<4; ++k) {
					cin >> p;
					//cout << p;
					m[p]++;
				}	
				getline(cin,junk);
			}
			else {
				getline(cin, junk);
			}
		}
		
		cin >> y;
		getline(cin, junk);
		for (int j = 0; j < 4; ++j) {
			if (j == y-1) {
				for (int k = 0; k<4; ++k) {
					cin >> p;
					//cout << p;
					m[p]++;
				}
				getline(cin, junk);
			}
			else {
				getline(cin, junk);
			}
		}
		
		int ans = -1;
		bool found = false;
		bool bad = false;
		for (auto it = m.begin(); it != m.end(); it++) {
			//cout << it->first << it->second << endl;
			if (it->second == 2) {
				if (!found) {
					ans = it->first;
					found = true;
				}
				else {
					bad = true;
					break;
				}				
			}
		}
		
		if (!found) 
			printf("Case #%d: Volunteer cheated!\n", i+1);
		else if (bad)
			printf("Case #%d: Bad magician!\n", i+1);
		else
			printf("Case #%d: %d\n", i+1, ans);
	}
	
	return 0;
}