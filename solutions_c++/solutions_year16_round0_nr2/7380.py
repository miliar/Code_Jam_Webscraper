
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include <list>

using namespace std;

void flip(std::vector<bool> &stack, int lastToFlip)
{	
	for (int i = 0; i < (int)lastToFlip/2; ++i)
	{
		bool temp = stack.at(i);
		stack.at(i) = stack.at(lastToFlip-i-1);
		stack.at(lastToFlip-i-1) = temp;
	}
	for (int i = 0; i < lastToFlip; ++i)
	{
		stack.at(i) = !stack.at(i);
	}
	//cout << "Flipping done" << endl;
}

int findFirstChange(std::vector<bool> stack)
{
	if (stack.at(0))
	{
		//cout << "a" << endl;
		int i = 1;
		for (; i < stack.size(); ++i)
		{
			if (stack.at(i) == false)
			{
				//cout << "First change is " << i << endl;
				return i;
			}
		}
		return i;
		
	}
	else
	{
		//cout << "b" << endl;
		int i = 1;
		for (; i < stack.size(); ++i)
		{
			//cout << "c" << endl;
			if (stack.at(i))
			{
				//cout << "d" << endl;
				//cout << "First change is " << i << endl;
				return i;
			}
		}
		//cout << "e" << endl;
		return i;
	}
	
}

bool evaluate(std::vector<bool> stack)
{
	for (int i = 0; i < stack.size(); ++i)
	{
		if (!stack.at(i))
		{
			//cout << "Evaluate returned false." << endl;
			return false;
		}
	}
	//cout << "Evaluate returned true." << endl;
	return true;
}

// - is false and + is true

int main(int argc, char const *argv[])
{
	long int n;
	ifstream input ("input.txt");
	ofstream output ("output.txt");
	input >> n;
	//cout << "Size n is " << n << endl;

	std::vector<std::vector<bool> > stack;

	for (long int i = 0; i < n; ++i)
	{
		stack.push_back(std::vector<bool>());
		string line;
		input >> line;
		for (int j = 0; j < line.size(); ++j)
		{
			if (line.at(j) == '+')
			{
				stack.at(i).push_back(true);
			}
			else
			{
				stack.at(i).push_back(false);
			}
		}
	}
	for (int i = 0; i < n; ++i)
	{
		int counter = 0;
		while(!evaluate(stack.at(i)))
		{
			int flipTo = findFirstChange(stack.at(i));
			//cout << "flipTo is " << flipTo << endl;
			flip(stack.at(i),flipTo);
			counter++;
		}
		output << "Case #" << i+1 << ": " << counter << endl;
		cout << "Case #" << i+1 << ": " << counter << endl;
	}
	return 0;
}