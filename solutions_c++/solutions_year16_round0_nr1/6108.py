#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;

int main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		//int n;
		int stuff;
		cin >> stuff;
		if (stuff == 0)
		{
			cout << "Case #" << t << ": INSOMNIA" << endl;
		}
		else
		{
			int sum = 0;
			int i = 1;
			int last = 0;
			int answer = 0;
			while (answer != 1023)
			{
				sum = stuff * i;
				last = sum;
				while (sum != 0)
				{
					answer |= (1 << sum%10);
					sum = sum/10;
				}
				i++;
			}

			cout << "Case #" << t << ": ";
			cout << last << endl;
		}
		
		
	}
	return 0;
}