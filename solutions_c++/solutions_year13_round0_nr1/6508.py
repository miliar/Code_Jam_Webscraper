#include <cstdio>
int map[5][5];
int check()
{
	int a,b,symb;
	for(a=1;a<=4;a++)
	{
		symb = 0;
		for(b=1;b<=4;b++)
		{
			if(symb && map[a][b]!=3 && map[a][b]!=symb) break;
			if(!map[a][b]) break;
			if(map[a][b]!=3) symb=map[a][b];
 		}
		if(b == 5) return symb;
	}
	for(a=1;a<=4;a++)
	{
		symb = 0;
		for(b=1;b<=4;b++)
		{
			if(symb && map[b][a]!=3 && map[b][a]!=symb) break;
			if(!map[b][a]) break;
			if(map[b][a]!=3) symb=map[b][a];
 		}
		if(b == 5) return symb;
	}
	symb = 0;
	for(b=1;b<=4;b++)
	{
		if(symb && map[b][b]!=3 && map[b][b]!=symb) break;
		if(!map[b][b]) break;
		if(map[b][b]!=3) symb = map[b][b];
	}
	if(b == 5) return symb;
	symb = 0;
	for(b=1;b<=4;b++)
	{
		if(symb && map[b][5-b]!=3 && map[b][5-b]!=symb) break;
		if(!map[b][5-b]) break;
		if(map[b][5-b]!=3) symb = map[b][5-b];
	}
	if(b == 5) return symb;
	for(a=1;a<=4;a++)
		for(b=1;b<=4;b++)
		if(!map[a][b]) return 0;
	return 3;
}
int getnextp()
{
	char c;
	do
	{
		scanf("%c",&c);
		if(c=='O') return 1;
		if(c=='.') return 0;
		if(c=='X') return 2;
		if(c=='T') return 3;
	}while(1);
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,i,a,b;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		for(a=1;a<=4;a++)
			for(b=1;b<=4;b++)
			map[a][b] = getnextp();
		int ans = check();
		if(ans == 0)
			printf("Case #%d: Game has not completed\n",i);
		if(ans == 1)
			printf("Case #%d: O won\n",i);
		if(ans == 2)
			printf("Case #%d: X won\n",i);
		if(ans == 3)
			printf("Case #%d: Draw\n",i);
	}
}