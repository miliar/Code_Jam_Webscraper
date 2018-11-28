/*
1 ¡Ü T ¡Ü 100.
1 ¡Ü A ¡Ü B ¡Ü 1000.
First large dataset
1 ¡Ü T ¡Ü 10000.
1 ¡Ü A ¡Ü B ¡Ü 1014.

long long 
da biao  10^7

Second large dataset
1 ¡Ü T ¡Ü 1000.
1 ¡Ü A ¡Ü B ¡Ü 10100.

gaojingdu


1 2 3 101 111 121 202 212 1001 1111 2002 10001 10101 10201 11011 11111 11211 20002 20102
*/

#include<iostream>
#include<cmath>

using namespace std;

int T;
double A,B;
int a,b,c,d;
int queue[30];
int p;
int tmp;
int ans;

bool check(long long x)
{
	int y[20];
	int e=0;
	
	while(x!=0)
	{
		e++;
		y[e]=x%10;
		x=x/10;	
	}
	for(int i=1;i<=e/2;i++)
		if(y[i]!=y[e+1-i]) return 0;
	return 1;
}
int main()
{
	freopen("in3.txt","r",stdin);
	freopen("out3.txt","w",stdout);
	scanf("%d",&T);
for(int w=1;w<=T;w++)
{
	p=21;
	queue[1]=1;queue[2]=2;queue[3]=3;queue[4]=11;queue[5]=22;
	queue[6]=101;queue[7]=111;queue[8]=121;queue[9]=202;queue[10]=212;
	queue[11]=1001;queue[12]=1111;queue[13]=2002;queue[14]=10001;queue[15]=10101;queue[16]=10201;queue[17]=11011;queue[18]=11111;
	queue[19] = 11211;queue[20] = 20002;queue[21] = 20102;
	
	scanf("%lf %lf",&A,&B);
	A=sqrt(A);B=sqrt(B);
	ans=0;
	for(int i=1;i<=p;i++)
	{
		if(queue[i]>=A && queue[i]<=B) ans++; 
	}
	printf("Case #%d: %d\n",w,ans);
}
	return 0;
}
