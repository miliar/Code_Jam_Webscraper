#include<bits/stdc++.h>
using namespace std;
#define x getchar()
#define y putchar

inline void out(long long int k)
{
    long long int n=k,i=0;
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
inline void inp(long long int &n)
{
    n=0;
    long long int ch=x,sign=1;
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

long long int Ar[] = {1 ,2 ,3 ,11 ,22 ,101 ,111 ,121 ,202 ,212 ,1001 ,1111 ,2002 ,10001 ,10101 ,10201 ,11011 ,11111 ,11211 ,20002 ,20102 ,100001 ,101101 ,110011 ,111111 ,200002 ,1000001 ,1001001 ,1002001 ,1010101 ,1011101 ,1012101 ,1100011 ,1101011 ,1102011 ,1110111 ,1111111 ,2000002 ,2001002};


int main()
{
	long long int T;
	inp(T);
	int C = 1;
	int i,j;
	
	for(i=0;i<39;i++)
		Ar[i] = Ar[i]*Ar[i];
	
	while(T--)
	{
		long long int A,B;
		inp(A);
		inp(B);
		
		int Ans1=0,Ans2=0;
		int count = 0;
		for(i=0;i<39;i++)
		{
			if(B>= Ar[i] && Ar[i]>=A)
				count++;
			else if(Ar[i]>B)
				break;
		}
		printf("Case #%d: %d\n",C,count);
		C++;
	}
	return 0;
}