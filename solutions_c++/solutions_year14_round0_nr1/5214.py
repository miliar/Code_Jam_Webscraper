//
//  main.cpp
//  google_code_jam
//

#include <iostream>
#include <vector>
using namespace std;

using std::vector;
using std::cin;
using std::cout;

int main(int argc, const char * argv[])
{
	int num_test_cases = 0;
	int first_ans = 0;
	int second_ans = 0;
	
	vector< vector<int> > first (5, vector<int> (5,0));
	vector< vector<int> > second (5, vector<int> (5,0));
	
	cin>>num_test_cases;
	if (num_test_cases < 1 || num_test_cases > 100)
		num_test_cases = 0;
	
	for (int test_case = 1; test_case <= num_test_cases; test_case++)	{
		vector<int> count(17, 0);
		bool visitor_fault = true;
		bool magician_fault = false;
		bool magic = false;
		int magic_number = 0;
		
		cin>>first_ans;
		for (int i = 1 ; i<= 4; i++)	{
			for (int j = 1; j<=4; j++)	{
				cin>>first[i][j];
			}
		}
		
		cin>>second_ans;
		for (int i = 1 ; i<= 4; i++)	{
			for (int j = 1; j<=4; j++)	{
				cin>>second[i][j];
			}
		}
		
		for (int i=1; i <=4; i++)	{
			count[first[first_ans][i]]++;
			count[second[second_ans][i]]++;
		}
		
		for (int i=1; i<=16; i++)	{
			if (count[i] == 2)	{
				if (magic)	{
					magician_fault = true;
				}
				else	{
					visitor_fault = false;
					magic = true;
					magic_number = i;
				}
			}
		}
		
		if (visitor_fault)	{
			cout<<"Case #"<<test_case<<": Volunteer cheated!\n";
		}
		else if (magician_fault)	{
			cout<<"Case #"<<test_case<<": Bad magician!\n";
		}
		else{
			cout<<"Case #"<<test_case<<": "<<magic_number<<"\n";
		}
		
	}
    return 0;
}
