#include <vector> 
#include <string>
#include <fstream>
using namespace std;

int main()
{
	int n;
	ifstream in;
	in.open("input.txt");
	ofstream out;
	out.open("output.txt");
    in >> n;
	for (int i = 0; i < n; i++)
	{
		int nmax;
		in >> nmax;
		string shy;
		in >> shy;

		int friends = 0;
		int currentNumber = 0;
		for (int j = 0; j <= nmax; j++)
		{
			int stepNumber = shy[j] -'0';
			int friendToAdd = 0;
			if ((currentNumber < j) && stepNumber!=0)
			{
				friendToAdd = j - currentNumber;
				friends += friendToAdd;
			}
			currentNumber += stepNumber + friendToAdd;
		}
		out << "Case #" << i+1 << ": " << friends<<endl;
	}
	
}