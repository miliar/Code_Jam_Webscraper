#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T, i, j, count;
	bool flip;
	string pStack;
	
	cin >> T;
	
	for(i = 0; i < T; ++i)
	{
		flip = count = 0;
		cin >> pStack;
		for(j = pStack.length(); j > 0; --j)
		{
			if((pStack[j-1] == '+' && flip == 1) || (pStack[j-1] == '-' && flip == 0))
			{
				++count;
				flip = !flip;
			}
		}
		
		cout << "Case #" << i +1 << ": " << count << endl;
	}
}
