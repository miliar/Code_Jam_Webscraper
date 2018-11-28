#include <iostream>
#include <math.h>
using namespace std;

int main() {
	int i, j, N, T, tmp, flag, a[10];
	float k;
	cin >> T;
	for(i = 0; i < T; ++i)
	{
		for(j = 0; j < 10; ++j)
			a[j] = 0;
		cin >> N;
		for(k = 0; k < 1000000; ++k)
		{
			tmp = N * (k+1);
			flag = 1;
			while(tmp != 0)
			{
				a[tmp % 10] = 1;
				tmp /= 10;
			}
			for(j = 0; j < 10; ++j)
			{
				if(a[j] == 0)
					flag = 0;
			}
			if(flag == 1)
				break;
		}
		if(flag == 1)
			cout << "Case #" << i+1 << ": " << N*(k+1) << endl;
		else
			cout << "Case #" << i+1 << ": INSOMNIA\n";
    }
    return 0;
}