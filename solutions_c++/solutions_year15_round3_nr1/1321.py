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

int main()
{
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		
		int R,C,W;
		cin >> R >> C >> W;
		cout << "Case #" << i << ": ";
		
		if(C % W == 0)
			cout << R * (int)(C/W) + W - 1 << endl;
		else
			cout << R * (int)(C/W) + W << endl;
	}
	return 0;
}

