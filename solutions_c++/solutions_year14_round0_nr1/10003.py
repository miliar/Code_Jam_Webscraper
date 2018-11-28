#include<iostream>
using namespace std;
int main()
{
	int get();
	int T,i;
	cin>>T;
	int a[T];
	for(i=0;i<T;i++)
	  a[i]=get();
	for(i=0;i<T;i++)
	{
		cout<<"Case #"<<(i+1)<<": ";
		if(a[i]==-1)
		  cout<<"Bad magician!"<<endl;
		else if(a[i]==-2)
		  cout<<"Volunteer cheated!"<<endl;
		else
		  cout<<a[i]<<endl;
	}
	return 0;
}
int get()
{
	int c1,c2,a1[4],a2[4],i,j,n,x=0;
	cin>>c1;
	for(i=0;i<16;i++)
	{
		cin>>n;
		if(i>=((c1-1)*4)&&x<4)
			a1[x++]=n;
	}

	cin>>c2;
	x=0;
	 for(i=0;i<16;i++)
	{
		cin>>n;
		if(i>=((c2-1)*4)&&x<4)
			a2[x++]=n;
	}
	x=0;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(a1[i]==a2[j])
			{
				x++;
				n=a1[i];
			}
		}
	}
	if(x==1)
		return n;
	else if(x==0)
		return -2;
	else
		return -1;
}