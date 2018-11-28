#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void solve(int test)
{
	int answer;
	int newNum;
	vector<int> possible;
	vector<int> actual;
	
	cin >> answer;
	answer *= 4;
	
	for(int number=0; number<16; number++)
	{
		cin >> newNum;
	
		if(number < answer && number >= answer-4) {possible.push_back(newNum);}
	}
	
	cin >> answer;
	answer *= 4;
	
	for(int number=0; number<16; number++)
	{
		cin >> newNum;
	
		if(number < answer && number >= answer-4) 
		{
			if(find(possible.begin(), possible.end(), newNum) < possible.end())
			{
				actual.push_back(newNum);
			}
		}
	}
	
	cout << "Case #" << test << ": ";
	
	if(actual.size() == 1)
	{
		cout << actual[0];
	}
	else if(actual.size() == 0)
	{
		cout << "Volunteer cheated!";
	}
	else
	{
		cout << "Bad magician!";
	}
	
	cout << "\n";
}

int main()
{
	int tests;
	
	cin >> tests;
	tests++;
	
	for(int test=1; test<tests; test++)
	{
		solve(test);
	}

	return(0);
}