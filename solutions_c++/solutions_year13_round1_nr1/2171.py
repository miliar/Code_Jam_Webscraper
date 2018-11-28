#include<iostream.h>
#include<conio.h>
void main()
{
	int t,r,m,n;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>r>>m;
		for(int s=1;s<=m;s++)
		{
			int temp;
			temp=s*(2*r+2*s-1);
			if(temp>m)
				break;
		}
		cout<<"Case #"<<i+1<<":"<<s-1<<endl;
	}
}
