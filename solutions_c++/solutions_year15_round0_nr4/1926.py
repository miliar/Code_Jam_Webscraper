#include <cstdio>
int T;
int Ti;
int x,r,c;
void swap(int &x, int &y)
{
	x^=y^=x^=y;
}
int main()
{
	scanf("%d", &T);
	for(Ti=1;Ti<=T;Ti++)
	{
		scanf("%d%d%d",&x,&r,&c);
		if(r<c) swap(r,c);
		if((r*c)%x == 0 && r>=x && c>=x-1 && x<7) printf("Case #%d: GABRIEL\n", Ti);
		else printf("Case #%d: RICHARD\n", Ti);
	}
	return 0;
}
