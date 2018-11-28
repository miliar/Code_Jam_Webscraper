#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#define mp make_pair
#define st first
#define nd second
#define ll long long
#define ld long double

using namespace std;
typedef pair <int, int> para;

int ilu[10001];

int main()
{
	int T;
	cin >> T;
	
	for(int k = 1; k <= T; k++)
	{
		int smax;
		cin >> smax;
		
		for(int i = 0; i <= smax; i++)
		{
			char x;
			cin >> x;
			
			ilu[i] = x - '0';
		}
		
		int dolozylismy = 0;
		int stoi = ilu[0];
		
		for(int powinno_stac = 1; powinno_stac <= smax; powinno_stac++)
		{
			if(powinno_stac > stoi + dolozylismy)
			{
				dolozylismy += (powinno_stac - stoi - dolozylismy);
			}
			stoi = stoi + ilu[powinno_stac];
		}
		
		cout << "Case #" << k << ": " << dolozylismy << endl; 
	}
	
	return 0;
}

