#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

bool isPalindrome(const string& str)
{
	return equal(str.begin(),str.end(),str.rbegin());
}

int main()
{
	ifstream file;
	file.open("C-small-attempt0.in");
	ofstream output;
	output.open("result.out");
	//output.setf(ios_base::fixed, ios_base::floatfield);
	//output.precision(10);
	

	int caseNo;
	file >> caseNo;

	for(int t=1; t<= caseNo; t++)
	{
		long long int start, end;
		long long int n;
		string str;
		stringstream temp;
		file >> start >> end;

		long long int score=0;

		for(n=start;n<=end;n++)
		{
			temp.str("");
			temp << n;
			str = temp.str();
			if(isPalindrome(str)){
				if((long double)(long long int)sqrt((long double)n) - sqrt((long double)n) == 0.0){
					temp.str("");
					temp << (long long int)sqrt((long double)n);
					str = temp.str();
					if(isPalindrome(str)) score += 1;
				}
			}
		}

		output << "Case #" << t << ": ";
		output <<  score << endl;

	}

	
}