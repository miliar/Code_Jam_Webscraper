# include<iostream>
using namespace std;
int main()
{
	freopen("input_file_name.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int t,x,ar[10],i,j,p,rem;
	long long n,nm,num;
	cin>>t;
	x=t;
	while(t--)
	{
		cin>>n;
		if(n==0)
		{
				cout<<"Case #"<<x-t<<": "<<"INSOMNIA"<<"\n";
				continue;
		}
		for(i=0;i<10;i++)
			ar[i]=0;
		for(j=1;;j++)
		{
			nm=j*n;
			//cout<<"nm:"<<nm<<"\n";
			num=nm;
//		if(nm==91)
//		{
//			for(i=0;i<10;i++)
//			cout<<ar[i];
//			break;
//		}
			while(num>0)
			{
			//	cout<<"num:"<<num<<"\n";
				rem=num%10;
				num=num/10;
				if(ar[rem]==1)
					continue;
				else
					ar[rem]=1;
					p=1;				
				for(i=0;i<10;i++)
				{	
					if(ar[i]==0)
				    {
						p=0;
						break;
					}
				}
				if(p)
				goto pm;	
			}
		}
		pm:
		cout<<"Case #"<<x-t<<": "<<nm<<"\n";
	}
	return 0;
}
