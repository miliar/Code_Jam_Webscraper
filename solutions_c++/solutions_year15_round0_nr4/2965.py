#include<cstdio>
#include<iostream>
#include<cmath>

inline int Read()
{
	register int c=getchar();
	int x=0;
	for(;(c<48 || c>57);c=getchar());
	for(;c>47 && c<58;c=getchar())
		x=(x<<1)+(x<<3)+c-48;
	return x;
}

int main()
{
	freopen("D-small-attempt2.in","r",stdin);
	freopen("opsmall2.txt","w",stdout);
	int t=Read();
	for(int l=1;l<=t;l++)
	{
		int x=Read(),r=Read(),c=Read();
		if(x==1)
		{
			printf("Case #%d: GABRIEL\n",l);
			continue;
		}
		if(x%2==0 && r%2==1 && c%2==1)
		{
			printf("Case #%d: RICHARD\n",l);
			continue;
		}
		if(x==2)
		{
			printf("Case #%d: GABRIEL\n",l);
			continue;
		}
		if(x>r*c || (r*c)%x!=0)
		{
			printf("Case #%d: RICHARD\n",l);
			continue;
		}
		if(r>c)
			std::swap(r,c);
		int max=(r>c)?r:c;
		if(x>max)
		{
			printf("Case #%d: RICHARD\n",l);
			continue;
		}
		if(x==3)
		{
			if(r==1)
			{
				printf("Case #%d: RICHARD\n",l);
				continue;
			}
			printf("Case #%d: GABRIEL\n",l);
			continue;
		}
		if(x==4)
		{
			if(r<3)
			{
				printf("Case #%d: RICHARD\n",l);
				continue;
			}
			printf("Case #%d: GABRIEL\n",l);
			continue;
		}
	}
	return 0;
}
