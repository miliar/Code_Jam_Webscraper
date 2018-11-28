#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("1l.out","w",stdout);
	int t,*A,i,max,sum,count,n;
	char C[1000];
	cin>>t;
	n=t;
	while(t--)
	{
		sum=0;
		count=0;
		cin>>max;
		A=new int[max+1];
		cin>>C;
		for(i=0;i<max+1;i++)
		{
			A[i]=C[i]-48;
			if(i>sum)
			{
				count++;
				//cout<<i<<"---"<<sum<<endl;
				sum++;
			}
			sum=sum+A[i];
		}
		cout<<"Case #"<<n-t<<": "<<count<<endl;
	}
}
