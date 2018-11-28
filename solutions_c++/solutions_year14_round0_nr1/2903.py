//Sat Apr 12 08:45:39 IST 2014
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

int main()
{
	int t;S(t);int i;
	for(i=1;i<=t;i++)
	{
		int j,k,ans1,ans2,m1[4][4],m2[4][4];
		int marked1[17],marked2[17];
		for(j=0;j<17;j++)
			marked1[j]=marked2[j]=0;
		S(ans1);
		for(j=0;j<4;j++) for(k=0;k<4;k++) scanf("%d",&m1[j][k]);
		for(j=0;j<4;j++) marked1[m1[ans1-1][j]]=1;
		
		S(ans2);
		for(j=0;j<4;j++) for(k=0;k<4;k++) scanf("%d",&m2[j][k]);
		for(j=0;j<4;j++) marked2[m2[ans2-1][j]]=1;
		int count=0;int ans=0;
		for(j=0;j<17;j++)
			if(marked1[j]==1 && marked2[j]==1)
			{
				count++;
				ans = j;
			}
		if(count == 1)
			printf("Case #%d: %d\n",i,ans);
		else if(count > 1)
			printf("Case #%d: Bad magician!\n",i);
		else if(count == 0)
			printf("Case #%d: Volunteer cheated!\n",i);
	}
	return 0;
}