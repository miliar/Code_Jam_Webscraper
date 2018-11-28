#include <iostream>
#include <algorithm>
using namespace std;
double a[1005],b[1005];
int main()
{
	int t,x,y;
	cin>>t;
	for (int i=0;i<t;++i)
	{
		cin>>x;
		for (int j=0;j<x;++j)
			cin>>a[j];
		for (int j=0;j<x;++j)
			cin>>b[j];
		sort(a,a+x);
		sort(b,b+x);
		int c=0;
		bool t=true;
		for (int j=0;j<x-c;++j)
			if (a[c+j]<b[j])
			{
				t=false;
				break;
			}
		while (!t && c<x)
		{
			c++;
			t=true;
			for (int j=0;j<x-c;++j)
				if (a[c+j]<b[j])
				{
					t=false;
					break;
				}
		}
		cout<<"case #"<<i+1<<": "<<x-c<<' ';
		int j=0,k=0;c=0;
		while (k<x)
		{
			while (b[k]<a[j] && k<x) k++;
			if (k<x) c++;
			j++;k++;
		}
		cout<<x-c<<endl;
	}
}
