#include <iostream>
using namespace std;
int main()
{
	freopen ("codejam1.txt", "r", stdin);
	unsigned long T;
	cin>>T;

	for(int i = 1; i<=T;i++)
	{
		unsigned long N;
		cin>>N;
		unsigned long l = 0;
		unsigned long F;
		int arr[10] = {0,0,0,0,0,0,0,0,0,0};
		int count = 0;
		while(1)
		{
			int K = ++l *N;
			F = K;
			if(K == 0 || l>100)
			{
				F = 0;
				break;
			}
			while(K)
			{
				if(arr[K%10] == 0)
				{
					arr[K%10] = 1;
					count++;
					if(count == 10)
						break;
				}
				K = K/10;
			}
			if(count == 10)
				break;
		}
		cout<<"Case #"<<i<<": ";
		if(N)
			cout<<F<<endl;
		else
			cout<<"INSOMNIA"<<endl;
	}
	return 0;
}