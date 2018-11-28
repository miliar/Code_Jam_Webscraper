#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <cmath>
#include <sstream>

using namespace std;

ifstream in;
ofstream out;

void processCase(int caseNum);
string to_string(long l);
bool isPalindrome(long num);

//precomputed in a few seconds using the commented code- only supports A, B up to 10^14
long sol[] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
int solSize = 39;

int main (void)
{
	in.open("C-large-1.in");
	out.open("output.txt");

	int T;
	in >> T;

	for (int i = 0; i < T; i++)
	{
		processCase(i+1);
	}

	in.close();
	out.close();
	return 0;
}

void processCase(int caseNum)
{
	long A, B;
	in >> A >> B;
	// long lowerBound = sqrt(A);
	// long upperBound = sqrt(B) + 1;

	int solCount = 0;

	// for (long i = lowerBound; i <= upperBound; i++)
	// {
	// 	if (isPalindrome(i))
	// 	{
	// 		long val = i*i;
	// 		if (!(A <= val && val <= B)) continue;
	// 		if (isPalindrome(val))
	// 		{
	// 			solCount++;
	// 			//cout << val << endl;
	// 		}
	// 	}
	// }

	for (int i = 0; i < solSize; i++) {
		if (sol[i] >= A && sol[i] <= B) 
		{
			solCount++;
		}
	}	

	out << "Case #" << caseNum << ": " << solCount << endl;;
}

bool isPalindrome(long num)
{
	//if (0 <= num && num <= 9) return true;
	string forw = to_string(num);
	string rev = string (forw.rbegin(), forw.rend());
	long revnum = atol(rev.c_str());

	return num == revnum;
}


string to_string(long l)
{
	stringstream ss;
	ss << l;
	return ss.str();
}