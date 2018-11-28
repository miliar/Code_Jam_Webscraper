#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<bitset>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cmath>
#include<sstream>
#include<fstream>
#include<iomanip>
#include<ctime>
#include<complex>
#include<functional>
#include<climits>
#include<cassert>
#include<iterator>
using namespace std;

int ca = 0;
void output(){
	printf("Case #%d: ", ca);
}
int t;
int r;
int c;
#define MAX 102
char room[MAX][MAX];
bool ok(int x, int y){
	return x >= 0 && y >= 0 && x < r&&y < c;
}
string op = "^v><";
int x[] = { -1, 1, 0, 0 };
int y[] = { 0, 0, 1, -1 };
vector<pair<int, int> > v;
bool use[MAX][MAX];
inline pair<int, int>  nex(int a, int b, int d){
	a += x[d];
	b += y[d];
	while (1){
		if (ok(a, b) == false){
			return make_pair(-1, -1);
		}
		/*if (use[a][b]){
		return make_pair(-2, -2);
		}*/
		use[a][b] = true;
		if (room[a][b] != '.'){
			return make_pair(a, b);
		}
		a += x[d];
		b += y[d];
	}
}
int mod[MAX][MAX];
int main(){
	scanf("%d", &t);
	while (t--){
		ca++;
		scanf("%d%d", &r, &c);
		for (int i = 0; i < r; i++){
			scanf("%s", room[i]);
		}
		v.clear();
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				if (room[i][j] == '.'){
					continue;
				}
				v.push_back(make_pair(i, j));
				for (int k = 0; k < 4; k++){
					if (room[i][j] == op[k]){
						mod[i][j] = k;
					}
				}
			}
		}
		bool ng = false;
		int countt = 0;
		for (int i = 0; i < v.size(); i++){
			/*if (use[v[i].first][v[i].second]){
			continue;
			}*/
			pair<int, int> r = nex(v[i].first, v[i].second, mod[v[i].first][v[i].second]);
			if (r.first == -1){
				bool ook = false;
				for (int j = 0; j <4; j++){
					r = nex(v[i].first, v[i].second, j);
					if (r.first != -1){
						countt++;
						ook = true;
						break;
					}
				}
				if (ook == false){
					ng = true;
					break;
				}
			}
		}
		output();
		if (ng){
			puts("IMPOSSIBLE");
		}
		else{
			printf("%d\n", countt);
		}
	}
	return 0;
}