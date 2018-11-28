//The mean is may that
//input: maxshining level(0～1000), k(k>=0)th number xk( xk is counted number that how many person whose shining level is exactlly k. )
//output:the minimum number p. p is the counted number which invite people.
//conditions: shining level k's person can stand up only the case k-1レベル以下の人がk人以上いる。
#include<iostream>
#include<string>
#include<algorithm>
#include<functional>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;

void Write(char *name, int T);

int t;
char out[100][1002];

signed main() {
	int i, j;
	cin >> t;
	for( i = 0; i < t; i++ ) {
		int smax;
		string s;
		cin >> smax >> s;
		
		int cnt[1001] = {0};
		for( j = 0; j < s.length(); j++ ) {
			cnt[j+1] = cnt[j] + (s[j]-'0');
		}
		
		int ans = 0;
		for( j = 0; j < s.length(); j++ ) {
			if( cnt[j+1] - cnt[j] > 0 ) {
				int invite = max(0, j - cnt[j] - ans);
				ans += invite;
			}
		}
		sprintf(out[i], "Case #%d: %d\n", i+1, ans);
	}
	
	Write("C:\\Users\\Kawakami\\kyopro\\GCJ\\2015\\qual\\out-a-small.txt", t);
	return 0;
}

//outの中を出力(改行なし)
void Write(char *name, int T) {
	FILE *fp = fopen(name, "w");
	for(int i = 0; i < T; i++ ) {
		fprintf(fp, "%s", out[i]);
		fprintf(stdout, "%s", out[i]);
	}
	fclose(fp);
}