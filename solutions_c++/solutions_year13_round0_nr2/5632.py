#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>

#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

#define pb push_back
#define fi(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define fit(v) fi(it, v)
#define f(i,n) for(int i = 0; i < (n); ++i)

#define fs first
#define sc second
#define mp make_pair

#define all(v) (v).begin(), (v).end()
#define ll long long int
#define vi vector<int>
#define vii vector<vi >
using namespace std;
int ctr[110] = {0};
int a, b, M = 0;
bool ok(int x,int y) {return x >= 0 && y >= 0 && x < a && y < b;};

int find_row(vii m){
	int x = -1, y = 1000;
	f(i,a){
		int k = m[i][0];
		bool okk = true, test = false;
		f(j,b){
			if (m[i][j] != k || k == M) okk = false;
			if (ok(i-1,j) && m[i-1][j] != k) test = true;
			if (ok(i+1,j) && m[i+1][j] != k) test = true;
		}
		if (okk && test && k < y) {
			y = k;
			x = i;
		}
	}
	return x;
}

int find_col(vii m){
	int x = -1, y = 1000;
	f(i,b){
		int k = m[0][i];
		bool okk = true, test = false;
		f(j,a){
			if (m[j][i] != k || k == M) {
				okk = false;
			}
			if (ok(j,i-1) && m[j][i-1] != k) test = true;
			if (ok(j,i+1) && m[j][i+1] != k) test = true;
		}
		if (okk && test && k < y) {
			y = k;
			x = i;
		}
	}
	return x;
}


void change_row(vii &m, int k){
	f(i,b){
		int x = ok(k-1,i) ? m[k-1][i] : 0;
		int y = ok(k+1,i) ? m[k+1][i] : 0;
		int z = max(x,y);
		m[k][i] = z;
		ctr[z]++;
	}
}

void change_col(vii &m, int k){
	f(i,a){
		int x = ok(i,k-1) ? m[i][k-1] : 0;
		int y = ok(i,k+1) ? m[i][k+1] : 0;
		int z = max(x,y);
		m[i][k] = z;
		ctr[z]++;
	}
}

int main(){
	
	ofstream output;
	output.open("problemB.out");
	ifstream input;
	input.open("problemB.in");
	
	int t; input >> t;
	
	
	for(int c = 1; c <= t; ++c){
		M = 0; 
		cout << c << endl;
		f(i,110) ctr[i] = 0;
		vii m;	
		input >> a >> b;
		f(i, a) {
			vi v;
			f(j, b) {
				int k; input >> k;
				v.pb(k);
				if (k > M) M = k;
				ctr[k]++;
			}
			m.pb(v);
		}
		int change = -1;
		do {

			if ((change = find_row(m)) >= 0) {
				change_row(m,change);
			} else if ((change = find_col(m)) >= 0) {
				change_col(m,change);
			}			
			
		} while (change >= 0);
		output << "Case #" << c << ": " << ((ctr[M] == a*b) ? "YES" : "NO") << endl;
	}
	input.close();
	output.close();
	return 0;
}
