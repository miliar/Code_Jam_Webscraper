#include <iostream>
#include <vector>
#include <algorithm>
#include <string>


using namespace std;

int main()
{
	int test_case;
	cin >> test_case;
	string input;
	for(int i = 1; i <= test_case; ++i)
	{
		cin >> input;
		vector<string> num;
		num.push_back("ZERO"); //done
		num.push_back("ONE");	//done
		num.push_back("TWO"); //done
		num.push_back("THREE");//done
		num.push_back("FOUR"); //done
		num.push_back("FIVE");//done
		num.push_back("SIX"); //done
		num.push_back("SEVEN"); //done
		num.push_back("EIGHT"); //done
		num.push_back("NINE");
		vector<int> characters(26);
		for(int j = 0; j < input.size(); ++j)
			++characters[input[j] - 'A'];
		vector<int> numbers(10);
		while(characters['Z'-'A'])
		{
			--characters['Z'-'A'];
			--characters['E'-'A'];
			--characters['R'-'A'];
			--characters['O'-'A'];
			++numbers[0];
		}
		while(characters['X'-'A'])
		{
			--characters['X'-'A'];
			--characters['S'-'A'];
			--characters['I'-'A'];
			++numbers[6];
		}	
		while(characters['G'-'A'])
		{
			--characters['E'-'A'];
			--characters['I'-'A'];
			--characters['G'-'A'];
			--characters['H'-'A'];
			--characters['T'-'A'];
			++numbers[8];
		}	
		while(characters['W'-'A'])
		{
			--characters['T'-'A'];
			--characters['W'-'A'];
			--characters['O'-'A'];
			++numbers[2];
		}
		while(characters['U'-'A'])
		{
			--characters['F'-'A'];
			--characters['O'-'A'];
			--characters['U'-'A'];
			--characters['R'-'A'];
			++numbers[4];
		}	
		while(characters['H'-'A'])
		{
			--characters['T'-'A'];
			--characters['H'-'A'];
			--characters['R'-'A'];
			--characters['E'-'A'];
			--characters['E'-'A'];
			++numbers[3];
		}	
		while(characters['O'-'A'])
		{
			--characters['O'-'A'];
			--characters['N'-'A'];
			--characters['E'-'A'];
			++numbers[1];
		}
		while(characters['F'-'A'])
		{
			--characters['F'-'A'];
			--characters['I'-'A'];
			--characters['V'-'A'];
			--characters['E'-'A'];
			++numbers[5];
		}	
		while(characters['S'-'A'])
		{
			--characters['S'-'A'];
			--characters['E'-'A'];
			--characters['V'-'A'];
			--characters['E'-'A'];
			--characters['N'-'A'];
			++numbers[7];
		}
		while(characters['N'-'A'])
		{
			--characters['N'-'A'];
			--characters['I'-'A'];
			--characters['N'-'A'];
			--characters['E'-'A'];
			++numbers[9];
		}			
		cout << "Case #" << i << ": ";
		for(int j = 0; j < 10; ++j)
		{
			while(numbers[j]--)
				cout << j;
		}
		cout << "\n";
	}
}
