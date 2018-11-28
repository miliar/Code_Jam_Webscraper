#include <iostream>
#include <vector>

using namespace std;

int T;

long long pow(long long a, long long b)
{
	if(b==0)
		return 1;
	if(b==1)
		return a;
	long long res = pow(a,b/2);
	res *= res;
	if(b%2)
		res *= a;
	return res;
}

int main()
{
	cin >> T;
	for(int i=0;i<T;i++)
	{
		long long k,c,s;
		cin >> k >> c >> s;
		cout << "Case #" << i+1 << ":";
		for(long long j=0;j<s;j++)
		{
			cout << " " << 1+pow(k,c-1)*j;
		}
		cout << endl;
	}
}
