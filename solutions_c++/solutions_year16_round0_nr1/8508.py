#include<iostream>
using namespace std;

int main()
{
	long long int z,j;
cin>>z;

for(j=0;j<z;j++)
{
	long long int n,i,k=1,l,arr[10]={0},count=1,m,c=0,t=1;
	cin>>n;
	l=n;
	while(t==1)
	{
		m=n;
		count++;
		if(count==100)
			t=0;
//		cout<<n<<'\n';
		while(n>9)
		{
			int a=n%10;
			arr[a]=arr[a]+1;
			n=n/10;
		}
//		arr[n]=arr[n]+1;
//		for(i=0;i<10;i++)
//			cout<<arr[i]<<" ";
//		cout<<'\n';

	arr[n]=arr[n]+1;

		for(i=0;i<10;i++)
		{
//			cout<<arr[i]<<" ";
			if(arr[i]>0)
			{
				c=1;
			}
			else
			{
				c=0;
				break;
			}

		}

//		cout<<'\n';
//		cout<<c;
//		cout<<'\n';

	if(c==1)
		{
			break;
		}

		n=count*l;

	} 

	if(c==1)
		cout<<"Case #"<<j+1<<": "<<m<<'\n';
	else if(c==0)
		cout<<"Case #"<<j+1<<": INSOMNIA"<<'\n';
}

}
