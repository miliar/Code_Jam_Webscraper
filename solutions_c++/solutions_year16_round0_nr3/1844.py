/*************************************************************************
    > File Name: qc.cpp
    > Author: james47
    > Mail: 
    > Created Time: Sat Apr  9 14:57:51 2016
 ************************************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long ll;
const int cN = 16;
const int cM = 500;
int T, N, M, cnt;

struct p{
	string s;
	int fac[10];
};
vector<p> ans;

int getfac(const string &s, int base){
	ll coef = 1, val = 0;
	for (int i = s.length() - 1; i >= 0; i--, coef *= base){
		val += (s[i] - '0') * coef;
	}
	for (int i = 2; (ll)i * i <= val; i++){
		if (val % i == 0) return i;
	}
//	cout << val << ' ' << base << ' ' << s << endl;
	return -1;
}

bool judge(string s){
	p temp;
	for (int i = 2; i <= 10; i++){
		int f = getfac(s, i);
		if (f == -1) return false;
		temp.fac[i-2] = f;
	}
	temp.s = s;
	ans.push_back(temp);
	return true;
}

void dfs(string s){
	if (cnt >= cM) return;
	if (s.length() == cN-2){
		if (judge("1" + s + "1")) cnt ++;
		return;
	}
	dfs(s+"0");
	dfs(s+"1");
}

int main()
{
	cin >> T >> N >> M;
	cout << "Case #1:\n";
	dfs("");
	for (int i = 0; i < M; i++){
		if (N == 32)
			ans[i].s = ans[i].s + ans[i].s;
		cout << ans[i].s;
		for (int j = 0; j < 9; j++)
			cout << ' ' << ans[i].fac[j];
		cout << endl;
	}
	return 0;
}
