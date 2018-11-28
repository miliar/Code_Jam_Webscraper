#include <iostream>
#include <algorithm>
#include <bitset>

using namespace std;

const int LIMIT = 75;

int main()
{
	bitset<10> check;
	int T, N, last;
	string s;
	
	
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		check.reset();
		cin >> N;
		cout << "Case #" << t << ": ";
		
		if (N > 0) {
			for (int i = 1; !check.all() && i < LIMIT; i++)
			{
				last = i*N;
				s = to_string(last);
				
				for (auto c : s)
					check |= (1 << (c - '0'));
			}
		}

		if (check.all()) cout << last << endl;
		else cout << "INSOMNIA" << endl;
	}
	
	return 0;
}
			
			
			
		
