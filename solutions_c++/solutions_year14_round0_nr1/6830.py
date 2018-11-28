# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;

int main()
{

	int t;
	cin >> t;
	
	for (int i = 0; i < t; i++){
		
		int n;
		cin>> n;
		
		vector<int> v;
		vector<int> v1;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++){
				int x;
				cin >> x;
				if(j == n-1) v.push_back(x);
			}
		}
		int m;
		cin >> m;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++){
				int x;
				cin >> x;
				if(j == m-1) v1.push_back(x);
			}
		}
		
		
		int cnt = 0;
		int ans;
		for (int j = 0; j < v.size(); j++ ){
			int fl = 0;
			for (int k = 0; k < v1.size(); k++ ){
				if(v[j] == v1[k]) {
					fl = 1;
					ans = v[j];
					break;
				}
			}
			
			if(fl) cnt++;
		}
		
		cout << "Case #"<<i+1<<": ";
		if(cnt == 1) cout << ans << endl;
		if(cnt > 1) cout <<"Bad magician!" << endl;
		if(cnt == 0) cout <<"Volunteer cheated!" << endl;
	}

	
	return 0;
	
}
