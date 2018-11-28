#include <bits/stdc++.h>

using namespace std;

int main(){
	ios::sync_with_stdio(false);
	int t, k = 1;
	cin >> t;
	while( t-- ){
		int n, total = 0, val;
		cin >> n;
		vector < pair < int, int > > senado;;
		for(int i = 0; i < n; i++){
			cin >> val;
			senado.push_back(make_pair(-val, i));
			total += val;
		}
		vector < string > ans;
		sort(senado.begin(), senado.end());
		while(senado[0].first != 0){
			total--;
			string at = "";
			at += (senado[0].second+'A');
			senado[0].first++;
			char px = '-';
			int id = 0;
			for(int i = 0; i < n; i++){
				if( senado[i].first == 0 ) continue;
				if( (double(-senado[i].first)/double(total)) > 0.5 ){
					px = senado[i].second;
					id = i;
					break;
				}
			}
			if( px != '-' ){
				at += char(px+'A');
				senado[id].first++;
				total--;
			}
			sort(senado.begin(), senado.end());
			ans.push_back(at);
		}
		cout << "Case #" << k++ << ":";
		for(int i = 0; i < ans.size(); i++ ){
			cout << " " << ans[i];
		}
		cout << '\n';
	}
	return 0;
}