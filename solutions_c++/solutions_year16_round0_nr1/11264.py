#include <iostream>
#include <map>

using namespace std;

int main()
{
	int t,n;
	cin>>t;
	for(int i = 1;i <= t;i++)
	{
		map<int,bool> num_count;
		int count = 0;
		cin>>n;
		int dig;
		if(n == 0)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		int o_num = n;
		int copy_n;
		int times = 2;
		int done = false;
		while(n <= 1000000)
		{
			while(n!=0)
			{
				dig = n%10;
				n /= 10;
				if(num_count.find(dig) == num_count.end())
				{
					num_count[dig] = true;
					count++;
				}
			}
			if(count != 10)
			{
				n = o_num * times;
				copy_n = n;
				times++;
			}
			else
			{
				cout<<"Case #"<<i<<": "<<copy_n<<endl;
				done = true;
				break;
			}
		}
		if(!done)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
	}
	return 0;
}