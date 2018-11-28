#include <iostream>
using namespace std;

int main()
{
	int t, cases = 1;
	cin >> t;
	while(t--)
	{
		int exist[10];
		for(int i = 0; i < 10; i++)
			exist[i] = 0;
		int n, s = 1;
		cin >> n;
		cout << "Case #" << cases++ << ": "; 
		if(n == 0)
		{
			cout << "INSOMNIA\n";
			continue;
		}
		while(1)
		{
			int x = s * n;
			while(x)
				exist[x % 10] = 1, x /= 10;
			int a = 1;
			for(int i = 0; i < 10; i++)
				a = a & exist[i];
			//cout << s * n << endl;
			if(a) break;
			else s++;
		}
		cout << s * n << endl;
	}

}