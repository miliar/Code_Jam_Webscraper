#include <iostream>
#include<cstdio>
using namespace std;

int main() {
	int t,z,j,i;
	double c,f,x,temp1,temp2,ans;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>c>>f>>x;
		z=1;
		temp1=x/2;
		temp2=(c/2)+(x/(2+f));
		while(1)
		{
			if(temp1>temp2)
			{
				z++;
				temp1=temp2;
				temp2=0;
				for(j=0;j<z;j++)
				{
					temp2+=(c/(2+j*f));
				}
				temp2+=(x/(2+(z*f)));
			}
			else
			{
				ans=temp1;
				break;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		printf("%.7f\n",ans);
	}
	return 0;
}
