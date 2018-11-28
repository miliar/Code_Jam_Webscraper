#include <bits/stdc++.h>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;++i)


string num[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };


int ccount[26];

void add(vector<int> &v,int nu,char car) {
	int c = ccount[car-'A'];
	FOR(i,num[nu].size()) ccount[num[nu][i]-'A']-=c;
	FOR(i,c) v.push_back(nu);
}

int main(void) {
	int t;
	scanf("%d\n",&t);
	for(int tt=1;tt<=t;++tt) {
		char s[5000];
		scanf("%s\n",s);
		int len = strlen(s);
		vector<int> ans;
		memset(ccount,0,26*4);
		FOR(i,len) ++ccount[s[i]-'A'];
		add(ans,4,'U');
		add(ans,0,'Z');
		add(ans,2,'W');
		add(ans,3,'R');
		add(ans,1,'O');
		add(ans,5,'F');
		add(ans,6,'X');
		add(ans,7,'S');
		add(ans,8,'T');
		add(ans,9,'I');
		sort(ans.begin(),ans.end());
		printf("Case #%d: ",tt);
		FOR(i,ans.size()) printf("%d",ans[i]);
		printf("\n");
	}
}