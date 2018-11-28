#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<vector>
#include<string>
#include<map>
#include<utility>
#include<cctype>
#include<cstring>
#include<cmath>

#define mp(a,b) make_pair(a,b)
#define rep(i,a,b) for(i=a;i<b;++i)

char map[10][10];


int rowchk(void)
{
    int i,j,cx,co;
    rep(i,0,4)
    {
	cx=co=0;
	rep(j,0,4)
	{
	    cx+=map[i][j]=='X'||map[i][j]=='T'?1:0;
	    co+=map[i][j]=='O'||map[i][j]=='T'?1:0;
	}
	if(cx==4)
	    return 1;
	if(co==4)
	    return 2;
    }
    return 0;
}

int colchk(void)
{
    int i,j,cx,co;
    rep(i,0,4)
    {
	cx=co=0;
	rep(j,0,4)
	{
	    cx+=map[j][i]=='X'||map[j][i]=='T'?1:0;
	    co+=map[j][i]=='O'||map[j][i]=='T'?1:0;
	}
	if(cx==4)
	    return 1;
	if(co==4)
	    return 2;
    }
    return 0;
}

int diagchk(void)
{
    int i,cx,co;
    cx=co=0;
    rep(i,0,4)
    {
	cx+=map[i][i]=='X'||map[i][i]=='T'?1:0;
	co+=map[i][i]=='O'||map[i][i]=='T'?1:0;
    }
    if(cx==4)
	return 1;
    if(co==4)
	return 2;
    cx=co=0;
    rep(i,0,4)
    {
	cx+=map[i][3-i]=='X'||map[i][3-i]=='T'?1:0;
	co+=map[i][3-i]=='O'||map[i][3-i]=='T'?1:0;
    }
    if(cx==4)
	return 1;
    if(co==4)
	return 2;
    return 0;
}

bool drawchk(void)
{
    int i,j;
    rep(i,0,4)
	rep(j,0,4)
	    if(map[i][j]=='.')
		return false;
    return true;
    
}

void print(int a)
{
    if(a==1)
	puts("X won");
    if(a==2)
	puts("O won");
}

int main(void)
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    int i;
    scanf("%d\n",&T);
    for(i=1;i<=T;++i)
    {
	memset(map,0,sizeof(map));
	int j;
	rep(j,0,4)
	    gets(map[j]);
	gets(map[8]);
	printf("Case #%d: ",i);
	int result=0;
	result=rowchk();
	if(result)
	{
	    print(result);
	    continue;
	}
	result=colchk();
	if(result)
	{
	    print(result);
	    continue;
	}
	result=diagchk();
	if(result)
	{
	    print(result);
	    continue;
	}
	if(drawchk())
	    puts("Draw");
	else
	    puts("Game has not completed");
    }
    return 0;
}
