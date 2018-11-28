#include <stdio.h>
//#include <conio.h>
int main()
{
	int t, j=1,x ,r, c;
	freopen("a.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d",&t);
	while (t--) {
		scanf("%d%d%d",&x,&r,&c);
		if(r > c) {
             int temp = r;
             r = c;
             c = temp;
        }
		if (x == 1) {
            printf("Case #%d: GABRIEL\n",j++);
		} else if (x == 2) {
			if ((r*c)%2 == 0) {
				printf("Case #%d: GABRIEL\n",j++);
			} else {
				printf("Case #%d: RICHARD\n",j++);
			}
		} else if (x == 3) {
			if ((r != 1 && c != 1) && (r == 3 || c == 3)) {
				printf("Case #%d: GABRIEL\n",j++);
			} else {
				printf("Case #%d: RICHARD\n",j++);
			}
		}
		else {
			if (c == 4 &&( r == 3 || r == 4) )
               printf("Case #%d: GABRIEL\n",j++);
			else 
                printf("Case #%d: RICHARD\n",j++);
		}
	}
	//getch();
	return 0;
}
