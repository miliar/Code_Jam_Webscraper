#include <stdio.h>
 
 
void scan(int &i){ char c; 
                  while ((c = getchar()) == '\n' || c == ' ' || c == '\r');
                  i = c - '0';
                 };
 
 
 
 
 
int main(){
	freopen("small.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, r, c, w, count, countbad, multi;
    int dig[10];
	scanf("%d", &t);
	int y = 1;
	while (t>0 && countbad<100){
        for (int h=0; h<10; h++){
            dig[h]=1;   
        }
        countbad = 0;
        count = 0;
		scanf("%d", &r);
        multi=0;
        while(count<10 && countbad<50){
        multi ++;
        c=multi*r;
        while (c!=0) {
            w = c%10;
            c /= 10;
            if ((dig[w])==1){
                dig[w]=0;
                countbad=0;
                count++;
            }
        }
        countbad ++;
        }
        if (count == 10){
           printf("Case #%d: %d\n", y, r*multi);
        }
        else {
            printf("Case #%d: INSOMNIA\n", y);   
        }
        t--;
        y++;
    }
	return 0;
}