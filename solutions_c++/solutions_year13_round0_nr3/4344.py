using namespace std;
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cassert>
#include<cstring>
#include<cmath>
bool ispal(int n) { 				string s;
				int _i=n;
				while (_i>0)s+='0'+_i%10,_i/=10;
				string s2=s;
				reverse(s2.begin(),s2.end());
				if (s==s2)return true;else return false;
}
int main() {
	int tc;
	cin >> tc;
	for (int casenr=1; casenr<=tc; casenr++) {
		int l, r;
		cin >> l >> r;
		int ans=0;
		for (int i=0;i<1000;i++) {
			if (!ispal(i))continue;
			int n=i*i;
			if (l<=n and n<=r) {
				string s;
				int _i=n;
				while (_i>0)s+='0'+_i%10,_i/=10;
				string s2=s;
				reverse(s2.begin(),s2.end());
				if (s==s2)ans++;
			}
		}
		printf("Case #%d: %d\n", casenr, ans);
	}
}
