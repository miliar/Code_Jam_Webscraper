#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
	int t, count;
	long long a, b, p, num;
	cin >> t;
	for(int c=1; c<=t; c++)
	{
		scanf_s("%lld %lld", &a, &b);
		num=static_cast<long long>(floor(sqrt(static_cast<double>(b))));
		b=num;
		num=static_cast<long long>(ceil(sqrt(static_cast<double>(a))));
		a=num;
		count=0;
		for(; a<=b; a++)
		{
			num=a;
			p=0;
			while(num!=0)
			{
				p=(p*10)+(num%10);
				num=static_cast<long long>(floor(static_cast<double>(num/10)));
			}
			if(a!=p)
				continue;
			num=static_cast<long long>(pow(static_cast<double>(a),2));
			p=0;
			while(num!=0)
			{
				p=(p*10)+(num%10);
				num=static_cast<long long>(floor(static_cast<double>(num/10)));
			}
			if(p==pow(static_cast<double>(a),2))
				count++;
		}
		cout << "Case #" << c << ": " << count << endl;
	}
	return 0;
}