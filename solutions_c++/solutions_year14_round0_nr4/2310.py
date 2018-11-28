#include<stdio.h>
#include<algorithm>
FILE *in=fopen("1.in","r");
FILE *out=fopen("1.out","w");
int cnt2,a,b1,b2,TT,Tcnt,cnt1,Bcnt,a1,a2;
double A[1005],B[1005];
int main()
{
	int N,i,j;
	fscanf(in,"%d",&TT);
	for(Tcnt=1;Tcnt<=TT;Tcnt++)
	{

		cnt2=cnt1=Bcnt=0;
		fscanf(in,"%d",&N);
		for(i=1;i<=N;i++)fscanf(in,"%lf",&A[i]);
		for(i=1;i<=N;i++)fscanf(in,"%lf",&B[i]);
		std::sort(A+1,A+1+N);
		std::sort(B+1,B+1+N);

		a=N;
		b1=1;
		b2=N;
		for(;a>=1;a--)
		{
			if(A[a]>B[b2])
			{
				cnt2++;
				b1++;
			}
			else b2--;
		}
		a=N;
		b1=1;
		b2=N;
		for(i=N;i>=1;i--)
		{
			if(A[i]>B[N])Bcnt++;
			else break;
		}
		j=1;
		for(i=1;i<=Bcnt;i++)
		{
			for(;j<=N;j++)
			{
				if(A[j]>B[i])
				{
					break;
				}
			}
			A[j]=100;
			B[i]=100;
			j++;
		}
		cnt1=Bcnt;
		std::sort(A+1,A+1+N);
		std::sort(B+1,B+1+N);
		N-=Bcnt;
		a1=1;
		a2=N;
		b1=1;
		b2=N;
		while(a1<=a2)
		{
			if(A[a2]>B[b2])
			{
				cnt1++;
				b2--;
				a2--;
			}
			else
			{
				a1++;
				b2--;
			}
		}
		fprintf(out,"Case #%d: %d %d\n",Tcnt,cnt1,cnt2);
	}
	return 0;
}