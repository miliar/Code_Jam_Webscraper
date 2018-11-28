#include<bits/stdc++.h>
using namespace std;
#define x getchar()
#define y putchar

inline void out(int k)
{
    int n=k,i=0;
    char ch[15];
    if(n<=0)
    {
        if(n==0)
            y('0');
        else
            y('-');
        n=n*-1;
    }
    while(n>0)
    {
        ch[i]=(n%10)+'0';
        n=n/10;
        i++;
    }
    while(i>0)
    {
        y(ch[i-1]);
        i--;
    }
    y('\n');
}
inline void inp(int &n)
{
    n=0;
    int ch=x,sign=1;
    while( ch < '0' || ch > '9' )
    {
        if(ch=='-')
            sign=-1;
        ch=x;
    }
    while( ch >= '0' && ch <= '9' )
        n=(n<<3)+(n<<1)+ ch-'0', ch=x;
    n=n*sign;
}

int main()
{
	int T;
	inp(T);
	int C = 1;
	while(T--)
	{
		int N,M;
		inp(N);
		inp(M);
		
		int A[N][M];
		int i,j,k,l;
		for(i=0;i<N;i++)
			for(j=0;j<M;j++)
				inp(A[i][j]);
		
		int Final = 0;
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
			{
				int flag = 0;
				for(k=0;k<M;k++)
				{
					if(A[i][j]<A[i][k])
					{
						flag = 1;
						break;
					}
				}
				
				if(flag==0)
					continue;
				
				for(k=0;k<N;k++)
				{
					if(A[i][j]<A[k][j])
					{
						Final = 1;
						printf("Case #%d: NO\n",C);
						break;
					}
				}
				if(Final==1)
					break;
			}
			if(Final==1)
				break;
		}
		if(Final==0)	
			printf("Case #%d: YES\n",C);
		C++;
	}
	return 0;
}
