#include <cstdio>

int main()
{
	int t, x, r, c, caseNum = 1, i, ans;
	scanf("%d", &t);
	while(t--){
		scanf("%d%d%d", &x, &r, &c);
		if(r > c)
			r ^= c ^= r ^= c;
		ans = 0;
		if(r == 1 && c == 1){
			if(x == 1)
				ans = 1;
		}else if(r == 1 && c == 2){
			if(x <= 2)
				ans = 1;
		}else if(r == 1 && c == 3){
			if(x == 1)
				ans = 1;
		}else if(r == 1 && c == 4){
			if(x <= 2)
				ans = 1;
		}else if(r == 2 && c == 2){
			if(x <= 2)
				ans = 1;
		}else if(r == 2 && c == 3){
			if(x <= 3)
				ans = 1;
		}else if(r == 2 && c == 4){
			if(x <= 2)
				ans = 1;
		}else if(r == 3 && c == 3){
			if(x == 1 || x == 3)
				ans = 1;
		}else if(r == 3 && c == 4){
			ans = 1;
		}else if(r == 4 && c == 4){
			if(x != 3)
				ans = 1;
		}
		if(ans == 1)
			printf("Case #%d: GABRIEL\n", caseNum++);
		else
			printf("Case #%d: RICHARD\n", caseNum++);
	}
	return 0;
}
