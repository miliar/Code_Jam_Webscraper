#include <iostream>

using namespace std;

bool ehPal(long long int a)
{
	long long int invertido;
	long long int back = a;

	for(invertido = 0; back != 0; back /= 10)
	{
		invertido = 10*invertido + back%10;
	}

	return (invertido == a);

}

int main()
{
	int n, count = 0;
	cin >> n;
	while(count < n)
	{
		count++;
		long long int a, b;
		cin >> a >> b;
		long long int resp = 0;
		long long quad = 1;
		for(long long int i = 1; quad <= b; i++, quad = i*i)
		{
			if( ehPal(i) && ehPal(quad) &&  quad >= a)
			{
				resp++;
			}
		}
		cout << "Case #"<<count<<": " << resp << endl;
	}
	return 0;
}
