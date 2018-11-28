#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isPossible(string& inputString, size_t& index, char ch);
char getSign(char first, char second, char result);

// Structure to represent complex entities
struct complex
{
	char sign;			// Can be '+' or '-'
	char symbol;		// Can be '1', 'i', 'j', or 'k'

	complex() = default;
	complex(char sym, char si)
	{
		symbol = sym;
		sign = si;
	}

	friend complex operator*(complex& a, complex& b);
	friend bool operator==(complex& a, complex& b);
};

// Allows for multiplication of complex entities
complex operator*(complex& a, complex& b)
{
	complex result;
	char obtResSign = '+';

	if (a.symbol == '1')
	{
		result.symbol = b.symbol;
	}
	else if (b.symbol == '1')
	{
		result.symbol = a.symbol;
	}
	else if (a.symbol == b.symbol)
	{
		result.symbol = '1';
		obtResSign = '-';
	}
	else
	{
		if (a.symbol == 'i' && b.symbol == 'j')
			result.symbol = 'k';
		else if (a.symbol == 'i' && b.symbol == 'k')
		{
			result.symbol = 'j';
			obtResSign = '-';
		}
		else if (a.symbol == 'j' && b.symbol == 'i')
		{
			result.symbol = 'k';
			obtResSign = '-';
		}
		else if (a.symbol == 'j' && b.symbol == 'k')
			result.symbol = 'i';
		else if (a.symbol == 'k' && b.symbol == 'i')
			result.symbol = 'j';
		else
		{
			result.symbol = 'i';
			obtResSign = '-';
		}
	}

	// Set the sign and return the result
	result.sign = getSign(a.sign, b.sign, obtResSign);
	return result;
}

// Support for comparison
bool operator==(complex& a, complex& b)
{
	return a.symbol == b.symbol && a.sign == b.sign;
}

// Returns the sign obtained by multiplying three signs which are either '+' or 'v'
char getSign(char first, char second, char result)
{
	// If all three are negative,
	if (first == '-' && second == '-' && result == '-')
		return '-';
	
	// If one of first 2 is negative and result is +ve,
	else if (((first == '-') ^ (second == '-')) && result == '+')
		return '-';

	// If first two are +ve and result is negative
	else if (first == '+' && second == '+' && result == '-')
		return '-';

	else
		return '+';
}

// For debugging -- overload << later
void printEntity(complex& ent)
{
	cout << ent.sign << ent.symbol << endl;
}

int main()
{
	int T;
	string inputString;

	// Read the number of test cases
	cin >> T;

	for (int Case = 1; Case <= T; Case++)
	{
		int L, X;
		cin >> L >> X;

		string chars;
		cin >> chars;

		if (L* X < 3)
		{
			cout << "Case #" << Case << ": NO" << endl;
			continue;
		}
		else if (L * X == 3)
		{
			cout << "Case #" << Case << ": " << (chars == "ijk" ? "YES" : "NO") << endl;
			continue;
		}
		else
		{
			// Generate the input string
			for (int i = 0; i < X; i++)
				inputString.append(chars);

			size_t start = 0;
			cout << "Case #" << Case << ": " << (isPossible(inputString, start, 'i') ? "YES" : "NO") << endl;
		}

		// Clear inputString for next iteration
		inputString.clear();
	}

	return 0;
}

bool isPossible(string& inputString, size_t& index, char ch)
{
	complex obj(inputString[index], '+');
	index++;

	complex desired(ch, '+');

	while (index < inputString.length())
	{
		obj = obj * complex(inputString[index], '+');
		index++;
		
		// If found desired entity,
		if (obj == desired)
		{
			// If desired is 'k' and we are not at the end of the string, continue
			if (ch == 'k' && index != inputString.length())
				continue;
			else
			{
				// If k, we found the complete string, 
				if (ch == 'k')
					return true;
				// If i, recursively check for 'j' and 'k'
				else if (ch == 'i')
				{
					if (isPossible(inputString, index, 'j'))
						return true;
				}
				else if (ch == 'j')
				{
					if (isPossible(inputString, index, 'k'))
						return true;
				}
			}
		}
	}

	// Wasn't found,
	return false;
}