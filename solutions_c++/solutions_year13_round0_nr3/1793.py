#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <utility>
#include <set>
#include <functional>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <ctime>
using namespace std;

#define FOR(_i,_n) for(int (_i)=0;(_i)<(_n);(_i)++)
#define iss istringstream
#define oss ostringstream
#define mp make_pair
#define pb push_back
#define px first
#define py second
#define pi 3.141592653589793
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int,int> Pair;

int dx[8] = { 0, 1,-1, 0, 1, 1,-1,-1};
int dy[8] = { 1, 0, 0,-1,-1, 1, 1,-1};
int hx[8] = {-2,-2,-1,-1, 1, 1, 2, 2};
int hy[8] = {-1, 1,-2, 2,-2, 2,-1, 1};

vector<int64> v;

bool isPal(int64 x) {
	ostringstream oss;
	oss << x;
	string s = oss.str();
	int i = 0;
	int j = s.size() - 1;
	while(i<j){
		if(s[i] != s[j]) return false;
		i ++;
		j --;
	}
	return true;
}

void pre() {
	for(int64 i=1;i<=10000001;i++) {
		if(isPal(i) && isPal(i*i)) {
			v.pb(i*i);
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	pre();
	
	int T;
	cin >> T;
	for(int t=1;t<=T;t++) {
		int64 A, B;
		cin >> A >> B;
		int cnt = 0;
		for(int i=0;i<v.size();i++) {
			if(A <= v[i] && v[i] <= B) {
				cnt ++;
			}
		}
		cout << "Case #" << t << ": " << cnt << endl;
	}
	
	return 0;
}
