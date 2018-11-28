#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

#define sd(i) scanf("%d",&i)
#define sll(i) scanf("%lld",&i)
#define sull(i) scanf("%llu",&i)
#define sc(i) scanf("%c",&ch)
#define sstr(i) scanf("%s",i)
#define pd(i) printf("%d",i)
#define pll(i) printf("%lld",i)
#define pull(i) printf("%llu",i)
#define pc(i) printf("%c",i)
#define pstr(i) printf("%s",i)
#define newline printf("\n")
#define itoa(i,j) sprintf(i,"%d",j)
#define rep(i,j,n) for(i=j;i<n;i++)
#define ull unsigned long long
#define ll long long


void readline(char *str)
{
	char ch;
	sc(ch);
	int i=0;
	while(ch != '\n') {str[i++]=ch;sc(ch);}
	str[i]='\0';
}

char arr[4][4];
		
void solve(int t)
{
	int i,j;
	rep(i,0,4)
	{
		rep(j,0,4)
		{
			if(arr[i][j]=='O' || arr[i][j]=='.') break; 
		}
		if(j==4) { printf("Case #%d: X won\n",t);return; }
	}
	rep(j,0,4)
	{
		rep(i,0,4)
		{
			if(arr[i][j]=='O' || arr[i][j]=='.') break; 
		}
		if(i==4) { printf("Case #%d: X won\n",t);return; }
	}
	rep(i,0,4) if(arr[i][i]=='O' || arr[i][i]=='.') break;
	if(i==4) { printf("Case #%d: X won\n",t);return; }
	rep(i,0,4) if(arr[i][3-i]=='O' || arr[i][3-i]=='.') break;
	if(i==4) { printf("Case #%d: X won\n",t);return; }
	rep(i,0,4)
	{
		rep(j,0,4)
		{
			if(arr[i][j]=='X' || arr[i][j]=='.') break; 
		}
		if(j==4) { printf("Case #%d: O won\n",t);return; }
	}
	rep(j,0,4)
	{
		rep(i,0,4)
		{
			if(arr[i][j]=='X' || arr[i][j]=='.') break; 
		}
		if(i==4) { printf("Case #%d: O won\n",t);return; }
	}
	rep(i,0,4) if(arr[i][i]=='X' || arr[i][i]=='.') break;
	if(i==4) { printf("Case #%d: O won\n",t);return; }
	rep(i,0,4) if(arr[i][3-i]=='X' || arr[i][3-i]=='.') break;
	if(i==4) { printf("Case #%d: O won\n",t);return; }
	bool is_comp=true;
	rep(i,0,4)
	{
		rep(j,0,4)
		{
			if(arr[i][j]=='.') break;
		}
		if(j!=4) {is_comp=false;break;}
	}
	if(is_comp) printf("Case #%d: Draw\n",t);
	else printf("Case #%d: Game has not completed\n",t);
}

int main()
{
	int t;
	sd(t);
	for(int in=1;in<=t;in++)
	{
		char ch;
		sc(ch);
		int i;
		rep(i,0,4)
		{
			char str[5];
			readline(str);
			int j;
			rep(j,0,4) arr[i][j]=str[j];
		}
		solve(in);
	}
	return 0;
}