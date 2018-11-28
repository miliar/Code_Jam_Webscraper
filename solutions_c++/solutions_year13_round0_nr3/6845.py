#include<stdio.h>
#include<math.h>
#include<string.h>
int foo(int in){
	char s[100] = {0};
	sprintf(s, "%d", in);
	int i = 0, j = strlen(s) -1;
	for(; i < j; i++, j--)
		if(s[i] != s[j])
			return 0;
	return 1;
}
int main(){
	int t, ct = 0;
	scanf("%d", &t);
	while(t--){
		int i, a, b, ans = 0;
		scanf("%d%d", &a, &b);
		int A = ((int)sqrt(a)) * ((int)sqrt(a)) == a ? (int)sqrt(a) : (int)sqrt(a) + 1, B = (int)sqrt(b);
		for(i = A; i <= B; i++)
			if(foo(i))
				ans += foo(i*i);
		printf("Case #%d: %d\n", ++ct, ans);
	}
	return 0;
}
