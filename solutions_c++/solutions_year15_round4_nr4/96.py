#include <iostream>     
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cassert>
#include <utility>
#include <iomanip>

using namespace std;

const int MAXN = 12;

int tn;
int n, m;
int a[MAXN][MAXN];
long long ans;
int cur[MAXN][MAXN];
vector < vector <long long> > ansv;

bool rot(vector <long long> a, vector <long long> b) {
	int len = (int) a.size();
	for (int i = 0; i < len; i++) {
		bool same = true;
		for (int j = 0; j < len; j++) 
			if (b[(j + i) % len] != a[j]) {
				same = false;
				break;
			}
		if (same)
			return true;
	}
	return false;
}

void go(int ii, int jj) {
	if (ii > n) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				//cout << a[i][j] << " ";
				if (a[i][j] != cur[i][j])
					return;  
			}
			//cout << endl;
		}

		vector <long long> v;

		for (int j = 1; j <= m; j++) {
			long long cur = 0;
			for (int i = 1; i <= n; i++)
				cur = cur * 10 + a[i][j];
			v.push_back(cur);
		}

		for (int i = 0; i < (int) ansv.size(); i++)
			if (rot(ansv[i], v))
				return;

		ansv.push_back(v);

		/*for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++)
				cout << a[i][j] << " ";
			cout << endl;
		}
		for (int i = 0; i < (int) v.size(); i++)
			cout << v[i] << " ";
		cout << endl;
		cout << endl;  */

		//cout << endl;
		ans++;
		return;
	}

	int goi = ii, goj = jj + 1;
	if (goj > m) {
		goi++; goj = 1;
	}
	
	for (int i = 1; i <= 3; i++) {
		cur[ii][jj] = 0;
		a[ii][jj] = i;

		bool bad = false;

		if (a[ii - 1][jj] == i) {
			cur[ii - 1][jj]++;
			cur[ii][jj]++;
			if (cur[ii - 1][jj] > i)
				bad = true;
			if (cur[ii][jj] > i)
				bad = true;  
		}

		if (a[ii][jj - 1] == i) {
			cur[ii][jj - 1]++;
			cur[ii][jj]++;
			if (cur[ii][jj - 1] > i)
				bad = true;
			if (cur[ii][jj] > i)
				bad = true;  
		}

		if (jj == m) {
			if (a[ii][1] == i) {
    			cur[ii][1]++;
    			cur[ii][jj]++;
    			if (cur[ii][1] > i)
    				bad = true;
    			if (cur[ii][jj] > i)
    				bad = true; 
    		}
		}

		if (ii - 1 > 0 && cur[ii - 1][jj] != a[ii - 1][jj])
			bad = true; 

		if (!bad)
			go(goi, goj);

		if (a[ii - 1][jj] == i) {
    		cur[ii - 1][jj]--;
    	}

    	if (a[ii][jj - 1] == i) {
    		cur[ii][jj - 1]--;
    	}

    	if (jj == m) {
    		if (a[ii][1] == i) {
        		cur[ii][1]--;
        	}
    	}
	}                  
}
                       
int main() {
	//assert(freopen("input.txt","r",stdin));
	//assert(freopen("output.txt","w",stdout));

	scanf("%d", &tn);

	for (int test = 1; test <= tn; test++) {
		scanf("%d %d", &n, &m);

		for (int i = 0; i <= n; i++)
			for (int j = 0; j <= m; j++)
				cur[i][j] = 0;
		ans = 0;
		ansv.clear();

		go(1, 1);

		printf("Case #%d: %I64d\n", test, ans);
	}

	return 0;
}