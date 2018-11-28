#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int t;
	double c,f,x,r,top,temp;
	int k=1;
	cin>>t;
	cin.precision(7);
	cout.precision(7);
	while(k<=t)
	{
			r=2.0000000;
			cin>>std::fixed>>c>>std::fixed>>f>>std::fixed>>x;
			top=double(x)/double(r);
			temp=0.0;
			while(top>=temp)
			{
				double i=2.0000000;
				while(i<=r)
				{
					
					temp+=double(c)/double(i);
					i=i+f;
				}
				temp+=double(x)/double((r+f));
				if(top>temp)
				{
					
					top=temp;
					r=r+f;
					temp=0;
				}
			}
			cout<<"Case #"<<k<<": "<<std::fixed<<top<<"\n";
			k++;
		}
}
			
			
