#include <iostream>
#include <set>

using namespace std;

int main(){
	freopen("C:/Users/Johan Sannemo/Downloads/A-small-attempt0.in", "r", stdin);
	freopen("C:/Users/Johan Sannemo/Downloads/A-small.out", "w", stdout);
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc){
		set<int> v[2];
		for (int s = 0; s <= 1; ++s){
			int row;
			cin >> row;
			for (int i = 1; i <= 4; ++i){
				for (int j = 1; j <= 4; ++j){
					int num;
					cin >> num;
					if (i == row) v[s].insert(num);
				}
			}
		}
		int num = -1;
		for (auto it = v[0].begin(); it != v[0].end(); ++it){
			if (v[1].find(*it) != v[1].end()){
				if (num != -1){
					cout << "Case #" << tc << ": Bad magician!" << endl;
					goto next;
				} else {
					num = *it;
				}
			}
		}
		if (num == -1){
			cout << "Case #" << tc << ": Volunteer cheated!" << endl;
		} else {
			cout << "Case #" << tc << ": " << num << endl;
		}
	next:;
	}

}