#include <iostream>
#include <string>
using namespace std;

int main() 
{
	string tmp;
	getline(cin, tmp);
	int numTestCases = stoi(tmp);

	for (int t = 0; t < numTestCases; t++) 
	{
		string panStack;
		getline(cin, panStack);
		int numFlips = panStack.back() == '-' ? 1 : 0;
		bool happySide = panStack.front() == '+' ? true : false;
		for (size_t i = 1; i < panStack.size(); i++)
			if ((panStack[i] == '+' && !happySide) || (panStack[i] == '-' && happySide))
			{
				numFlips++;	
				happySide = !happySide;
			}
		printf("Case #%d: %d\n", t+1, numFlips);
	}
	return 0;
}