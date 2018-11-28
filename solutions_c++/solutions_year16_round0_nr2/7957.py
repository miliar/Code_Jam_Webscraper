#include<iostream>
using namespace std;

int main()
{
	int n,count=0;
	cin>>n;
	for (int c=1;c<=n;c++)
	{
		int k=0;
		char st[105] ;
		cin>>st;
		char t=st[0];
		while (st[k])
		{
			if (st[k]!=t)
			{
				for (int z=0;z<k||z==0;z++)
					if (st[z]=='-')
						st[z]='+';
					else
						st[z]='-';
				count++;
				t=st[0];
			}
			k++;
		}
		if (t=='-')
		{
			count++;
			for (int z=0;z<k;z++)
				if (st[z]=='-')
						st[z]='+';
					else
						st[z]='-';
		}

		cout<<"Case #"<<c<<": "<<count<<endl;
		count=0;
	}
	return 0;
}