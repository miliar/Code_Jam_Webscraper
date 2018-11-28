//slow

#include <iostream>
#include <cstdio>
using  namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int a,b,c,d,i,j,t,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>a>>b>>c;
		d=0;
		for(i=0;i<a;i++)
			for(j=0;j<b;j++)
				if( (i&j) <c)
				{
	//				cout<<i<<" "<<j<<endl;
					d++;
				}
		cout<<"Case #"<<k<<": "<<d<<endl;
	}
	return 0;
}