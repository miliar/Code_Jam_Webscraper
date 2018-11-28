#include <bits/stdc++.h>
using namespace std;

void main2(){
	int len; scanf("%d", &len);
	char s[len+10]; scanf("%s", s);
	int cur = 0, ans = 0;
	for (int i=0; i<=len; i++){
		if (s[i] != '0'){
			ans+= max(0, i-cur);
			cur = max(cur, i);
			cur+= s[i]-'0';
		}
	}
	printf("%d\n", ans);
}

int main(){
	int t; scanf("%d", &t);
	for (int o=1; o<=t; o++){
		printf("Case #%d: ", o); 
		main2();
	}
	return 0;
}
