#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int* itoarray(int num)
{
    int len = log(num)/log(10) + 1;
    int* arr = new int[len];

    for (int i = 0; i < len; ++i)
    {
	int digit = num / pow(10, len-i-1);
//	DBG << digit << " ";
	arr[i] = digit;
	num = num - digit * pow(10, len-i-1);
    }
//    DBG << endl;

    return arr;
}

bool checkPalin(int num)
{
    int len = log(num)/log(10) + 1;
    int* arr = new int[len];

    for (int i = 0; i < len; ++i)
    {
	int digit = num / pow(10, len-i-1);
//	DBG << digit << " ";
	arr[i] = digit;
	num = num - digit * pow(10, len-i-1);
    }
//    DBG << endl;

    for (int i = 0; i < len/2; ++i)
    {
	if (arr[i] != arr[len-i-1])
	    return false;
    }
    return true;
}

bool checkSquare(int num)
{
    int s = sqrt(num);
    if (s*s == num && checkPalin(s) == true)
	return true;
    else
	return false;
}

int main()
{
//    ifstream fin("input.txt", ios::in);
    ifstream fin("C-small-attempt0.in", ios::in);
//    ifstream fin("C-large.in", ios::in);
    ofstream fout("output.txt", ios::out);

    int T, A, B;
    fin >> T;

    int found;
    for (int t = 0; t < T; ++t)
    {
	found = 0;
	fin >> A >> B;

	for (int n = A; n <= B; ++n)
	{
	    if (checkSquare(n) == true && checkPalin(n) == true)
	    {
//		cout << n << endl;
		++found;
	    }
	}
//	cout << endl;
	
	fout << "Case #" << t+1 << ": " << found << endl;;
    }
}
