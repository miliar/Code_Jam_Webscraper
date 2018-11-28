#include <cstdio>
#include <cstring>

char s[1001000];
long long t, l, n, ans;

bool x[300];

int main(){
	scanf("%lld", &t);
	
	long long iar, last;
	
	x['a'] = true;
	x['e'] = true;
	x['i'] = true;
	x['u'] = true;
	x['o'] = true;
	
	for (long long q = 0; q < t; q++){
		scanf(" %s%lld", s, &n);
		
		l = strlen(s);
		ans = 0;
		iar = 0;
		last = -1;
		
		for (int i = 0; i < l; i++){
			if (!x[s[i]])
				iar++;
			else
				iar = 0;
			
			if (iar >= n)
				last = i - n + 1;
			
			if (last != -1)
				ans += last + 1;
		}	
		
		printf("Case #%lld: %lld\n", q + 1, ans);
	}
	
}
