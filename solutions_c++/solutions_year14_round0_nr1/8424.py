#include <iostream>
#include <cstdio>
using namespace std;
int main() 
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	ios_base::sync_with_stdio(false);
	int t,x,y,a[5],b[5],i,j,c,f;
	cin>>t;
	for(j=1;j<=t;j++)
		{
			int m[20]={0};
			cin>>x;
			x--;
			for(i=0;i<16;i++)
				{
					if((i/4)==x)
						{cin>>a[i%4];
						 m[a[i%4]]=1;
						}
					else cin>>y;
				}
			c=0;
			cin>>x;
			x--;
			for(i=0;i<16;i++)
				{
					if((i/4)==x)
						{cin>>b[i%4];
						 if(m[b[i%4]]==1)
							{c++;f=b[i%4];}
						}
					else cin>>y;
				}
			cout<<"Case #"<<j<<": ";
			if(c==0)
				cout<<"Volunteer cheated!";
			if(c==1)
				cout<<f;
			if(c>1)
				cout<<"Bad magician!";
			cout<<"\n";
			/*
			for(i=0;i<4;i++)
				cout<<a[i]<<",";
			cout<<"\n";
			for(i=0;i<4;i++)
				cout<<b[i]<<",";
			cout<<"\n";
			for(i=0;i<16;i++)
				cout<<m[i]<<",";
			cout<<"\n"<<c;
			
			cout<<"\n\n";
			*/
		}
	
	return 0;
}
