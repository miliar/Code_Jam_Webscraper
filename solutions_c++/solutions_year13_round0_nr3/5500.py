#include <iostream>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

map<long, bool> checked;

bool isPalindrome(long inp)
{
	//if(checked.count(inp) > 0)
	//	return checked[inp];
	long temp = inp;
	unsigned long reversed = 0; 
	while (temp != 0)
    {
       reversed = reversed * 10;
       reversed = reversed + temp % 10;
       temp = temp / 10;
    }
    bool result = (inp == reversed);
    checked[inp] = result;
    checked[reversed] = result;
    return result;
}

int main()
{
	int cases;
	cin >> cases;
	for(int n = 1; n <= cases; n++)
	{
		long nPalinsquares = 0;
		long start, end;
		cin >> start >> end;
		
		long sq = 0;
		for(long i = 1;; i++)
		{
			sq = i*i;
			if(sq > end) break;
			if(isPalindrome(i) && isPalindrome(sq) && sq >= start && sq <= end)
			{
				nPalinsquares++;
				//cout << sq << endl;
			}
		}
		cout << "Case #" << n << ": " << nPalinsquares << endl;	
		//cout << "map size: " << checked.size() << endl;
	}
}
