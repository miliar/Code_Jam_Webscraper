#include <iostream>
#include <fstream> 

using namespace std;
 
int main()
{
	int testCases;
	int arr[10];
	int input;

	ofstream out;
	out.open ("C:\Users\kim\Desktop\output.txt");
	ifstream in;
	in.open("A-small-attempt1.in");
 
	in >> testCases;
 
	for (int i = 0; i < testCases; i++)
	{
		in >> input;
		out << "Case #" << i + 1 << ": ";
 
		if (input == 0)
			out << "INSOMNIA" << "\n";
		else
		{
			long long mul;
			int divTmp, p = 0;
 
			memset(arr, 0, sizeof(arr));
 
			for (int j = 0; ; j++)
			{
				mul = (j + 1)*input;
 
				for (long long tmp = mul; ; )
				{
					divTmp = tmp % 10;
 
					if (arr[divTmp] == 0)
						arr[divTmp] = 1;
					tmp = tmp / 10;

					if (tmp == 0)
						break;
				}

				for (p; p < 10; p++)
				{
					if (arr[p] != 1)
						break;
				}
 
				if (p == 10)
				{
					out << mul << "\n";
					break;
				}
				else
					p = 0;
			}
		}
	}
}