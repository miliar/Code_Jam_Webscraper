#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

bool IsThere(int digit, int number)
{
	int n;
	while (number>0)
	{
		n=number%10;
		number/=10;
		if (n == digit)
			return true;
	}
	return false;
}

bool AllTrue(bool test[], int size)
{
	for (int i = 0; i < size; i++)
	{
		if(test[i]==false)
			return true;
	}
	return false;
}

int main()
{
	ifstream infile;
	infile.open("A-large.in");
	ofstream outfile("data.txt");
	int T;
	infile >> T;
	//cout <<T;
	for (int i=0;i<T;i++)
	{
		int n;
		infile >> n;
		//cout <<"Case #" <<i+1 << ": ";
		outfile <<"Case #" <<i+1 << ": ";
		if (n==0)
		{
			//cout << "INSOMNIA" <<endl;
			outfile << "INSOMNIA";
		}
		else
		{
			int store = n;
			int nums[10]={0,1,2,3,4,5,6,7,8,9};
			bool test[10]={false};
		
			while (AllTrue(test,10))
			{
				for (int j = 0; j < 10; j++)
				{
					if(IsThere(j,n))
						test[j]=true;
				}
				n+=store;
			}
			outfile << n-store;
			//cout << n-store <<endl;
		}
		if (i<T-1)
			outfile <<endl;
		
	}
	return 0;
}