#include <iostream>
#include <fstream>
#include <cmath>
//해석한 내용

//대칭수의 제곱근이 대칭수인 수.

using namespace std;


int checkPalindromes(int n)
{
	int temp = 0;
	int result = 0;
	int length = log10((double)n);

	temp = n;
	for(int i=0; i<=length; i++)
	{
		result = result * 10 + (temp % 10) ;
		temp = temp / 10;
	}

	if(result == n)
		return 1;

	return 0;
}

int main()
{
	int T;
	int A, B;
	int result;

	ifstream fin;
	ofstream fout;

	//fin = ifstream("C-small-attempt0.in");
	//fout = ofstream("output.txt");
	fin = ifstream(stdin);
	fout = ofstream(stdout);

	fin>>T;

	for(int count=1; count<=T; count++)
	{
		result = 0;
		fin>>A>>B;

		for(int i=A; i<=B; i++)
		{
			if(checkPalindromes(i))
			{
				double temp = sqrt((double)i);

				if( temp - (double)((int)temp) == 0 && checkPalindromes(temp))
				{
					result ++;
				}
			}
		}

		fout << "Case #" << count << ": " << result << endl;
	}

	return 0;
}