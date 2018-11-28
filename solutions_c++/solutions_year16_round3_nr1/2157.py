#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>

using namespace std;

#define LL long long

#define FOR(i,a,b) for(int i = a ; i < b ; i++)
#define FORI(i,b,a) for(int i = b ; i >= a ; i--)

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	FOR(tc,1,T+1)
	{
		int arr[26] = {0};
		int n;
		cin >> n;
		int sum = 0;
		FOR(i,0,n)
		{
			int num;
			cin >> num;
			sum = sum + num;
			arr[i] = num;
		}
		cout << "Case #" << tc << ": ";
		int s = 0;
		while(s < sum)
		{
			int i1 = -1;
			FOR(i,0,26)
			{
				if(i1 == -1 || (arr[i] > arr[i1] && arr[i] != 0))
				{
					i1 = i;
				}
			}
			int i2 = -1;
			FOR(i,0,26)
			{
				if(i1 != i && arr[i1] == arr[i])
				{
					i2 = i;
				}
			}
			cout << (char)('A' + i1);
			arr[i1]--;
			
			if(s + 1 != sum && s + 3 != sum)
			{
				if(i2 != -1)
				{
					cout << (char)('A' + i2) << " ";
					arr[i2]--;
				}
				else
				{
					cout << (char)('A' + i1) << " ";
					arr[i1]--;
				}
				s = s + 2;
			}
			else
			{
				cout << " ";
				s = s + 1;
			}
		}
		cout << endl;
	}
	return 0;
}
