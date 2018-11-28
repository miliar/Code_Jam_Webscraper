#include <iostream>
#include <fstream>
using namespace std;


void main()
{
	int cases, level;
	char x[7];
	int people[7];

	ifstream in("C:\\Users\\M\\Downloads\\A-small-attempt1.in");
	ofstream out("C:\\Users\\M\\Desktop\\out.txt");
	in >> cases;

	for (int k = 0;  k < cases; k++) // 
	{

	in >> level;
	int extra = 0;

	for (int i = 0; i <= level; i++)
		{
		int sum = 0;
		 in >> x[i];
		 people[i] = x[i] - '0';
			
			for (int j = 0; j < i; j++)
				sum += people[j];
		int it = i - sum;
		
		if ( it > 0)
			{
			extra += it; 
			people[0]+=it;
			}
		}

	out << "Case #" << k + 1 <<": " << extra <<endl;

	}

}