#include <vector>
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <string>
#include <climits>

using namespace std;

void iterate(unsigned int& a, vector<int>& others, unsigned int& min)
{
	unsigned int tmp = INT_MAX;

	for(vector<int>::iterator it=others.begin(); it!=others.end();)
	{
		if( *it < a)
		{
			a = a + *it;
			others.erase(it);
			it = others.begin();
		}
		else if(*it<tmp)
		{
			min=*it;
			tmp=*it;
			it++;
		}
		else
		{
			it++;
		}
	}
}

int howManyToReach(unsigned int a, unsigned int min)
{
	unsigned int count=0;
	while(a<=min && a!=1)
	{
		a += (a-1);
		count++;
	}

	if(a==1)
	{
		return INT_MAX;
	}

	return count;
}

int main()
{


	ifstream inputFile;
	inputFile.open("A-large.in");
	if ( inputFile.good() )
	{
		unsigned int numberOfInputs;
		inputFile >> numberOfInputs;

		for(unsigned int inputNumber=0; inputNumber<numberOfInputs;)
		{
			unsigned int a, n, min=999, op=0, tmp_eleman=0;
			inputFile >> a >> n;
			int pl, many;
			bool flag=true;
			vector<int> others;
			for(unsigned int t=0; t<n; t++)
			{
				inputFile >> pl;
				others.push_back(pl);
			}

			iterate(a, others, min);
			tmp_eleman = others.size();
			while(flag)
			{
				if ( (many=howManyToReach(a, min)) < others.size() )
				{
					for(unsigned int j=0; j<many; j++)
					{
						a += (a-1);
						op++;
					}
				}
				else
				{
					flag = false;
				}
				iterate(a, others, min);
			}

			op+=others.size();

			others.clear();

			if (op>tmp_eleman)
			{
				op = tmp_eleman;
			}
			cout << "Case #" << ++inputNumber << ": " << op << endl;

		}
	}
	inputFile.close();

	return 0;
}
