#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <string.h>
#include <fstream>
#include <math.h>
#include <sstream>
#include <cctype>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cstdio>
#include <stdio.h>
#include <numeric>
#include <climits>
#include <stack>
#include <utility>

using namespace std;

#define sz(v) (int)v.size()
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define ss   stringstream
#define ll long long
#define pb push_back
#define mem(a,b) memset(a,b,sizeof(a))
#define F first
#define S second
#define cnt(x , n) count(x.begin(),x.end(),n)
#define mx(x) *max_element(x.begin(),x.end())
#define mn(x) *min_element(x.begin(),x.end())
#define ull unsigned long long
#define ac(x) accumulate(all(x),0)
#define iter(it,v) for(it=v.begin();it!=v.end();it++)
#define MP make_pair
#define next next_permutation

int in;
vector<vector<int> > v(4, vector<int>(4));
vector<vector<int> > w(4, vector<int>(4));
vector<int> v1, v2;

int check() {
	int c = 0;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (v1[i] == v2[j]) {
				c++;
				in = i;
			}
		}
	}
	return c;
}

int main() {
	freopen("A-small-attempt2.in","r",stdin);
	freopen("output.in","w",stdout);
	int n, x, y;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> x;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++)
				cin >> v[j][k];
		}
		cin >> y;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++)
				cin >> w[j][k];
		}
		v1 = v[x - 1];
		v2 = w[y - 1];
		cout << "Case #" << i << ": ";
		if (check() == 0)
			cout << "Volunteer cheated!" << endl;
		else if (check() == 1)
			cout << v1[in] << endl;
		else
			cout << "Bad magician!" << endl;
	}
	return 0;
}
