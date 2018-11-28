#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <cstdio>
#include <set>
#include <cstring>
using namespace std;

long long t[200];
long long r[200];
long long v[200];
long long desiredV;
long long desiredT;
int n;


inline long long inp() {
	long double a;
	cin >> a;
	return (long long) (a*10000 + 0.01);
}

bool cmp(int a, int b) {
	return abs(t[a]) < abs(t[b]);	
}

bool can() {
	long long sum1 = 0, sum2 = 0;
	vector<int> v1, v2;
	for (int i = 0; i < n; ++i ) {
		if (t[i] <0) {
			sum1 -= t[i]*v[i];
			v1.push_back(i);
		}
		if (t[i]>= 0) {
			sum2 += t[i]*v[i];
			v2.push_back(i);
		}
	}
	long long sum = min(sum1, sum2);
	sort(v1.begin(), v1.end(), cmp);
	sort(v2.begin(), v2.end(), cmp);
	long long ans = 0;
	for (int i : v1) {
		if (sum>=(t[i]*v[i])) {
			ans += v[i];
			sum -= (t[i]*v[i]);
		}
		else {
			ans += sum / abs(t[i]);
			break;
		}
	}
	
	sum = min(sum1, sum2);
	for (int i : v2) {
		if (sum>=(t[i]*v[i])) {
			ans += v[i];
			sum -= (t[i]*v[i]);
		}
		else {
			ans += sum / abs(r[i]);
			break;
		}
	}
	if (ans >= desiredV) return true;
	else return false;
}

string solve() {
	cin >> n;
	desiredV = inp();
	desiredT = inp();
	long long r1 = 0;
	long long r2 = 0;
	for (int i = 0; i < n; ++i ) {
		r[i] = inp();
		t[i] = inp(); //cout << r[i] << " " << t[i] << endl;
		t[i] -= desiredT;
	}
	bool flag1 = false, flag2 = false;
	for (int i = 0; i < n; ++i ) {
		if (t[i] >= 0) flag1 = true;
		if (t[i] <= 0) flag2 = true;
	}
	if (!flag1 || !flag2) return "IMPOSSIBLE";
	
	/*
	long double t1 = 0, t2 = 10e8;
	while (t2-t1>1e-10) {
		long double m = (t1+t2)/2;
		for (int i = 0; i < n; ++i ) v[i] = (long long) (r[i]*m);
		if (can()) t2 = m;
		else t1 = m;
		//cout << m << endl;
	}
	return to_string((t1+t2)/2);
	*/
	
	long long sum1 = 0, sum2 = 0;
	vector<int> v1, v2;
	for (int i = 0; i < n; ++i ) {
		if (t[i] <0) {
			sum1 -= t[i]*r[i];
			v1.push_back(i);
		}
		if (t[i]>= 0) {
			sum2 += t[i]*r[i];
			v2.push_back(i);
		}
	}
	long long sum = min(sum1, sum2);
	sort(v1.begin(), v1.end(), cmp);
	sort(v2.begin(), v2.end(), cmp);
	long long ans = 0;
	long double ans1 = 0;
	long double ttt = 0;
	long long tt1 = 0;
	long long tt2 = 1;
	for (int i : v1) {
		if (sum>=(-t[i]*r[i])) {
			ans += r[i];
			sum += (t[i]*r[i]);
		}
		else {
			if (sum == 0) break;
			tt1 = sum;
			tt2 = -t[i];
			break;
		}
	}
	
	sum = min(sum1, sum2);
	for (int i : v2) {
		if (sum>=(t[i]*r[i])) {
			ans += r[i];
			sum -= (t[i]*r[i]);
		}
		else {
			if (sum == 0) break;
			tt1 += sum;  
			tt2 = t[i];
			break;
		}
	}
	ans1 = ans;
	if (tt1 >0) {
		ans1 += ((long double )tt1)/tt2;
	}
	//desiredV *= tt2;
	//ans = ans*tt2 + tt1;
	//return to_string(ans) + " / " + to_string(tt2);
	return to_string((long double)(( (long double) desiredV) / ans1));
	
}

int main(int argc, char *argv[]) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int caseNum;
	cin >> caseNum;
	for (int caseID = 1; caseID <= caseNum; ++caseID) {
		cout << "Case #" << caseID << ": " << solve() << endl;
		fflush(stdout);
	}
}