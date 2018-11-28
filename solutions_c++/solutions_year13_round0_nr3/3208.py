#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
using namespace std;
bool IsPal(int a);int main() {
	freopen("inputC.in", "r", stdin);
	freopen("outputC", "w", stdout);
	int count[1001];
	memset(count, 0, sizeof(int) * 1001);
	for(int i = 1; i < sqrt(1000); ++i) {
	     if(IsPal(i) && IsPal(i * i)) {
		     count[i * i] = 1;
	     }
	}
	for(int i = 1; i < 1001; ++i) {
		count[i] = count[i - 1] + count[i];
	}
	int t, l, h; cin>>t;
	for(int i1 = 1; i1 <= t; ++i1) {
		cin>>l>>h;	
		cout<<"Case #"<<i1<<": "<<(count[h] - count[l - 1])<<endl;
	}
	
}

bool IsPal(int a) {
	int ret = 0;
	int temp = a;
	while(a != 0) {
		ret = ret * 10 + a % 10;
		a /= 10;
	}
	return ret == temp;
}
