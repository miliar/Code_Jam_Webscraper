#include <fstream>
#include <iostream>
#include <math.h>

using namespace std;

int Pow10(long long pow);
int Digit(long long numb, long long pos);
bool IsPolyndrom(long long numb);
long long Sqrt(long long L);

int main()
{
	int T, A, B;
	fstream in("C-small-attempt0.in", ios::in);
	fstream out("out.out", ios::out);

	in >> T;

	for (int k = 0; k < T; k++)
	{
		int count = 0;
		in >> A >> B;
		for (long long i = A; i <= B; i++)
		{
			if (IsPolyndrom(i))
			{
				long long a = long long (pow(double(i), 0.5));
				if (a - pow(double(i), 0.5) == 0)
				if (IsPolyndrom(a))
					count++;
			}
		}
		out << "Case #" << k+1 << ": " << count << endl;
	}

	in.close();
	out.close();

	system("pause");
	return 0;
}

int Digit(long long numb, long long pos)		// pos = 1..n
{
	return (numb / (Pow10(pos-1))) % 10;
}

int Pow10(long long pow)
{
	if (pow == 0)
		return 1;
	int s;
	if (pow % 2 == 0)
		s = 1;
	else
		s = 10;

	if (pow == 1)
		return 10;
	else
		return s * Pow10(pow/2) * Pow10(pow/2);
}

bool IsPolyndrom(long long numb)
{
	long long digit = numb;
	long long length = 1;
	while (digit > 9)
	{
		length++;
		digit = numb / Pow10(length-1);	
	}

	for(int i = 0; i <= length / 2; i++)
	{
		if (Digit(numb, i+1) != Digit(numb, length - i))
			return 0;
	}

	return 1;
}

long long Sqrt(long long L)
{
	long long div = 1, rslt = 0; 
	while (L > 0)
	{
		L -= div,  div += 2; 
		rslt += L < 0 ? 0 : 1; 
	}
	return rslt; 
}