#include<bits/stdc++.h>
using namespace std;

int tc,a,len,val,now,ans;
char ch[5000];

int main() {
	scanf("%d",&tc);
	for(int tk = 1; tk <= tc; tk++) {
		scanf("%d",&a); scanf("%s",&ch); 
		len = strlen(ch); now = (int)ch[0] - '0'; ans = 0;
		for(int i = 1; i < len; i++) {
			val = (int)ch[i] - '0';
			if (now < i && val > 0) {
				ans += (i - now);
				now = i + val;
			} else 
				now = now + val;
		}
		printf("Case #%d: %d\n",tk,ans);
	}
}