#include <iostream>
bool visited[10];
int main()
{
	long long t, n;
	std::cin >> t;
	for(int i = 0;i < t;++ i)
	{
		bool ok = false;
		long long mul = 0;

		for(int j = 0;j < 10;++ j)
			visited[j] = false;
		std::cin >> n;
		if(n == 0)
		{
			std::cout << "Case #" << i+1 << ": INSOMNIA\n";
			continue;
		}

		while(!ok)
		{
			mul ++;
			long long n2 = n * mul;
			while(n2 != 0)
			{
				visited[n2 % 10] = true;
				n2 /= 10;
			}
			ok = true;
			for(int j = 0;j < 10;++ j)
			{
				if(!visited[j])
				{
					ok = false;
					break;
				}
			}
		}
		std::cout << "Case #" << i+1 << ": " << n*mul << '\n';
	}
	return 0;
}
