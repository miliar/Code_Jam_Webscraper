# include<iostream>
using namespace std;
int main()
{
	int no,n,t,k,i,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		int a[2501]={0};
		cin>>n;
		for(i=1;i<=(2*n)-1;i++)
		{
			for(k=1;k<=n;k++)
			{
				cin>>no;
				a[no]++;
			}
		}
		cout<<"Case #"<<j<<": ";
		for(i=0;i<=2500;i++)
		{
			if(a[i]%2==0)
				a[i]=0;
			else cout<<i<<" ";
		}
		cout<<endl;
	}
	return 0;
}
