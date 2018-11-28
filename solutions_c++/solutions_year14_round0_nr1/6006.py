#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
using namespace std;

int a[10][10], b[10][10];

void conduct() {
	int i, j, av, bv, ar, br, ans;
	map<int, int> dic; dic.clear();
	map<int, int>::iterator it;
	for (i=0; i<16; ++i) dic.insert(pair<int, int>((1<<i), i+1));
	scanf("%d", &ar); ar--;
	for (i=0; i<4; ++i) for (j=0; j<4; ++j) scanf("%d", &a[i][j]);
	scanf("%d", &br); br--;
	for (i=0; i<4; ++i) for (j=0; j<4; ++j) scanf("%d", &b[i][j]);
	for (av=i=0; i<4; ++i) av+=(1<<(a[ar][i]-1));
	for (bv=i=0; i<4; ++i) bv+=(1<<(b[br][i]-1));
	ans=av&bv;
	if (!ans) printf("Volunteer cheated!\n");
	else if ((it=dic.find(ans))==dic.end()) printf("Bad magician!\n");
	else printf("%d\n", it->second);
}

int main() {
	int time; scanf("%d", &time);
	for (int i=1; i<=time; ++i) {
		printf("Case #%d: ", i);
		conduct();
	}
}
