#include <iostream>
#include <string>

using namespace std;

#define debug cout

int counter[26];
int number[10];

void incr(char c)
{
	counter[c-'A']++;
}

void decr(char c)
{
	counter[c-'A']--;
}

void decr(string s)
{
	for (int i = 0; i < s.size(); i++)
		decr(s[i]);
}

bool isPos(char c)
{
	return counter[c-'A'] > 0;
}

string giveNumber()
{
	string output = "";
	
	for (int i = 0; i < 10; i++)
		while (number[i]-- > 0)
			output += ('0' + i);
	
	return output;
}

void RunInstance()
{
	string input;
	
	for (int i = 0; i < 10; i++)
		number[i] = 0;
	
	for (int i = 0; i < 26; i++)
		counter[i] = 0;
	
	cin >> input;
	
	for(int i = 0; i < input.size(); i++)
		incr(input[i]);
	
	while (isPos('Z'))
	{
		number[0]++;
		decr("ZERO");
	}
	
	while (isPos('W'))
	{
		number[2]++;
		decr("TWO");
	}
	
	while (isPos('X'))
	{
		number[6]++;
		decr("SIX");
	}
	
	while (isPos('G'))
	{
		number[8]++;
		decr("EIGHT");
	}
	
	while (isPos('U'))
	{
		number[4]++;
		decr("FOUR");
	}
	
	while (isPos('O'))
	{
		number[1]++;
		decr("ONE");
	}
	
	while (isPos('H'))
	{
		number[3]++;
		decr("THREE");
	}
	
	while (isPos('F'))
	{
		number[5]++;
		decr("FIVE");
	}
	
	while (isPos('V'))
	{
		number[7]++;
		decr("ZEVEN");
	}
	
	while (isPos('I'))
	{
		number[9]++;
		decr("NINE");
	}
	
	cout << giveNumber();
}

// ============================ Nothing to change here ============================ //

int main() 
{
    int num_of_instances = 0;
    cin >> num_of_instances;
    
    for (int i = 1; i <= num_of_instances; ++i) 
    {
        cout << "Case #" << i << ": ";
        RunInstance();
        cout << endl;
    }
}