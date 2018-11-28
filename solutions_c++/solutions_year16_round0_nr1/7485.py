#include<bits/stdc++.h>
using namespace std;

long long int n;



int main()
{
	int T;
	scanf("%d",&T);
	int t;
	ofstream o("program3data.txt");
	for(t=0;t<T;t++)
	{
int f[10]={0};
			
		cin>>n;long long int c=2,ans=0,n1=n;
		if(n==0)
		{
			cout<<"Case #"<<t+1<<": "<< "INSOMNIA"<<"\n";
		o<<"Case #"<<t+1<<": "<<"INSOMNIA"<<"\n";
		continue;
		}
		while(1)
		{
			int g=n,j=1,i;
			while(g!=0)
			{
				f[g%10]=1;
				g/=10;
			}//cout<<n;
			for(i=0;i<10;i++)
			{
		if(f[i]==0)
		j=0;}
			if(j==1)
			{
			ans=n;//cout<<n<<endl;
			break;}
			else
			{
			n=n1*c;c++;}
		}
		
		
		
		
		cout<<"Case #"<<t+1<<": "<< ans<<"\n";
		o<<"Case #"<<t+1<<": "<< ans<<"\n";
	}
	return 0;
}
