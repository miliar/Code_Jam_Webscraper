#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <climits>
#include <limits.h>
#include <string>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <assert.h>
#include <cstring>
using namespace std;
#define rep(i, n) for (int (i) = 0, j1234 = n; (i) < j1234; (i) ++)
#define rep1(i, n) for (int (i) = 1, j1234 = n; (i) <= j1234; (i) ++)
#define For(i, a, b) for (int (i) = (a), ub1234=b; (i) <= ub1234; (i) ++)
#define db(x) {if(debug){cout << #x << " = " << (x) << endl;}}
#define dba(a, x, y) {if(debug){cout << #a << " :";For(i, (x), (y))cout<<" "<<(a)[(i)];cout<<endl;}}
#define clr(x) memset(x,0,sizeof(x));
#define mp make_pair
#define pb push_back
#define endl '\n'
#define ll long long
#define ld long double
#define i 2
#define j 3
#define k 4
const int INF = INT_MAX;
const ll INFL = LLONG_MAX;
const int output_precision = 15;
const ld pi = acos(-1);
const bool debug = true;
// const ll MOD = ;
int lut[5][5];
int mysign(int integer){return (integer < 0)? -1:1;}
set<int> possibleI;
set<int> possibleJ;
int main() {
	ios_base::sync_with_stdio(0); cout.precision(output_precision); cout << fixed;
	cout.tie(0);

	lut[1][1] = 1;
	lut[1][i] = i;
	lut[1][j] = j;
	lut[1][k] = k;
	lut[i][1] = i;
	lut[i][i] = -1;
	lut[i][j] = k;
	lut[i][k] = -j;
	lut[j][1] = j;
	lut[j][i] = -k;
	lut[j][j] = -1;
	lut[j][k] = i;
	lut[k][1] = k;
	lut[k][i] = j;
	lut[k][j] = -i;
	lut[k][k] = -1;
	int T;
	cin >> T;
	rep1(kkk, T){
		possibleI.clear();
		possibleJ.clear();
		int l, x;
		cin >> l >> x;
		string s;
		cin >> s;
		stringstream ss;
		rep(z, x){
			ss << s;
		}
		s = ss.str();
		rep(ii, s.size()){
			s[ii] = s[ii]-'i'+2;		
		}
		
		int c = 1;
		rep(ii, s.size()-2) {
			c = lut[abs(c)][s[ii]] * mysign(c);
			//cout << c <<endl;
			if(c==i) possibleI.insert(ii+1);
		}
	//	db( possibleI.size() );
		for(set<int>::iterator it = possibleI.begin(); it != possibleI.end(); ++it){
			c=1;
			for(int jj = *it; jj < s.size()-1; jj++){
				c = lut[abs(c)][s[jj]] * mysign(c);
				//cout << "here" << c  << endl;
				if(c==j) possibleJ.insert(jj+1);
			}
		}
		bool can = false;
		//db( possibleJ.size() );
		for(set<int>::iterator it = possibleJ.begin(); it != possibleJ.end(); ++it){
			c=1;
			for(int jj = *it; jj < s.size(); jj++){
				c = lut[abs(c)][s[jj]] * mysign(c);
				if(jj==s.size()-1 && c==k){
					can=true;
					break;
				}
			}
			if(can)break;
		}
		cout<< "Case #" << kkk << ": ";
		if(can)cout << "YES";
		else cout << "NO";
		cout << endl;		
	}
}
