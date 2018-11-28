#include<stdio.h>
//#include<conio.h>
#include <cstdio>
inline void fastRead_int(int &x) {					//faster input method for long long int type integers
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
int main()
{
	freopen("A-large.in", "r", stdin);
  	freopen("out.out", "w", stdout);
 	int T,i;
	fastRead_int(T);
	for(i=1;i<=T;i++)
	{
	 	int N,x=0,y=0,max;	
		fastRead_int(N);
		int m[N],j;
		for(j=0;j<N;j++)
		fastRead_int(m[j]);
		max=m[0]-m[1];
		for(j=0;j<N-1;j++)
		{
			if(m[j+1]<m[j])
			x+=(m[j]-m[j+1]);
			if((m[j]-m[j+1])>max)
			max=m[j]-m[j+1];
		}
		for(j=0;j<N-1;j++)
		{
			if(m[j]<max)
			y+=m[j];
			else
			y+=max;
		}
		printf("Case #%d: %d %d\n",i,x,y);
	}
//	getch();
	return 0;
}
