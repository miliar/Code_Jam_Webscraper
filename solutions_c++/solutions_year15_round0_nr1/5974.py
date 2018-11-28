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
int b=0,t,s;
char a[1001];
int ppl,ans,i;
t=fast_input();
while(b<t)
{
	ans=0;
	ppl=0;
	s=fast_input();
	scanf("%s",a);
	for(i=0;i<=s;i++)
	{
		if (ppl>=i) ppl+=a[i]-'0';
		else
		{
			ans+=i-ppl;
			ppl=i+a[i]-'0';
		}
	}
	printf("Case #%d: ",b+1);
	fast_output(ans);
	b++;
}
return 0;
}
