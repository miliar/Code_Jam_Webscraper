#include <cstdio>

bool nomino()
{
	int x, r, c;
	scanf("%d %d %d", &x, &r, &c);
	
	if(x>=7) return false;

	if((x==4 && ((c==4 && r==2) || (c==2 && r==4))) || (x==6 && ((c==6 && r==3) || (c==3 && r==6)))) return false;

	return ((r * c) % x || (r < x && c < x) || (r<<1 < x || c<<1 < x)) ? false : true;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++)
		printf("Case #%d: %s\n", i, (nomino() ? "GABRIEL" : "RICHARD"));
}