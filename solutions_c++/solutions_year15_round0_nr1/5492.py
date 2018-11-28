#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	ifstream in("A-small-attempt2.in");
	ofstream out("A-small-attempt2.out");
	//ifstream in("problem1.in");
	//ofstream out("problem2.out");
	std::vector <int> list;
	char ch;

	int T;
	in>>T;
	
	int j=0;
	while(j<T)
	{
		int neededCount = 0;
		int totalPerson = 0;
		int req = 0;

		int cSize;
		in>>cSize;
		
		int i=0;
		while(i<=cSize)
		{			
			in>>ch;			

			if(((int)ch-48) == 0)
			{
				neededCount++;
			}
			else if(totalPerson < i)
			{
				if(totalPerson == 0)
					req = neededCount;
				else
					req += i - totalPerson;

				totalPerson += (int)ch-48 + req;
				neededCount = 0;
			}
			else
			{
				totalPerson += (int)ch-48;
			}
			i++;
		}
		out<<"Case #"<<++j<<": "<<req<<endl;
	}
	
	//system("pause");
	return 0;
}