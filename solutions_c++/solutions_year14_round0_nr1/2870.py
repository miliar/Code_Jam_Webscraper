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
	
	int a1[4][4], a2[4][4];
	int n, m;
	
	int t;
	cin >> t;
	
	for(int i = 1; i <= t; i++) {
		
		cin >> n;
		for(int j = 0; j < 4; j++)
		for(int s = 0; s < 4; s++)
		cin >> a1[j][s];
		cin >> m;
		for(int j = 0; j < 4; j++)
		for(int s = 0; s < 4; s++)
		cin >> a2[j][s];
		
		vector<int> answer;
		
		for(int j = 0; j < 4; j++) {
			
			int x = a1[n-1][j];
			
			bool found = false;
			for(int s = 0; s < 4; s++)
			if(x == a2[m-1][s]) found = true;
			
			if(found)
				answer.push_back(x);
		}
		
		cout << "Case #" << i << ": ";
		
		if(sz(answer) == 1) cout << answer[0] << endl;
		else if(sz(answer) == 0) cout << "Volunteer cheated!" << endl;
		else cout << "Bad magician!" << endl;
	}
}














 