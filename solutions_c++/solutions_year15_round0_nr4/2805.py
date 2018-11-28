#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

inline int fast_input(void)
{
	char t;
	int x=0;
	int neg=0;
	t=getchar();
	while((t<48 || t>57) && t!='-')
		t=getchar();
	if(t=='-')
		{neg=1; t=getchar();}
    while(t>=48 && t<=57)
    {
        x=(x<<3)+(x<<1)+t-48;
        t=getchar();
    }
	if(neg)
		x=-x;
	return x;
}

inline void fast_output(int x)
{
	char a[20];
	int i=0,j;
	a[0]='0';
	if (x<0) {putchar('-'); x=-x;}
	if (x==0) putchar('0');
	while(x)
	{
		a[i++]=x%10+48;
		x/=10;
	}
	for(j=i-1;j>=0;j--)
	{
		putchar(a[j]);
	}
	putchar('\n');
}

int main()
{
int b=0,t,x,r,c;
t=fast_input();
while(b<t)
{
	x=fast_input();
	r=fast_input();
	c=fast_input();
	printf("Case #%d: ",b+1);
	if ((r*c)%x||(r*c)<x*(x-1)) printf("RICHARD\n");
	else printf("GABRIEL\n");
	b++;
}
return 0;
}
