#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <functional>
#include <numeric>
#include <iomanip>
using namespace std;




bool isPalindrome(int input)
{
	int num = input;
	int new_num = 0;
	while(num > 0)
    {
		new_num = new_num*10 + (num % 10);
		num = num/10;
    }
	return (new_num == input);

}

int main(int argc, char * argv[])
{
	ifstream fin("input.txt"); 
	ofstream fout("output.txt");
	
	if(!fin.good())
	{
		cout << "opps" << endl;
	}
	string str;
	getline(fin, str);
	
	const int T = atoi(str.c_str());

	for( int aaa = 0; aaa < T ; aaa++)
	{
		int palinCount = 0;
		//	Load start and end
		getline(fin, str);
		istringstream iss(str);
		
		int A, B;
		iss >> A >> B;

		//	Compute ranges.
		int startA = ceil(sqrt (A));
		int startB = floor(sqrt (B));

		for (int bbb = startA; bbb <= startB; ++bbb)
		{
			if(isPalindrome(bbb))
			{
				int test = bbb*bbb;
				if(isPalindrome(bbb*bbb))
				{
					++palinCount;
				}
			}
		}

		fout << "Case #" << aaa+1 << ": " <<palinCount << "\n";
	}	

	fin.close(); fout.close();
	return 0;
}
