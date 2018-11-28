#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<ctype.h>

//#include<bits/stdc++.h>
//using namespace std;

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


struct profile
{
    int indexi;
    int count;
}s[28];



int compare(const void *p1, const void *p2)
{
    struct profile *elem1 = (struct profile *)p1;    
    struct profile *elem2 = (struct profile *)p2;

   if ( elem1->count < elem2->count)
      return 1;
   else if (elem1->count > elem2->count)
      return -1;
   else
      return 0;
}


int cond(int *N)
{
	//	printf("\nN=%d\n",*N);
	int i,counti=0;
	for(i=0;i<=*N-1;i++)
		{
			if(s[i].count==0)
				counti++;
			//	return(1);
		}
	*N=*N-counti;
//	printf("N=%d\n",*N);
	return(*N);
//	return(counti);
}

int main()
{
//freopen("input.in", "r" , stdin);
//freopen ("output.out","w",stdout);

	int i,T,j,N,sum;
	scanf("%d",&T);
	
	for(j=1;j<=T;j++)
	{
		scanf("%d",&N);
		for(i=0;i<=N-1;i++)
		{
			scanf("%d",&s[i].count);
			s[i].indexi=i;
		}
			qsort(s,N,sizeof(struct profile),compare);
		

		
		printf("Case #%d: ",j);
		while(cond(&N))
		{
			sum=0;	
		/*	printf("printing\n");
			for(int k=0;k<=N-1;k++)
				{
					printf("%d and %c\n",s[k].count,'A'+s[k].indexi);
				}	
			printf("%d and %d\n",s[1].count,N);
		*/
			for(int k=0;k<=N-1;k++)
				{
					sum=sum+s[k].count;	
				}
			if(2*(s[1].count)<=sum-2)
				{
				//	printf("hello\n");
					s[0].count=s[0].count-2;
			//		N=N-2;
		//			printf("s[0].count=%d\n",s[0].count);
					printf("%c%c ",s[0].indexi+'A',s[0].indexi+'A');
					
				}
			else
				{
					if(s[1].count>=1&&!(N==3&&s[1].count==1&&s[0].count==1&&s[2].count==1))
					{
					s[0].count=s[0].count-1;
					s[1].count=s[1].count-1;
			//		N=N-2;
					printf("%c%c ",s[0].indexi+'A',s[1].indexi+'A');
					}
					else
					{
						printf("%c %c%c ",s[0].indexi+'A',s[1].indexi+'A',s[2].indexi+'A');
						N=0;		
					}
				}
				
				qsort(s,N,sizeof(struct profile),compare);
		}
		
		
		
		printf("\n");
		
		
	}
	
//	fclose(stdout);
	return(0);
}


