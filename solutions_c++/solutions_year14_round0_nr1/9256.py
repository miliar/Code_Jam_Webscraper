#include <iostream>
#include <vector>

using namespace std;

void dev_null(int n)
{
	int trash;
	for(int i=0;i<n;i++)
	{
		cin >> trash;
	}
}

void print_vector(vector<int> i)
{
	cout << "Vector: ";
	for(vector<int>::iterator it = i.begin(); it != i.end(); ++it)
	{
		cout << *it << " ";
	}
	cout << endl;
}

int main()
{
	int test_cases, row_in, read_in;
	cin >> test_cases;

	for(int i=1;i<=test_cases;++i)
	{
		cin >> row_in;
		vector<int> first_results, second_results;

		for(int j=1;j<=4; ++j)
		{
			if(j == row_in)
			{
				for(int k=0; k<4; ++k)
				{
					cin >> read_in;
					first_results.push_back(read_in);	
				}
			} else {
				dev_null(4);
			}
		}
		
		cin >> row_in;
		for(int j=1;j<=4;++j)
		{
			if(j == row_in)
			{
				for(int k=0;k<4;++k)
				{
					cin >> read_in; 
					vector<int>::iterator it = first_results.begin();
					while(it != first_results.end())
					{
						if(*it == read_in)
						{
							second_results.push_back(read_in);
						}
						++it;
					}
				}
			} else {
				dev_null(4);
			}
		}

		cout << "Case #" << i << ": ";
		if(second_results.size() == 0)
		{
			cout << "Volunteer cheated!" << endl;
		} else if( second_results.size() > 1)
		{
			cout << "Bad magician!" << endl;
		} else 
		{
			cout << second_results[0] << endl;
		}

	}
	return 0;
}
