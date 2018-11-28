#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <map>
#include <ctime>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;

int n;
int cnt[20];

void get_ans()
{
	int v;
	memset(cnt, 0, sizeof(cnt));
	cin >> n;
	for (int i = 1; i <= 4; ++i) {
		for (int j = 1; j <= 4; ++j) {
			cin >> v;
			if(i == n) ++cnt[v];
		}
	}
	cin >> n;
	for (int i = 1; i <= 4; ++i) {
		for (int j = 1; j <= 4; ++j) {
			cin >> v;
			if(i == n) ++cnt[v];
		}
	}
	int ans_num = 0, ans = -1;
	for (int i = 0; i < 20; ++i) if(cnt[i] == 2) {
		++ans_num;
		ans = i;
	}
	if (ans_num == 1) {
		printf("%d\n", ans);
	} else if (ans_num == 0) {
		puts("Volunteer cheated!");
	} else {
		puts("Bad magician!");
	}
}

void read()
{

}

int main()
{
	int cas, tcas = 0;
	for (cin >> cas; cas; --cas)
	{
		//read();
		printf("Case #%d: ", ++tcas);
		get_ans();
	}
}
