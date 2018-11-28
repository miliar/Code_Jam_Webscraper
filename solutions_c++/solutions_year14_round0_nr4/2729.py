//Sat Apr 12 18:14:12 IST 2014
//Author- Priyanshu Srivastava
//CSE 2nd Year
//MNNIT Allahabad

#include <iostream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>

#define min(a,b) 	(a<b?(a):(b))
#define max(a,b) 	(a>b?(a):(b))
#define getcx 		getchar_unlocked
#define lli 		long long
#define clr(a,b) 	memset(a,b,sizeof(a))

#define S(a) 		scanf("%d",&a);
#define SL(a) 		scanf("%lld",&a);
#define SS(a) 		scanf("%s",a);
#define SA(a,n) 	{ int i;for(i=0;i<n;i++) scanf("%d",&a[i]);   }
#define SLA(a,n) 	{ int i;for(i=0;i<n;i++) scanf("%lld",&a[i]); }
#define PA(a,n) 	{ int i;for(i=0;i<n;i++) printf("%d ",a[i]);printf("\n");  }
#define PLA(a,n) 	{ int i;for(i=0;i<n;i++) printf("%lld ",a[i]);printf("\n");}

//Bitwise
#define chkbit(s, b) 	(s & (1<<b))
#define setbit(s, b) 	(s |= (1<<b))
#define clrbit(s, b) 	(s &= ~(1<<b))

#define chk(a) 		cout << endl << #a << " : " << a << endl;
#define gc 		getchar();

using namespace std;
void fscani(int *x)
{
	int n=0;int sign=1;char c=getcx();
	while(c<'0' || c>'9'){if(c=='-') sign=-1;c=getcx();}
	while(c>='0' && c<='9'){n=(n<<1)+(n<<3)+(c-'0');c=getcx();}
	n=n*sign;*x=n;
}
void fscanl(lli *x)
{
	lli n=0;int sign=1;char c=getcx();
	while(c<'0' || c>'9'){if(c=='-') sign=-1;	c=getcx();}
	while(c>='0' && c<='9')	{n=(n<<1)+(n<<3)+(c-'0');c=getcx();}
	n=n*sign;*x=n;
}

void preprocess()
{
	
}

int findOptimal(double naomi[],double ken[],int n)
{
	double Naomi[n],Ken[n];
	for(int i=0;i<n;i++)
	{
		Naomi[i]=naomi[i];
		Ken[i] = ken[i];
	}
	int ans = 0;
	int p1=0,p2=0;
	for(int i=0;i<n;i++)
	{
		int j;
		for(j=0;j<n;j++)
			if(Ken[j] > Naomi[i])
			{
				Ken[j]=-1;
				break;
			}
		if(j==n)
			ans++;
	}
	return ans;
}
 
int findDeceitful(double naomi[],double ken[],int n)
{
	double Naomi[n],Ken[n];
	for(int i=0;i<n;i++)
	{
		Naomi[i]=naomi[i];
		Ken[i] = ken[i];
	}
	int p1=0,p2=0;int ans=0;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
			if(Naomi[i] > Ken[j])
			{
				Ken[j] = 2;
				ans++;break;
			}
	}
	return ans;
}

int main()
{
	int t;S(t);int k=0;
	for(k=1;k<=t;k++)
	{
		int n;S(n);
		double naomi[n],ken[n];
		for(int i=0;i<n;i++)	scanf("%lf",&naomi[i]);
		for(int j=0;j<n;j++)	scanf("%lf",&ken[j]);
		sort(naomi,naomi + n);	
		sort(ken, ken + n);
		//for(int i=0;i<n;i++)	printf("%lf ",naomi[i]);printf("\n");
		//for(int i=0;i<n;i++)	printf("%lf ",ken[i]);printf("\n");
		
		int opt= findOptimal(naomi,ken,n);
		int dec = findDeceitful(naomi,ken,n);
		printf("Case #%d: %d %d\n",k,dec,opt);
	}
	return 0;
}
