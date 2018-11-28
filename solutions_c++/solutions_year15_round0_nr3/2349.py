#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int main()
{
	int mul[5][5],i,j,k;
	mul[1][1]=1;
	mul[2][2]=-1;
	mul[3][3]=-1;
	mul[4][4]=-1;
	mul[1][2]=mul[2][1]=2;
	mul[1][3]=mul[3][1]=3;
	mul[1][4]=mul[4][1]=4;
	mul[2][3]=4;
	mul[3][2]=-4;
	mul[2][4]=-3;
	mul[4][2]=3;
	mul[3][4]=2;
	mul[4][3]=-2;
	int p,mini,maxk,m,flag,f_i,f_j,t,l,a,b,c;
	long long x;
	int val[80000],valrev[80000];
	int X,I,J,K;
	char A[80000],B[80000];
	scanf("%d",&t);
	for(m=1;m<=t;m++)
	{
		scanf("%d %lld",&l,&x);
		scanf("%s",A);
		strcpy(B,A);
		X=1;
		for(i=0;i<strlen(A);i++)
		{
			a=A[i]-'g';
			if(X<0)
				val[i]=X=-1*mul[-1*X][a];
			else
				val[i]=X=mul[X][a];
		}
		p=0;
		flag=0;
		if(X==-1 && x%2 ==1)
			p=1;
		else if( (abs(X) == 2 || abs(X) ==3 || abs(X)==4) && x%4==2)
			p=1;
		if(p>0)
		{
			for(i=1;i<min(x,(long long)8);i++)
				strcat(A,B);
			X=1;
			mini=-1;
			maxk=0;
			for(i=0;i<strlen(A);i++)
			{
				a=A[i]-'g';
				if(X<0)
					val[i]=X=-1*mul[-1*X][a];
				else
					val[i]=X=mul[X][a];
				if(mini==-1 && X==2)
					mini=i;
			}
			for(i=0;i<strlen(A);i++)
			{
				if(val[i] == 4 && i>maxk && i<(strlen(A)-1))
				{
					if(x>4)
						maxk=i;
					else
						maxk=i;
				}
			}
			if(maxk>mini && (mini!=-1))
				flag=1;	
		}
		if(flag)
			printf("Case #%d: YES\n",m);
		else
			printf("Case #%d: NO\n",m);
	}
	return 0;
}
