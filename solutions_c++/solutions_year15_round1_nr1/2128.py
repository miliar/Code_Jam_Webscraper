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

int a[1001];

int main()
{
	int T;
	cin >> T;
	
	for(int ii = 1; ii <= T; ii++)
	{
		int N;
		cin >> N;
		
		for(int i = 1; i <= N; i++)
		{
			cin >> a[i];
		}	
		
		int licznik = 0, licznik2 = 0;
		
		for(int i = 2; i <= N; i++)
			if(a[i] - a[i - 1] < 0)
				licznik = licznik + a[i - 1] - a[i];
				
		int zab = 0;
		
		for(int i = 1; i <= N - 1; i++)
			if(a[i] - a[i + 1] > 0)
			{
				zab = max(zab, (a[i] - a[i + 1]));
			}
			
		for(int i = 1; i <= N - 1; i++)
		{
			licznik2 = licznik2 + min(a[i], zab);
		}
		
		cout << "Case #" << ii << ": " << licznik << " " << licznik2 << endl;
	}
	
	return 0;
}

