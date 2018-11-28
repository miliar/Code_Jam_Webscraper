#include <stdio.h>

FILE *out = fopen("output.txt", "w");
int t;
int x;
int r;
int c;
int flag = 0;
void process();

void init(){
	x = 0;
	r = 0;
	c = 0;
	flag = 0;
}

void process()
{
	int i;
	switch (x){
	case 1:
		flag = 1;
		break;
	case 2:
	case 3:
	case 4:
	case 5:
	case 6:
		if ((c%x == 0 && r >= x - 1) || (r%x == 0 && c >= x - 1))
			flag = 1;
		break;
	}
}
int main(void)
{
	int i;
	char temp[10001];
	scanf("%d", &t);
	for (i = 1; i <= t; i++) {
		init();
		scanf("%d %d %d", &x, &r, &c);
		process();
		if (flag == 1)
			fprintf(out, "Case #%d: GABRIEL\n", i);
		else
			fprintf(out, "Case #%d: RICHARD\n", i);
	}
	return 0;
}
