#include <bits/stdc++.h>
#define fr(x) scanf("%d", &x)
using namespace std;

map<char,char> m;
char s[2024];

int main(){
	int t, len, k, ans, flag;

	m['+'] = '-';
	m['-'] = '+';

	fr(t);
	for(int t1=1; t1<=t ;++t1){
		scanf(" %s", &s[1]);
		fr(k);
		flag=1;
		ans=0;

		len=strlen(&s[1]);

		for(int i=1;i<=len;++i){
			if(s[i]=='-'){
				if(i+k-1>len){
					flag=0;
					continue;
				}
				++ans;
				for(int j=0;j<k;++j){
					s[i+j]=m[s[i+j]];
				}
			}
		}
		if(flag){
			printf("Case #%d: %d\n", t1, ans);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n", t1);
		}
	}
	return 0;
}