#include <iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=0; i<t;i++)
	{
		int n;
		cin>>n;
		int a[10] = {0};
		if(n == 0)
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		else
		{
			int j = 1;
			bool flag = false;
			int temp,result;
			while(flag == false)
			{
				temp = j * n;
				result = temp;
				// cout<<temp<<endl;
				while(temp > 0)
				{
					int d =  temp % 10;
					a[d] = 1;
					temp = temp/10;
					// cout<<temp<<endl;

				}
				flag = true;
				for(int k = 0;k<10;k++)
				{
					// cout<<a[k]<<" ";
					if(a[k] == 0)
						flag = false;
				}
				j++;

			}
			cout<<"Case #"<<i+1<<": "<<result<<endl;
		}
	}
}