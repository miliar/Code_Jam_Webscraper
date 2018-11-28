#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

static int cc = 1;
void output() {
	printf("Case #%d: ", cc++);
}
void readfile(const char* a) {
	freopen(a, "r", stdin);
	freopen("res", "w", stdout);
}
#define __READFIEL__;
double Naomi[2000];
double Ken[2000];
int DeceitfulWar(int n) {
	int head,tail;
	head = 0;
	tail = n - 1;
	int cnt = 0;
	for(int i = 0; i < n; i ++) {
		if(Naomi[i] > Ken[head]) {
			head ++;
			cnt ++;
		}
		else {
			tail --;
		}
	}
	return cnt;
}
int War(int n) {
	int head,tail;
	head = 0;
	tail = n - 1;
	int cnt = 0;
	for(int i = n - 1; i >= 0;i --) {
		if(Naomi[i] > Ken[tail]) {
			cnt ++;
			head ++;
		}
		else {
			tail--;
		}
	}
	return cnt;
}
int main() {
	int cas;
	#ifdef __READFIEL__
	readfile("D--large.in");
	#endif
	cin>>cas;
	while(cas --) {
		int n;
		cin>>n;
		for(int i = 0; i < n; i ++) {
			cin>>Naomi[i];
		}
		for(int i = 0; i < n; i ++)
			cin>>Ken[i];
		sort(Naomi, Naomi + n);
		sort(Ken, Ken + n);

		output();
		cout<<DeceitfulWar(n)<<" "<<War(n)<<endl;
	}
}
