#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>
#include <vector>

using namespace std;

int main() {
	ofstream ofile;
	ofile.open("./A.out");
	ifstream ifile;
	ifile.open("./A-small-attempt0.in");
	int t, k = 0, sum;
	long long num, n, temp;
	ifile >> t;
	while(k < t)
	{
		ifile >> num;
		if(num == 0)
					ofile << "Case #" << k + 1 << ": INSOMNIA\n";
		else
		{
			bool count[10] = {false};
			n = num;
			while(1)
			{
				sum = 0;
				temp = n;
				while(temp > 0)
				{
					count[temp % 10]  = true;
					temp /= 10;
				}
				for(int i = 0; i < 10; ++i)
					sum += count[i];
				if(sum == 10)
					break;
				n += num;
			}
			ofile << "Case #" << k + 1 << ": " << n << "\n";
		}
		k++;
	}
	ifile.close();
	ofile.close();

	return 0;
}