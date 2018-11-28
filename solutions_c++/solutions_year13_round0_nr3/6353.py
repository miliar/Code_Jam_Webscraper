#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>

using namespace std;

int main ()
{
	int T, digit, num;
	ifstream infile;
	ofstream outfile;
	infile.open("C-small-attempt0.in");
	outfile.open("Result.txt");
	infile >> T;
	for (int count = 0; count < T; count++)
	{
		int start, end, total = 0;
		infile >> start;
		infile >> end;
		for (int i = start; i <= end; i++)
		{
			int rev = 0;
			bool isPal = false, isSq = false;
			num = i;
			do
			{
			digit = num % 10;
			rev = (rev*10) + digit;
			num = num/10;
			 }while (num != 0);
			if (i == rev)
				isPal = true;
			int root = (sqrt(i));
			if (root * root == i)
				isSq = true;
			rev = 0;
			num = root;
			bool isRootPal = false;
			do
			{
			digit = num % 10;
			rev = (rev*10) + digit;
			num = num/10;
			 }while (num != 0);
			if (root == rev)
				isRootPal = true;
			if (isPal == true && isSq == true && isRootPal == true)
				total ++;
		}
		outfile << "Case #" << count + 1 << ": " << total;
		outfile << '\n';
	}
	infile.close();
	outfile.close();
}