#include "iostream"
#include "stdio.h"
using namespace std;
int counter()
{
	string input,A,C;
	int x = 0;
	cin >> input;
	char B=input[0];
	for (int i = 1; i < input.size(); ++i)
	{

		if (input[i]>=B)
		{
			B=input[i];
			A+=input[i];
			x++;
		}
		else
		{
			C+=input[i];
		}
	}
	for (int i = A.size()-1; i >= 0; --i)
	{
		printf("%c",A[i] );
	}
	cout << input[0]+C;
	return 0;
}
int main(int argc, char const *argv[])
{
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		cout << "Case #"<< i+1 <<": ";
		counter();
		cout << endl;
	}
	return 0;
}