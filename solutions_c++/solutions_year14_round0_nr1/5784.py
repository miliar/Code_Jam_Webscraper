#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
	set<int> options;
	int t, n, input, cont, teste=1, result;
	cin >> t;

	while(t-- > 0)
	{
		options.clear();
		cin >> n;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> input;
				if(i+1 == n)
					options.insert(input);
			}
		}
		
		cont=0;
		cin >> n;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> input;
				if(i+1 == n)
				{
					if(!options.insert(input).second)
					{
						cont++;
						result = input;
					}
				}
			}
		}
		if(cont == 0)
			cout << "Case #" << teste++ << ": Volunteer cheated!\n"; 
		else if(cont == 1)
			cout << "Case #" << teste++ << ": " << result << "\n";
		else
			cout << "Case #" << teste++ << ": Bad magician!\n";
	}
	return 0;
}
