#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	freopen("b1.in","r",stdin);
	freopen("b1.out","w",stdout);
	int T;
	cin>>T;
	for (int id=1;id<=T;id++)
	{
		int a,b,k;
		cin>>a>>b>>k;

		int sum=0;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				int temp=i&j;
				if (temp<k) sum++;
			}
		}
		cout <<"Case #"<<id<<": "<<sum<<endl;
	}
	return 0;
}