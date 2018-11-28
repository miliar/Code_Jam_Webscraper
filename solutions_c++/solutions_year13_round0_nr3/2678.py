#include <fstream>
using namespace std;

int T;
long long int A,B;

bool palindrome(long long int num)
{
	int digits[100];
	int idx = 0;
	while (num != 0)
	{
		digits[idx] = num%10;
		num /= 10;
		idx++;
	}
	for (int i = 0; i < floor(idx/2); i++)
		if (digits[i] != digits[idx-1-i])
			return false;
	return true;
}

void main()
{
	ifstream fin;
	ofstream fout;
	fin.open("C-small-attempt0.in");
	fout.open("2.txt");
	fin >> T;
	for (int i = 0; i < T; i++)
	{
		fin >> A >> B;
		long long int a,b;
		a = ceil(sqrt(A));
		b = floor(sqrt(B));
		long long int count = 0;
		for (int j = a; j <=b; j++)
		{
			long long int c = j*j;
			if(palindrome(j) && palindrome(c))
				count++;
		}
		fout << "Case #" << i+1 << ": " << count << endl;
	}
	fin.close();
	fout.close();
}