#ifndef __MYLIB_H
#define __MYLIB_H

#include<iostream>
#include<algorithm>
#include<sstream>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<utility>  // pair, make_pair
#include<cstdio>
#include<cmath>
#include<cstring>
#include<climits>
using namespace std;

#define all(vec)    vec.begin(),vec.end()
#define rall(vec)    vec.rbegin(),vec.rend()
#define sz(r)      r.size()
#define rem1(v, i)    (v.erase(v.begin()+i))
#define rem2(v, i, j)  (v.erase(v.begin()+i, v.begin()+j+1))
#define digits(i)    (int)((log(i)/log(10))+1)
#define dround(num)    (int)floor(num+0.5)  // Rounds num to int (int)num+(<.5 to 0, > .5 to 1)
#define strtoint(str)    (extract_int(str)[0])

#define REP(i,n)     for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr)     for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

#define first_bit_index(num) __builtin_ctz(num) // count trailing zeros
#define last_bit_index(num)  __builtin_clz(num) // count leading zeros
#define UNDEFINED_BIT       32
#define test_bit(num, bit)   ((num & 1 << bit) != 0)
#define num_bits(num)       __builtin_popcount(num)

#define inf   INT_MAX
#define mn_inf  INT_MIN

typedef stringstream sstream;
typedef struct point{
  int x, y;
  point(){};
  point(int a, int b){x=a;y=b;}
}point;

int X[] = {0, 1, -1, 0, -1, 1, -1, 1};
int Y[] = {1, 0, 0, -1, -1, 1, 1, -1};


/**
 * Convert int to string
*/
string inttostr(int num)
{
  string res;
  sstream s;

  s << num; s >> res;
  return res;
}

/**
 * Extract int from string
*/
vector<int> extract_int(string str)
{
  sstream s;
  s << str;

  vector<int> res;
  int num = -1;

  while((s >> num))
    res.push_back(num);

  return res;
}

#endif 

/* End of my lib */

void cut_rows(vector<vector<int> > &g, vector<int> rows) {
	for(int i = 0; i < sz(g); i++) {
		for(int j = 0; j < sz(g[i]); j++) {
			if(g[i][j] > rows[i]) g[i][j] = rows[i];
		}
	}
}

void cut_cols(vector<vector<int> >&g, vector<int> cols) {
	for(int i = 0; i < sz(g[0]); i++) {
		for(int j = 0; j < sz(g); j++)
			if(g[j][i] > cols[i]) g[j][i] = cols[i];
	}
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		int n, m;
		cin >> n >> m;

		vector<vector<int> > g1(n, vector<int>(m)), g2(n, vector<int>(m));
		for(int a = 0; a < n; a++)
		for(int b = 0; b < m; b++) {
			cin >> g2[a][b];
			g1[a][b] = 100;
		}

		vector<int> rows(n, 0), cols(m, 0);

		for(int a = 0; a < n; a++)
		for(int b = 0; b < m; b++) rows[a] = max(g2[a][b], rows[a]);

		cut_rows(g1, rows);

		for(int a = 0; a < m; a++)
		for(int b = 0; b < n; b++) cols[a] = max(g2[b][a], cols[a]);

		cut_cols(g1, cols);

		if(g1 == g2) cout << "Case #" << i << ": YES" << endl;
		else cout << "Case #" << i << ": NO" << endl;
	}
}

