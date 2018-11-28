#include <stdio.h>
#include <string.h>

int ans = 0;
int sum = 0;
char str[1010];
int main (){
	freopen("A-large.in", "r",stdin);
	freopen("A-large.out", "w",stdout);
	int T = 0 ;
	int kase = 1;
	scanf ("%d", &T);
	while (T --){
		sum = 0;
		ans = 0;
		int max_shy = 0;
		scanf ("%d %s", &max_shy, str);
		if (str[0] == '0')
		{
			ans ++;
			sum = 1;
		}
		else
			sum += str[0] - '0';
		for (int i = 1 ; i < strlen(str); i ++){
			if (sum < i && str[i] != '0')
			{
				ans += i - sum;
				sum = i;
			}
			sum += str[i] - '0';
		}

		printf ("Case #%d: %d\n",kase++, ans);
		
	}
	return 0;
}