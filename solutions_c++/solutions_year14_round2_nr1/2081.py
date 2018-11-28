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
#define rev(v, i, j)   (reverse(v.begin()+i, v.begin()+j+1))
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

int main() {
	int t;
	cin >> t;
	
	for(int i = 1; i <= t; i++) {
		
		int n;
		cin >> n;
		
		vector<string> vec(n);
		for(int j = 0; j < n; j++) cin >> vec[j];
		
		vector<vector<int> > cnter(n);
		string tmp = "";
		
		bool flag = true;
		for(int a = 0; a < n; a++) {
			string s = "";
			for(int b = 0; b < sz(vec[a]); b++) {
				s += vec[a][b];
				
				while((b+1) < sz(vec[a]) && vec[a][b+1] == vec[a][b]) b++;
			}

			if(tmp == "") tmp = s;
			else if(tmp != s) {
				flag = false;
				break;
			}
		}

		for(int a = 0; a < n; a++) {
			int cnt = 1;
			for(int b = 1; b < sz(vec[a]); b++) {
				if(vec[a][b] == vec[a][b-1]) cnt++;
				else {
					cnter[a].push_back(cnt);
					cnt = 1;
				}
			}
			cnter[a].push_back(cnt);
		}
		
		cout << "Case #" << i << ": ";
		
		if(!flag) cout << "Fegla Won" << endl;
		else {
		
			int ret = 0;
			for(int a = 0; a < sz(cnter[0]); a++) {
				int mx = 0, mn = inf;
				for(int b = 0; b < n; b++) {
					mx = max(cnter[b][a], mx);
					mn = min(cnter[b][a], mn);
				}
				ret += (mx-mn);
			}
			
			cout << ret << endl;
		}
	}
}














 