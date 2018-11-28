#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

bool is_pal(unsigned long long curr)
{
	vector<int> digits;
	while(curr>=1)
	{
		digits.push_back(curr%10);
		curr/=10;
	}
	int back=digits.size()-1, front=0;
	while(back>front)
	{
		if(digits[back]!=digits[front])
		{
			return false;
		}
		back--;
		front++;
	}
	return true;
}

int main()
{
    int numTests;
    cin >> numTests;
    for(int test = 0; test < numTests; ++test)
    {
        unsigned long long min, max;
        cin >> min >> max;
        unsigned long long realMin = ceil(sqrt(min));
        unsigned long long realMax = floor(sqrt(max));
        int numFAS = 0;
        for (unsigned long long i = realMin; i <= realMax; ++i)
        {
            if (is_pal(i) && is_pal(i*i)) {
                //cout << i << endl;
                ++numFAS;
            }
        }

        cout << "Case #" << test+1 << ": " << numFAS << endl;
    }
}
