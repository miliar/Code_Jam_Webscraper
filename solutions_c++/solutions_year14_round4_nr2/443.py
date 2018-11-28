///*
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> e, D;
int N;

int solve()
{
	int ans = 0;
	vector<int> s = D;
	sort(s.begin(), s.end());
	for(int i = 0; i < s.size(); i++){
		vector<int>::iterator ad;
		int j = 0;
		for(ad = D.begin(); ad != D.end(); ad++, j++){
			if(*ad == s[i]) break;
		}
		int mn = min( j , (int)D.size() - j - 1);
		ans += mn;
		D.erase(ad);
	}
	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		scanf("%d", &N);
		D.clear();
		for(int i = 1; i <= N; i++){
			int a;
			scanf("%d", &a);
			D.push_back(a);
		}
		printf("%d\n", solve());
	}
	return 0;
}

//*/