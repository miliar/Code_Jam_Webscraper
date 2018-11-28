#include <iostream>
using namespace std;

int main() {
	int t,r,c,a[4],b[4],q1,q2,z[4][4],i,f,j,q,d;
	cin>>t;
	for(d=1;d<=t;d++)
	{
		cin>>q1;
		for(r=0;r<4;r++)
		{
			for(c=0;c<4;c++)
				cin>>z[r][c];
		}
		for(r=0;r<4;r++)
			a[r]=z[q1-1][r];
		cin>>q2;
		f=0;
		j=0;
		for(r=0;r<4;r++)
		{
			f=0;
			for(c=0;c<4;c++)
			{	
				cin>>z[r][c];
				if(a[c]==z[r][c])
				{
					f++;
				}
			}
			if(f==4)
				j=1;
		}
		i=0;
		for(r=0;r<4;r++)
			b[r]=z[q2-1][r];
		for(r=0;r<4;r++)
		{
			for(c=0;c<4;c++)
			{
				if(a[r]==b[c])
				{	
					i++;
					q=c;
				}
			}
		}
		cout<<"Case #"<<d<<": ";
		if(i==0)
			cout<<"Volunteer cheated!"<<endl;
		else if(i==1)
			cout<<b[q]<<endl;
		else if(i>1)
			cout<<"Bad magician!"<<endl;
	}
	return 0;
}