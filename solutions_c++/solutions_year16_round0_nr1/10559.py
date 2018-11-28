#include<iostream>
#include<fstream>
using namespace std;

int check(int k,int a[])
{
int t=0;
while(k>0)
{
	int p=k%10;
	a[p]++;
	k=k/10;
}


for(int i=0;i<=10;i++)
{
	if(a[i]==0)
	{
		t++;
	}
}
return t;	
}


int main()
{
	
int t,n,k=0,countT=1;
cin>>t;
while(t--)
{
int lol;
	cin>>n;
	if(n==0)
	{
		cout<<"Case #"<<countT<<": INSOMNIA"<<endl;
	}
	else
	{
		int a[10]={0};
		for(int i=1;;i++)
		{
			k=n*i;
			lol=check(k,a);
			if(lol==0)
			{
				break;
			}
		}
		cout<<"Case #"<<countT<<": "<<k<<endl;
	}
	countT++;
}
return 0;
}
