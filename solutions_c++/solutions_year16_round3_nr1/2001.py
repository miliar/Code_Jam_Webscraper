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
	int t, tt, n, i;
	tt = 0;
	ifile >> t;
	int max, maxNum1, maxNum2, sum;
	char name;
	while(tt < t)
	{
		ifile >> n;
		vector<int> s(n);
		sum = 0;
		for(i = 0; i < n; ++i)
		{
			ifile >> s[i];
			sum += s[i];
		}
		ofile << "Case #" << tt + 1 << ": " ;
		while(sum)
		{
			max = 0;
			for(i = 0; i < n; ++i)
			{
				if(s[i] > max)
				{
					max = s[i];
					maxNum1 = i;
					maxNum2 = -1;
				}
				else if(s[i] == max)
				{
					if(maxNum2 != -1)
						maxNum2 = -1;
					else
						maxNum2 = i;
				}
			}
			if(maxNum2 != -1)
			{
				name = 'A' + maxNum1;
				ofile << name;
				name = 'A' + maxNum2;
				ofile << name << " ";
				s[maxNum1]--;
				s[maxNum2]--;
				sum -= 2;
			}
			else
			{
				name = 'A' + maxNum1;
				ofile << name;
				s[maxNum1]--;
				sum --;
				if(s[maxNum1] > 1)
				{
					ofile << name;
					s[maxNum1]--;
					sum --;
				}		
				ofile  << " ";
			}
		}
		ofile << "\n";
		tt++;
	}
	ifile.close();
	ofile.close();
	return 0;
}