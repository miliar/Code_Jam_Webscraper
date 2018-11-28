#include<iostream>
using namespace std;
int A[10]={0,0,0,0,0,0,0,0,0,0};
//int flag0=0,flag1=0,flag2=0,flag3=0,flag4=0,flag5=0,flag6=0,flag7=0,flag8=0,flag9=0;
int flag=0;
int chkflag()
{	int i;
	for(i=0;i<10;i++)
	{
		if(A[i]==0)
			return 0;
	}
	return 1;
}
void flush()
{
	int i=0;
	for(i=0;i<10;i++)
		A[i]=0;
}
int main()
{	
	
	long long int i=1;
	long long int N,t,tmp,k,r,T;
	cin>>T;
	while(T--)
	{
		cin>>N;
		flush();
		flag=0;
		if(N==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA\n";
		}
		else
		{	
			k=1;
			while(flag==0)
			{	tmp=k*N;
				t=tmp;			
				while(t>0)
				{
					r=t%10;
					t=t/10;
					if(A[r]==0)
						A[r]=A[r]+1;
				}
				flag=chkflag();
				k++;
			}
			cout<<"Case #"<<i<<": "<<tmp<<"\n";
		}
		i++;
	}
	return 0;
}
	
		
