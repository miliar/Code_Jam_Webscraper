#include<bits/stdc++.h>
using namespace std;
#define LL long long
 
bool prime(LL n,LL *div,int j)
{
	for(LL i=2;i<=sqrt(n);i++)
	{
		if(n%i==0)
		{
			div[j]=i;
			return false;
		}
	}
	return true;
}

 
int check(char *A,int n)
{
	int i,status=0;
	LL int b[50]={0};
	LL int div[50];
 	int len = strlen(A);
	for(int j=2;j<=10;j++)
	{
		b[j]=0;
		div[j]=0;
		LL val = 1;
		for(int i=0;i<len;i++)
		{
			b[j]+=(val*(A[len-i-1]-'0'));
			val *= j;
		}
		LL int a;
		if(prime(b[j],div,j))
			return false;
	}
		cout<<A<<" ";
		for(i=2;i<=10;i++)
			cout<<div[i]<<" ";
 
		cout<<endl;
		return true;	
}
 
void generateCoins(char *A,int n,int j,int *count,int index)
{
	if(*count==j)
		return;
	if(index==n-1)
	{
		if(check(A,n))
			(*count)++;
		return;
	}
	A[index]='0';
	generateCoins(A,n,j,count,index+1);
	A[index]='1';
	generateCoins(A,n,j,count,index+1);
}
 
int main()
{
 
	int i,T,N,J;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T>>N>>J;
	cout<<"Case #1:\n";
	int count = 0;
	int index=1;
	char A[N+1];
	for(i=0;i<N;i++)
		A[i]='0';
	A[i]='\0';
	A[0]=A[N-1]='1';
	generateCoins(A,N,J,&count,index);
	return 0;
}