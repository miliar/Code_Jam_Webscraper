#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>
using namespace std;

int main()
{
	int caseN;
	cin >> caseN;
	for (int caseI = 1; caseI <= caseN; caseI++)
	{
		int n;
		cin >> n;
		
		vector<int> numbers(n);
		for (int i = 0; i < n; i++)
			cin >> numbers[i];
		
		int ans = 0;
		while (numbers.size() > 1)
		{
			int j = 0;
			for (int k = 1; k < numbers.size(); k++)
				if (numbers[k] < numbers[j])
					j = k;
			
			ans += min(j, (int)numbers.size() - 1 - j);
			numbers.erase(numbers.begin() + j);
		}
		
		cout << "Case #" << caseI << ": " << ans << endl;
	}
	
	return 0;
}
