#include<iostream>
#include <fstream>
#include <string>
using namespace std;

ofstream fout("answer.out");
ifstream fin("B-small-attempt0.in");

int main()
{
	int number1, count1;
	fin >> number1;
	for (count1 = 1; count1 <= number1; count1++)
	{
		int A, B, K, count2, count3, count4 = 0, number2;
		fin >> A >> B >> K;
		for (count2 = 0; count2 < A; count2++)
		{
			for (count3 = 0; count3 < B; count3++)
			{
				number2 = count2&count3;
				//cout << number2;
				if (number2 < K)
				{
					//cout << count2 << " " << count3 << endl;
					count4++;
				}
			}
		}
		fout << "Case #" << count1 << ": " << count4 << endl;
	}
	return 0;
}