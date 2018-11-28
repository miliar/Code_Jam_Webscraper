#include <iostream>
using namespace std;

int main() {
	int n,f[10]={0},flag=0,t=0,i=1,m=1,tc,ic=1,j;
	cin>>tc;
	while(tc--)
	{
	 flag=0; t=0;i=1;m=1;
	 for(j=0;j<10;j++)
	 	f[j]=0;
	cin>>n;
	m=n;
	if(n==0)
	{
	    cout<<"Case #"<<ic<<": "<<"INSOMNIA"<<"\n";
	    ic++;
	    continue;
	}
	do
	{
		while(m!=0)
		{
			t=m%10;
			f[t]++;
			m=m/10;
		}
		if(f[0]>0&&f[1]>0&&f[2]>0&&f[3]>0&&f[4]>0&&f[5]>0&&f[6]>0&&f[7]>0&&f[8]>0&&f[9]>0)
		{
			flag=1;
		}
		else
		{
			i++;
			m=1;
			m=i*n;
		}
	}while(flag==0);
	m=1;
	m=i*n;
	cout<<"Case #"<<ic<<": "<<m<<"\n";
	ic++;
	}
	return 0;
}
