
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <iomanip>
#include <fstream>
#include <tuple>

using namespace std;
inline int toInt(string s) { int v; istringstream sin(s); sin >> v; return v; }
template<class T> inline string toString(T x) { ostringstream sout; sout << x; return sout.str(); }
template<class T> inline T sqr(T x) { return x*x; }
typedef pair<int, int> P;
typedef long long ll;
typedef unsigned long long ull;

#define For(i,a,b) for(int i = a;i < b;i++)
#define rep(i,n)  for(int (i) = 0;(i) < (n);(i)++)
#define clr(a) memset((a), 0 ,sizeof(a))
#define mclr(a) memset((a), -1 ,sizeof(a))
#define all(a)  (a).begin(),(a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) (sizeof(a))
#define Fill(a,v) fill((int*)a,(int*)(a+(sz(a)/sz(*(a)))),v)
bool cheak(int x, int y, int xMax, int yMax){ return x >= 0 && y >= 0 && xMax > x && yMax > y; }
const int dx[4] = { -1, 0, 1, 0 }, dy[4] = { 0, 1, 0, -1 };
const int mod = 1000000007;
const int INF = 2147483647;

struct block{
	int d[7][7];
	const int x, y;
	block():x(3),y(3){
		rep(i, 7)rep(j, 7)d[i][j] = 0;
	}
	void turn(){
		int t[7][7];
		rep(i, 7)rep(j, 7)
			t[i][j] = d[i][j];

		rep(i, 7)rep(j, 7)
			d[i][j] = t[j][6-i];
	}
	void Ccounter(){
		int t[7][7];
		rep(i, 7)rep(j, 7)
			t[i][j] = d[i][j];
		rep(i, 7)rep(j, 7)
			d[i][j] = t[i][6 - j];

	}
	void Lcounter(){
		int t[7][7];
		rep(i, 7)rep(j, 7)
			t[i][j] = d[i][j];
		rep(i, 7)rep(j, 7)
			d[i][j] = t[6 - i][j];
	}

	bool ecual(block b){
		rep(i, 7)rep(j, 7){
			if (b.d[i][j] != d[i][j])return false;
		}
		return true;
	}

	void print(){
		rep(i, 7){
			rep(j, 7)cout << d[i][j];
			cout << endl;
		}
		cout << endl;
	}
};

void makeblock();


int d[10][10];
int X, R, C;
int k[5] = { 0, 1, 1, 2, 5 };
block B[5][5];

bool dfs(block b)
{
	bool f = false;

	int air = 0;
	rep(x, R)rep(y, C){
		if (d[x][y] == 0)air++;
	}

	if (air && (air % X != 0))
		return false;

	rep(_, 4){
		
		if(_ != 0){
			block t = b;
			b.turn();
			if (b.ecual(t))continue;
		}
		rep(__, 3){

			if(__ != 0){
				block t = b;
				if (__ == 1)b.Ccounter();
				if (__ == 2)b.Lcounter();
				if (b.ecual(t))continue;
			}

			rep(x, R)rep(y, C){
				rep(i, 7)rep(j, 7){
					int tx = x + i - b.x;
					int ty = y + j - b.y;
					if (tx >= 0 && ty >= 0 && tx < R && ty < C){
						if (d[tx][ty] == 1 && b.d[i][j] == 1)
							goto La;
					}
					else if (b.d[i][j] == 1)goto La;
				}
				rep(i, 7)rep(j, 7){
					int tx = x + i - b.x;
					int ty = y + j - b.y;
					if (tx >= 0 && ty >= 0 && tx < R && ty < C)
						if (b.d[i][j] == 1)d[tx][ty] = 1;
				}

				rep(i,k[X])
				f = f || dfs(B[X][i]);
				if (f)return true;

				rep(i, 7)rep(j, 7){
					int tx = x + i - b.x;
					int ty = y + j - b.y;
					if (tx >= 0 && ty >= 0 && tx < R && ty < C)
						if (b.d[i][j] == 1)d[tx][ty] = 0;
				}

			La:;
			}
			if (__ == 1)b.Ccounter();
			if (__ == 2)b.Lcounter();
		}
	}
	rep(x, R)rep(y, C){
		if (!d[x][y])return false;
	}
	return true;
}


int main()
{
	int T;
	cin >> T;
	makeblock();

	rep(Case, T){
		cin >> X >> R >> C;
		bool f = true;
		rep(i, k[X]){
			clr(d);
			if (!dfs(B[X][i]))f = false;
		}

		cout << "Case #" << Case + 1 << ": ";
		if (f)cout << "GABRIEL" << endl;
		else  cout << "RICHARD" << endl;

	}

}

void makeblock(){

	B[1][0].d[3][3] = 1;

	B[2][0].d[3][3] = 1;
	B[2][0].d[3][4] = 1;

	B[3][0].d[3][3] = 1;
	B[3][0].d[3][4] = 1;
	B[3][0].d[3][5] = 1;

	B[3][1].d[3][3] = 1;
	B[3][1].d[3][4] = 1;
	B[3][1].d[4][4] = 1;

	B[4][0].d[3][3] = 1;
	B[4][0].d[3][4] = 1;
	B[4][0].d[4][3] = 1;
	B[4][0].d[4][4] = 1;

	B[4][1].d[3][3] = 1;
	B[4][1].d[3][4] = 1;
	B[4][1].d[3][5] = 1;
	B[4][1].d[3][6] = 1;

	B[4][2].d[3][3] = 1;
	B[4][2].d[3][4] = 1;
	B[4][2].d[4][3] = 1;
	B[4][2].d[5][3] = 1;

	B[4][3].d[3][3] = 1;
	B[4][3].d[4][3] = 1;
	B[4][3].d[4][4] = 1;
	B[4][3].d[5][3] = 1;

	B[4][4].d[3][3] = 1;
	B[4][4].d[4][3] = 1;
	B[4][4].d[4][4] = 1;
	B[4][4].d[5][4] = 1;

}