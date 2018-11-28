/*
By Tianyi Chen. All rights reserved.
Date: 2016-04-30
*/
#include<bits/stdc++.h>
using namespace std;
int c[200],remain;
string num[]={
	"ZERO","ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};
vector<int>ans;
void s(int i) {
	bool bad=0;
	for (auto&&x:num[i]) {
		if (--c[x]<0)bad=1;
		--remain;
	}
	if (bad)goto rec;
	ans.push_back(i);
	if (remain==0) {
		for (auto&&x:ans)putchar('0'+x);putchar('\n');;
		throw 0;
	}
	for (int j=i;j<10;++j)s(j);
	ans.pop_back();
rec:for (auto&&x:num[i]) {
	++c[x];
	++remain;
}
}
string str;
int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;scanf("%d",&T);for (int _=1;_<=T;++_) {
		ans.clear();
		cin>>str;memset(c,0,sizeof c);remain=str.length();
		for (auto&&x:str)++c[x];
		printf("Case #%d: ",_);
		try {
			for (int i=0;i<10;++i)s(i);
		} catch (...) {}
	}
}