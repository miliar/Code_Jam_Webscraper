#include <fstream>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

string toString(unsigned int what)
{
    stringstream ss;
	ss << what;
    return string(ss.str());
}

class DigitsDictionary
{
private:
	int leftDigits;
	bool setDigits[10];
public:
	DigitsDictionary()
	{
		leftDigits = 10;
		for(int i = 0; i < 10; i++)
		{
			setDigits[i] = 0;
		}
	}
	void Add(unsigned int nr)
	{
		do
		{
			if(!setDigits[nr % 10])
			{
				setDigits[nr % 10] = true;
				leftDigits--;
			}
			nr /= 10;
		} while(nr > 0);
	}
	bool IsFull()
	{
		return leftDigits == 0;
	}
};

unsigned int maxSteps = 0;
unsigned int maxV = 0;

string solve(unsigned int n)
{
	string ans = "INSOMNIA";
	if(n > 0)
	{
		DigitsDictionary dict;
		for(unsigned int i = 1; i <= 1000000; i++)
		{
			dict.Add(i * n);
			if(dict.IsFull())
			{
				maxSteps = max(maxSteps, i);
				maxV = max(maxV, i * n);
				return toString(i * n);
			}
		}
	}
	return ans;
}

int main()
{
	int t;
	unsigned int n;
	ifstream f("input.txt");
	ofstream g("output.txt");
	f >> t;
	for(int i = 1; i <= t; i++)
	{
		f >> n;
		string ans = solve(n);
		g << "Case #" << i << ": " << ans << '\n';
	}
	f.close();
	g.close();
	return 0;
}
