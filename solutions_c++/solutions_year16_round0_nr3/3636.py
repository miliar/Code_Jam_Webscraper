#include <fstream>
#include <cmath>
#include <iostream>

using namespace std;

ifstream f1("in.in");
ofstream f2("out.out");

int v[16], c=0, n, lc;
long long d[11];

long long putere(long long a, long long b)
{
	long long result = a;
	for (int i = 1; i<b; i++)
		result = result * a;
	return result;
}

long long prim(long long n)
{
	for (int i = 2; i <= sqrt(n); i++)
		if (n%i == 0)
			return i;

	return 0;
}

bool valid()
{
	if (v[0] != 1 || v[n - 1] != 1)
		return false;

	long long number;

	for (int i = 0; i<11; i++)
		d[i] = 0;

	for (int b = 2; b <= 10; b++)
	{
		number = 0;
		for (int i = 1; i<n; i++)
		{
			long long prod = number + (long long) v[i] * putere((long long) b, (long long) i);
			number = prod;
		}
		number ++;
		long long div = prim(number);
		if (div == 0)
			return false;
		else
			d[b] = div;
	}

	return true;
}

void afiseaza()
{
    for(int i=n-1; i>=0; i--)
        f2 << v[i];
    f2 << " ";
    for(int i=2;i<=10;i++)
    {
        f2 << d[i];
        if(i!=10)
            f2<< " ";
    }
    f2<<"\n";
}

void backtrack()
{
    int k=0;
    v[k]=-1;
    while(k>=0)
    {
        while(v[k]<1)
        {
            v[k]++;
            if(k == n-1)
            {
                if(valid())
                {
                    afiseaza();
                    c++;
                    if(c==lc)
                        return;
                }
            }
            else
            {
                k++;
                v[k]=-1;
            }

        }
        k--;
    }

}

int main()
{

    f2 << "Case #1:\n";
    f1 >> n;
    f1 >> n >> lc;

    backtrack();

    f1.close();
    f2.close();

    return 0;
}
