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

int main()
{
	int t;
	sd(t);
	int index;
	rep(index,1,t+1)
	{
		int a,b;
		sd(a);sd(b);
		int c=0;
		if(a==1) c++;
		if(a<=4 && b>=4) c++;
		if(a<=9 && b>=9) c++;
		if(a<=121 && b>=121) c++;
		if(a<=484 && b>=484) c++;
		printf("Case #%d: %d\n",index,c);
	}
	return 0;
}