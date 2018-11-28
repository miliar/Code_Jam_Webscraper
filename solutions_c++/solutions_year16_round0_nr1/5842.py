#include <iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int i = 1;
	while(t--)
	{
		int arr[10] = {0};
		long int n;
		long int sum = 0;
		cin>>n;
		if(n == 0)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
		else
		{
			int j =1;
			while(sum != 10)
			{
				int temp = n * j;
				while(temp != 0)
				{
					int x = temp%10;
					temp = temp/10;
					if(arr[x] == 0)
					{
						arr[x] = 1;
						sum++;
					}
				}
				j++;
			}
			cout<<"Case #"<<i<<": "<<(j-1)*n<<endl;
		}
		i++;
	}
	return 0;
}