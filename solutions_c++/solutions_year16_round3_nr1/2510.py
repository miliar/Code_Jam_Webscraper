#include <iostream>
#include <set>
#include <utility>
#include <tuple>
#include <string>

using namespace std;

int main(){
	int t, n, in;
	set<pair<int, int>, greater<pair<int, int>>> pq;

	cin >> t;

	for (int i = 1; i <= t; i++){
		cin >> n;
		for (int j = 0; j < n; j++){
			cin >> in;
			pq.insert(make_pair(in, j));
		}
		cout << "Case #" << i << ": ";
		while (!pq.empty()){
			int num, party;
			tie(num, party) = *pq.begin();
			pq.erase(pq.begin());
			if (num != 1)
				pq.insert(make_pair(num - 1, party));
			string s(1, 'A' + party);
			if (!pq.empty()){
				int num2, party2, num3, party3;
				tie(num2, party2) = *pq.begin();
				pq.erase(pq.begin());
				if (!pq.empty()){
					tie(num3, party3) = *pq.begin();
					if (num2 == 2 && num3 == 1 && pq.size() % 2 == 0 || num == 1 && pq.size() % 2 == 1){
						pq.insert(make_pair(num2, party2));
					}
					else{
						if (num2 != 1)
							pq.insert(make_pair(num2 - 1, party2));
						string s2(1, 'A' + party2);
						s += s2;
					}
				}
				else{
					if (num2 != 1)
						pq.insert(make_pair(num2 - 1, party2));
					string s2(1, 'A' + party2);
					s += s2;
				}
			}
			s += " ";
			cout << s;
		}
		cout << endl;
	}

	return 0;
}
