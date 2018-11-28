#include<iostream>

using namespace std;

int N, digits[10];
int nl = 0;

unsigned int CheckDigit(unsigned int elem)
{
	int cnt = 1;
	while(1)
	{
		int mul = cnt * elem;
		int tmul = mul;
		while(mul != 0)
		{
			int rem = mul%10;
			mul = mul/10;
			if (digits[rem] == 0)
			{
				nl++;
				digits[rem] = 1;
				if (nl == 10)
				{
//					cout << elem << " : " << cnt << endl;
					return tmul;
				}
			}
		}
		cnt++;
	}
}


int main()
{
	cin >> N;
	unsigned int elem;
	for (int i = 0; i < N; i++)
	{
		cin >> elem;
		if (elem == 0)
			cout << "Case #"<<i+1<<": INSOMNIA"<<endl;
		else
		{
			unsigned int ans = CheckDigit(elem);
			cout << "Case #"<<i+1<<": "<< ans <<endl;
		}
		for (int j = 0; j < 10; j++) digits[j] = 0;
		nl = 0;
	}
	return 0;
}


