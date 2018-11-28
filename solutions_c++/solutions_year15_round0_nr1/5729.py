#include<stdio.h>
#include<stdlib.h>
#include <cstdio>

inline void fastRead_int(long long int &x) {
    register int c = getchar_unlocked();
    x = 0;
    int neg = 0;

    for(; ((c<48 || c>57) && c != '-'); c = getchar_unlocked());

    if(c=='-') {
    	neg = 1;
    	c = getchar_unlocked();
    }

    for(; c>47 && c<58 ; c = getchar_unlocked()) {
    	x = (x<<1) + (x<<3) + c - 48;
    }

    if(neg)
    	x = -x;
}

inline void fastRead_string(char *str)
{
    register char c = 0;
    register int i = 0;

    while (c < 33)
        c = getchar_unlocked();

    while (c != '\n') {
        str[i] = c;
        c = getchar_unlocked();
        i = i + 1;
    }

    str[i] = '\0';
}
int main()
{
	freopen("A-large.in", "r", stdin);
  	freopen("out.out", "w", stdout);
	long long int T,j;
	fastRead_int(T);
	for(j=1;j<=T;j++)
	{
		long long int Smax,n=0,n1,i;
		fastRead_int(Smax);
		char *f;
		f=(char*)malloc((Smax+1)*sizeof(char));
		fastRead_string(f);
		if(f[0]=='0')
		{
			n1=1;
			n=1;
		}
		else
		n1=f[0]-48;	
		for(i=1;i<=Smax;i++)
		{
			if(i<=n1)
			{
			n1+=(f[i]-48);
			continue;
			}
			else
			{
				n+=(i-n1);
				n1=i+f[i]-48;
			}
		}
	printf("Case #%lld: %lld\n",j,n);
	}
return 0;
}
