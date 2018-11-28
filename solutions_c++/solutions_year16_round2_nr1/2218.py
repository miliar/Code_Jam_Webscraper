#include<stdio.h>
#include<string.h>

//typedef unsigned long long int ull;
//typedef long long int ll;

#define M 1000000007

int minVal(int x, int y) { return (x < y)? x: y; }
int maxVal(int x, int y) { return (x > y)? x: y; }

int fast_pow(long long base, long long n) 
{
    if(n==0)
       return 1;
    if(n==1)
	return base;
    long long halfn=fast_pow(base,n/2);
    if(n%2==0)
        return ( halfn * halfn ) % M;
    else
        return ( ( ( halfn * halfn ) % M ) * base ) % M;
}

int gcd(int n1, int n2)
{
    if (n2!=0)
       return gcd(n2, n1%n2);
    else 
       return n1;
}

int cmpfunc (const void * a, const void * b)
{
   return ( *(int*)a - *(int*)b );
}

char str[2009];

//multiset<int>coll;

int counti[12];

int main()
{
//freopen("A-large.in", "r" , stdin);
//freopen ("output.out","w",stdout);

	int T,j,i,len;
	scanf("%d",&T);
	int countF,countO,countS,countR,countI,temp;
	for(j=1;j<=T;j++)
	{
		for(i=0;i<=10;i++)
			counti[i]=0;
			countF=countO=countI=countS=countR=0;
		scanf("%s",str);
		len=strlen(str);
		
		
		for(i=0;i<=len-1;i++)
			{
				if(str[i]=='Z')
					counti[0]++;
				
				if(str[i]=='W')
					counti[2]++;
				
				if(str[i]=='U')
					counti[4]++;
					
				if(str[i]=='X')
					counti[6]++;
				
				if(str[i]=='G')
					counti[8]++;
				if(str[i]=='O')
					countO++;
				if(str[i]=='I')
					countI++;
				
				if(str[i]=='S')
					countS++;
				
				if(str[i]=='R')
					countR++;
				if(str[i]=='F')
					countF++;
				
			}
		
			counti[5]=countF-counti[4];//true
			counti[7]=countS-counti[6];//true
			counti[9]=countI-counti[5]-counti[6]-counti[8];//true
			counti[3]=countR-counti[0]-counti[4];//true
			counti[1]=countO-counti[0]-counti[2]-counti[4];
			
		/*	for(i=0;i<=9;i++)
				{
					printf("count of %d=%d\n",i,counti[i]);
				}
		*/	
			printf("Case #%d: ",j);
			for(i=0;i<=9;i++)
				{
					for(temp=1;temp<=counti[i];temp++)
						{
							printf("%d",i);
						}
				}
		printf("\n");	
	//	coll.clear();		
		
				
	}

//fclose(stdout);
	return(0);
}


