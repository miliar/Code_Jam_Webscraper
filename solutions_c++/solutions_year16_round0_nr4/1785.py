#include <iostream>
using namespace std;

int main()
{
	int T;
	unsigned long long int K,C,S,p;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		cout << "Case #" << t << ": ";
		cin >> K >> C >> S;
		p=1;
		for(int i=1;i<C;i++)
			p*=K;
		for(int i=0;i<K;i++)
			cout << (i*p+1) << " ";
		cout << endl;
	}

	return 0;
}

