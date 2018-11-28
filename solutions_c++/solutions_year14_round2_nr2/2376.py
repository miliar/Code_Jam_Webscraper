#include<stdio.h>
#include<map>
#include<string.h>
#include<iostream>
#include<stack>
#include<queue>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<algorithm>

#define gc getchar_unlocked()
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define mod 1000000007
#define swap(a,b) ((b)=(a)^(b)^((a)=(b)))
#define INF 100000000000000000LL

using namespace std;

typedef long long int LL;

LL power(LL b,LL p)
{	LL a=1;	while(p) { if(p&1) {	a*=b;	a%=mod;	}	b*=b;	b%=mod;	p=p>>1;	}	return a%mod;	}
	

FILE *fin=fopen("in.txt","r");
FILE *fout=fopen("out.txt","w");

LL in()
{
  char c;LL t=0,negative=1;
  c=gc;
  
  while((c<48||c>57)&&c!='-')c=gc;
  if(c=='-')
  {negative=-1;c=gc;}
  while(c>=48&&c<=57)
  {t=(t<<3)+(t<<1)+c-'0';c=gc;}
  return t*negative;
}

int compare(const void *a,const void *b)	//qsort(arr,n,sizeof(LL),compare)
{
  return (*(LL*)a-*(LL*)b);
}

int main()
{
	LL t,cases,a,b,k,count=0,i,j;
	
	fscanf(fin,"%lld",&t);
	
	while(t--)
	{
		cases++;
		count=0;
		
		fscanf(fin,"%lld %lld %lld",&a,&b,&k);
		
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
					count++;
			}
		}
		
		fprintf(fout,"Case #%lld: %lld\n",cases,count);
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}