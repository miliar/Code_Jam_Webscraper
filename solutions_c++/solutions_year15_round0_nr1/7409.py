#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int T;
int Smax;
char shyness;

int sum;
int numFriend;

int main()
{
	/*Read input:*/
	ifstream fin("A-large.in", ifstream::in);
	fin >> T;
	
	/*Write output:*/
	ofstream fout("A-large.out", ofstream::out);
	
	for (int i=1; i<=T; i++)
	{
		fin >> Smax;
		sum = 0;
		numFriend = 0;
		
		for (int k=0; k<=Smax; k++)
		{
			fin >> shyness;

			if (sum < Smax) /*Not maximum of shyness level*/
			{
				shyness -= '0'; /*Convert to numeric*/
				if (sum >= k)
				{
					sum += (int)shyness;
				}
				else
				{
					numFriend += k - sum;
					sum += k - sum + (int)shyness;
				}
			}
		}
		
		fout << "Case #" << i << ": " << numFriend << endl;
	}
	
	fin.close();
	fout.close();
	
	return 0;
}
