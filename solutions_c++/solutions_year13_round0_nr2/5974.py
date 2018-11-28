// ねむい

#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <functional>
using namespace std;

int checkMax(vector<vector<int>> lawn) {
	int max = 0;
	for (int i = 0; i < lawn.size(); i++) {
		for (int j = 0; j < lawn[i].size(); j++) {
			if (lawn[i][j] > max) max = lawn[i][j];
		}
	}
	return max;
}
bool contains(vector<int> list, int value) {
	return find(list.begin(), list.end(), value) != list.end();
}
vector<int> buildList(vector<vector<int>> lawn) {
	vector<int> list;
	list.clear();

	// 外周をチェックして存在するhをリストに追加
	for (int j = 0; j < lawn.size(); j++) {
		// 列方向
		if (!contains(list, lawn[j][0])) list.push_back(lawn[j][0]);
		if (!contains(list, lawn[j][lawn[0].size()-1])) list.push_back(lawn[j][lawn[0].size()-1]);
	}
	for (int j = 0 ; j < lawn[0].size(); j++) {
		// 行方向
		if (!contains(list, lawn[0][j])) list.push_back(lawn[0][j]);
		if (!contains(list, lawn[lawn.size()-1][j])) list.push_back(lawn[lawn.size()-1][j]);
	}

	sort(list.begin(),list.end(),std::greater<int>());//降順ソート

	return list;
}
bool equal (vector<vector<int>> l1, vector<vector<int>> l2) {
	for (int i = 0; i < l1.size(); i++) {
		for (int j = 0; j < l1[i].size(); j++) {
			if (l1[i][j] != l2[i][j]) return false;
		}
	}
	return true;
}
vector<vector<int>> draw(vector<vector<int>> tmp, int x, int y, int dir, int val) {
	switch (dir) {
		case 0://上下
			for (int i = 0; i < tmp.size(); i++) {
				tmp[x+i][y] = val;
			}
			break;
		case 1:// 右←
			for (int i = 0; i < tmp[0].size(); i++) {
				tmp[x][y-i] = val;
			}
			break;
		case 2:// 下上
			for (int i = 0; i < tmp.size(); i++) {
				tmp[x-i][y] = val;
			}
			break;
		case 3:// ←右
			for (int i = 0; i < tmp[0].size(); i++) {
				tmp[x][y+i] = val;
			}
			break;
	}

	return tmp;
}
bool canDraw(vector<vector<int>> lawn, int x, int y, int dir, int val) {
	bool flg = true;
	int size = lawn[0].size();
	switch (dir) {
		case 0://上下
			for (int i = 0; i < lawn.size(); i++) {
				if (lawn[x+i][y] != val) return false;
			}
			break;
		case 1:// 右←
			for (int i = 0; i < lawn[0].size(); i++) {
				if (lawn[x][y-i] != val) return false;
			}
			break;
		case 2:// 下上
			for (int i = 0; i < lawn.size(); i++) {
				if (lawn[x-i][y] != val) return false;
			}
			break;
		case 3:// ←右
			for (int i = 0; i < lawn[0].size(); i++) {//i=6
				if (lawn[x][y+i] != val) return false;
			}
			break;
	}

	return true;
}
void print(vector<vector<int>> v) {
	for (int i = 0 ; i< v.size(); i++) {
		for (int j = 0 ; j < v[i].size(); j++) {
			cout << v[i][j] << " " << flush;
		}
		cout << endl;
	}
}
bool rowOnly(vector<vector<int>> lawn) {
	for (int i = 0; i < lawn.size(); i++) {
		if (lawn[i].size() > 1) return false;
	}
	return true;
}
bool check(vector<vector<int>> lawn) {
	if (lawn.size() == 1 || rowOnly(lawn)) return true;
	// 外周に存在する数字のリストを作る。
	vector<vector<int>> tmp;
	vector<int> list = buildList(lawn);
	int max = checkMax(lawn);

	tmp = lawn;
	// 一旦全要素の最大値に設定（”listの”ではない）
	for (int i = 0; i < lawn.size(); i++) {
		for (int j = 0; j < lawn[i].size(); j++) {
			tmp[i][j] = max;//list[0];
		}
	}

	// 外周を見て数値が高いものから順に行/列方向に走らせる
	if (list.size() > 1) {
		for (int i = 1; i < list.size(); i++) {// 最大値より小さい値から見る
			for (int j = 0; j < lawn.size(); j++) {
				if (j == 2) {
					string buf = "debugPopint";
				}
				// 列方向に、（行方向に塗れるか）見る
				if (lawn[j][0] == list[i] && canDraw(lawn, j, 0, 3, list[i]))
					tmp = draw(tmp, j, 0, 3, list[i]);
				if (lawn[j][lawn[0].size()-1]  == list[i] && canDraw(lawn, j, lawn[0].size()-1, 1, list[i]))
					tmp = draw(tmp, j, lawn[0].size()-1, 1, list[i]);
			}
			for (int j = 0 ; j < lawn[0].size(); j++) {
				// 行方向に見る
				if (lawn[0][j] == list[i] && canDraw(lawn, 0, j, 0, list[i]))
					tmp = draw(tmp, 0, j, 0, list[i]);
				if (lawn[lawn.size()-1][j] == list[i] && canDraw(lawn, lawn.size()-1, j, 2, list[i]))
					tmp = draw(tmp, lawn.size()-1, j, 2, list[i]);
			}
		}
	} else if (list.size() > 0) {
		for (int i = 0; i < list.size(); i++) {// 最大値より小さい値から見る
			for (int j = 0; j < lawn.size(); j++) {
				if (j == 2) {
					string buf = "debugPopint";
				}
				// 列方向に、（行方向に塗れるか）見る
				if (lawn[j][0] == list[i] && canDraw(lawn, j, 0, 3, list[i]))
					tmp = draw(tmp, j, 0, 3, list[i]);
				if (lawn[j][lawn[0].size()-1]  == list[i] && canDraw(lawn, j, lawn[0].size()-1, 1, list[i]))
					tmp = draw(tmp, j, lawn[0].size()-1, 1, list[i]);
			}
			for (int j = 0 ; j < lawn[0].size(); j++) {
				// 行方向に見る
				if (lawn[0][j] == list[i] && canDraw(lawn, 0, j, 0, list[i]))
					tmp = draw(tmp, 0, j, 0, list[i]);
				if (lawn[lawn.size()-1][j] == list[i] && canDraw(lawn, lawn.size()-1, j, 2, list[i]))
					tmp = draw(tmp, lawn.size()-1, j, 2, list[i]);
			}
		}
	}

	print(tmp);
	// 走らせきったあと、元のlawnと一致してたらPLAUSIBLEなlawn
	if (equal(tmp, lawn)) {
		return true;
	} else {
		return false;
	}
}

int main(void)
{
	//ifstream cin("B-sample2.txt");
	//ofstream ofs("B-sample2O.txt");
	ifstream cin("B-small-attempt2.in");
	ofstream ofs("B-small-attempt2.out");

	vector<vector<int>> lawn;
	int T = 0, N, M;
	cin >> T;
	cin.ignore();
	for (int i = 0; i < T; i++) {
		// lawn読み込み
		cout << i << "th index" << endl;
		cin >> N;
		cin >> M;
		lawn.resize(N);
		for (int j = 0; j < lawn.size(); j++) {
			lawn[j].resize(M);
		}
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				cin >> lawn[j][k];
			}
		}

		if (i == 8) {
			int d = 0;
		}
		
		ofs << "Case #" << i+1 << ": " << (check(lawn) ? "YES" : "NO") << endl;
		//cout << (check(lawn) ? "YES" : "NO") << endl;
	}

	return 0;
}