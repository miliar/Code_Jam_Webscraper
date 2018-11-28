/*
Abolfazl Kazemi

BSc in Software Engineering: IAUN Iran
MSc student of Software Engineering: IUST
UVA, topcoder, codeforces, facebook account: AKJ88
*/

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <functional>
#include <string>
#include <sstream>
#include <ctime>
#include <bitset>
#include <cstdlib>

using namespace std;

#define     For(i,a,b)        for (i=a; i<b; i++)
#define     FoR(i,a,b)        for (i=a; i<=b; i++)
#define     Rep(i,a)          for (i=0; i<a; i++)
#define     FIT(it,v)         for (it=(v).begin(); it!=(v).end(); ++it)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     SF                scanf
#define     PF                printf

#define 	EPS  		1e-8
#define 	PI			acos(-1)
#define 	MAXN 		105
#define 	MOD 		1000000007
#define 	INF 		1000000000
#define 	X 			first
#define 	Y 			second

typedef pair<int, int> ii;
typedef pair<double, double> dd;
typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<dd> vdd;

string strs[MAXN], mStrs[MAXN];
vi values[MAXN];
int result;

void remIdenticalChars(string &s, int idx){
	string res = "";
	int i, cnt = 1;
	res += s[0];
	For(i, 1, s.length()){
		if (s[i] != s[i - 1]){
			res += s[i], values[idx].push_back(cnt);
			cnt = 1;
		}
		else
			cnt++;
	}
	values[idx].push_back(cnt);
	s = res;
}

int main(){
	int i, j, k, t, n, m, val, r, Case = 1;
	string maxS;
	bool valid;
#ifndef ONLINE_JUDGE
	freopen("C:\\acm_inp\\cj\\A-small-attempt3.in", "r", stdin);
	freopen("C:\\acm_inp\\cj\\A-small-attempt3.OUT", "w", stdout);
#endif
	cin >> t;
	while (t--){
		cin >> n;
		valid = true;
		maxS = "";
		Rep(i, n){
			cin >> strs[i];
			mStrs[i] = strs[i];
			if (maxS.length() < strs[i].length())
				maxS = strs[i];
			remIdenticalChars(strs[i], i);
			if (i && strs[i] != strs[i - 1])
				valid = false;
		}

		cout << "Case #" << Case++ << ": ";
		if (valid){
			m = strs[0].length();
			result = 0;
			Rep(i, m){
				val =  r= 0;
				Rep(j, n)
					val += values[j][i];
				val /= n;
				Rep(j, n)
					result += abs(values[j][i] - val);
			}
			cout << result << endl;
		}
		else
			cout << "Fegla Won" << endl;
		Rep(i, n)
			values[i].clear();
	}

	return 0;
}













