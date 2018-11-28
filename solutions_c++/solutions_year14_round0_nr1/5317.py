#include <set>
#include <queue>
#include <vector>
#include <iostream>
#include <iterator>
#include <algorithm>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

VVI read_cards(){
	VVI res(4, VI(4));
	for (int i = 0; i < 4; i++){		
		for (int j = 0; j < 4; j++){
			cin >> res[i][j];
		}
	}
	return res;
}

set<int> get_row(const VVI& c1, int r1){
	set<int> res;
	for (int i = 0; i < 4; i++){		
		res.insert(c1[r1 - 1][i]);
	}
	return res;
}

int solve(){
	int r1, r2;
	VVI c1, c2;
	cin >> r1;	
	c1 = read_cards();
	cin >> r2;
	c2 = read_cards();
	set<int> row1 = get_row(c1, r1);
	set<int> row2 = get_row(c2, r2);
	VI res;
	set_intersection(row1.begin(), row1.end(), row2.begin(), row2.end(),  back_inserter(res));
	if (res.size() == 1){
		return res[0];
	}
	if (res.size() > 1){
		return -1;
	}
	return -2;	
}
int main(){
#if 1
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
		cout << "Case #" << i << ": ";
		int res = solve();
		if (res == -1){
			cout << "Bad magician!";
		}
		else if (res == -2){
			cout << "Volunteer cheated!";
		}
		else{
			cout << res;
		}
		cout << endl;
	}
	return 0;
}