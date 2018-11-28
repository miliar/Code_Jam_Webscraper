#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >>t;
	for(int i =1; i<= t; i++)
	{
		long long a, b, k;
		cin >>a >> b >> k;
		long long res =0;
		for(long j =0;j < a; j ++)
		{
			for (long s =0; s < b; s++)
			{
				if( (j&s) < k) res ++;
			}
		}
		cout<<"Case #"<<i<<": "<<(long long)res<<endl;
	}
	return 0;
}