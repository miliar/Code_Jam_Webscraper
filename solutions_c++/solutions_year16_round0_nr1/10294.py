#include<bits/stdc++.h>
#define loop(x, n) for(int x = 0; x < n; ++ x)
using namespace std;

int a_evr[10],a_cntr=0,sum=0;
bool flag=false;

void no_digits(int num)
{
	int temp[8],cnt=0,j=0;
	sum=0;
	//cout<<"\n";
	while(num!=0)
	{
		temp[cnt]=num%10;
		loop(a_cntr,10)
		{
			if(a_evr[a_cntr]==temp[cnt])
				a_evr[a_cntr]=-1;
		}
		cnt++;
		num=num/10;
	}
	loop(a_cntr,10)
	{
	//	cout<<"\t"<<a_evr[a_cntr];
		sum=sum+a_evr[a_cntr];
		if(sum==-10)
			flag=true;
	}
}
main()
{
	FILE *fout = freopen("output.txt", "w", stdout);
	int t,i=1,t_cntr=0;
	long int n,n_temp;

	cin>>t;
	while(t--)
	{
		i=1;
		flag=false;
		t_cntr++;
		loop(a_cntr,10) 
		{
			a_evr[a_cntr]=a_cntr;
		}
		cin>>n;
		if(n!=0)	
		{
			while(flag==false)
			{
			n_temp=(i)*n;
			no_digits(n_temp);
			i++;
			}
			cout<<"Case #"<<t_cntr<<": "<<n_temp<<"\n";
		}	
		else cout<<"Case #"<<t_cntr<<": "<<"INSOMNIA\n";
	}
	exit(0);
}
