#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);

	for(int i=1;i<=t;i++)
	{
		int n;
		bool arr[10];
		for(int i=0;i<10;i++)
			arr[i] = false;

		scanf("%d",&n);

		if(n==0)
		{	
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}

		bool flag = true;
		int k=1;

		int copy;int copy2;
		while(flag)
		{
			copy = n*k;
			copy2=copy;
			while(copy != 0)
			{
				int d = copy%10;
				arr[d] = true;
				copy = copy/10;
			}

			bool abc = false;
			for(int i=0;i<10;i++)
			{
				if(arr[i] == false)
					abc = true;
			}
			flag = abc;
			k++;
		}

		cout<<"Case #"<<i<<": "<<copy2<<endl;
	}
}