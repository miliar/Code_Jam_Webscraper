#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <utility>
#include <functional>
#include <memory>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <cctype>
#include <limits.h>
using namespace std;
#define ll long long
#define ull unsigned ll
#define ld long double
const int INF = 1e9 + 7;
const double PI = 2 * acos(0.);
const double EPS = 1e-13;
template<class T> inline T sqr(const T& x){ return x*x; }
template<class T> inline bool isInInterval(T x, T a, T b){ return a <= x && x < b; }
void run();
const string problem = "A";
void saveCode(){
	ofstream outFile((problem + ".cpp").c_str());
	ifstream inFile("Source.cpp");
	char k;
	while (inFile.get(k))
		outFile << k;
}
int main(){
	ios_base::sync_with_stdio(0);
#ifdef TRAINING
	saveCode();
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	cout.precision(13);
	cout.setf(cout.fixed);
	run();
	return 0;
}

int direction[4][2] = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };

int getDirection(char k){
	switch (k){
	case '>':
		return 1;
	case '<':
		return 3;
	case '^':
		return 2;
	case 'v':
		return 0;
	}
	return -1;
}

int find_all_circles(int x, int y, vector<vector<char>>& vec, vector<vector<bool> >& used){
	int dir = -1;
	if (vec[x][y] == '.' || used[x][y] == true)
		return 0;
	while (isInInterval(x, 0, (int)vec.size()) && isInInterval(y, 0, (int)vec[0].size())){
		if (vec[x][y] != '.' && used[x][y] == false){
			dir = getDirection(vec[x][y]);
			used[x][y] = true;
		}
		else if (vec[x][y] != '.' && used[x][y] == true){
			return 0;
		}
		x += direction[dir][0];
		y += direction[dir][1];
	}
	return 1;
}


void run(){
	int t;
	cin >> t;
	for (int _t = 1; _t <= t; ++_t){
		int r, c;
		cin >> r >> c;
		vector< vector<char> > table(r, vector<char>(c));
		vector< vector<bool> > used(r, vector<bool>(c, false));
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j){
				cin >> table[i][j];
			}
		bool impossible = false;
		for (int i = 0; i < r && !impossible; ++i){
			for (int j = 0; j < c && !impossible; ++j){
				if (table[i][j] != '.'){
					int count = 0;
					
					for (int p = 0; p < 4; ++p){
						int _x = i, _y = j;
						while (isInInterval(_x, 0, r) && isInInterval(_y, 0, c)){
							if (table[_x][_y] != '.')
								++count;
							_x += direction[p][0];
							_y += direction[p][1];
						}
					}

					impossible = count == 4;
				}
			}
		}
		if (impossible){
			printf("Case #%d: IMPOSSIBLE\n", _t);
			continue;
		}
		
		int result = 0;
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j){
				result += find_all_circles(i, j, table, used);
			}
		printf("Case #%d: %d\n",_t, result);
	}
}