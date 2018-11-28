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

		vector<double> v1, v2;
		
		double tmp;
		for(int j = 0; j < n; j++) {
			cin >> tmp;
			v1.push_back(tmp);
		}
		for(int j = 0; j < n; j++) {
			cin >> tmp;
			v2.push_back(tmp);
		}
		 
		sort(all(v1));
		sort(all(v2));
			
		int ret1 = 0, ret2 = 0;
		
		vector<double> tmp1 = v1, tmp2 = v2;

		while(sz(tmp1) && sz(tmp2)) {
			
			if(tmp1[0] > tmp2[0]) {
				ret1++;
				rem1(tmp1, 0);
				rem1(tmp2, 0);
			}
			else {
				rem1(tmp1, 0);
				rem1(tmp2, sz(tmp2)-1);
			}
		}
		
		tmp1 = v1, tmp2 = v2;
		
		while(sz(tmp1) && sz(tmp2)) {
			
			if(tmp1[0] < tmp2[0]) {
				rem1(tmp1, 0);
				rem1(tmp2, 0);
			}
			else {
				int x = -1;
				for(int a = 0; a < sz(tmp2); a++)
					if(tmp2[a] > tmp1[0]) {
						x = a;
						break;
					}
					
				if(x == -1) {
					rem1(tmp1, 0);
					rem1(tmp2, 0);
					ret2++;
				}
				else {
					rem1(tmp1, 0);
					rem1(tmp2, x);
				}
			}
			
		}
			
		cout << "Case #" << i << ": " << ret1 << " " << ret2 << endl;
	}
	
	return 0;
}














 