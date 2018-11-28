#include <iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int cno = 1;
	while(t--)
	{
		int a,b,k;
		cin>>a>>b>>k;
		int count = 0;
		for(int i=0;i<a;i++)
			for(int j=0;j<b;j++)
			{
				int num = i&j;
				if(num>=0 && num < k)
					count++;
			}

		cout<<"Case #"<<cno<<": "<<count<<endl;
		cno++;
	}
}