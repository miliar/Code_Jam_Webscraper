#include <iostream>
#include <string>
#include <fstream>
#include <math.h>

using namespace std;

bool palindromo(int n)
{
	int dig[9];
	int cant = 0;
	while(n > 0)
	{
		dig[cant] = n % 10;
		cant++;
		n /= 10;
	}
	for(int i = 0; i < cant / 2; i++)
		if(dig[i] != dig[cant - i - 1])
			return false;
	return true;
}

int cantRes(int tope)
{
	int res = 0;
	float lim = sqrt(tope);
	for(int i = 1; i <= lim; i++)
	{
		if(palindromo(i) && palindromo(i*i))
			res++;
	}
	return res;
}

int main()
{
	ifstream fin("c-s.in");
	//ifstream fin("in.txt");
	ofstream fout("c-s.out");
	
	int t;
	fin >> t;
	
	for(int s = 0; s < t; s++)
	{
		int a, b;
		fin >> a >> b;
		fout << "Case #" << s+1 << ": " << cantRes(b) - cantRes(a-1) << endl;
	}
	
	return 0;
	
}
