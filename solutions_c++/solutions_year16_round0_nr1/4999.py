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

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	FOR(tc,1,T+1)
	{
		int n, N;
		cin >> N;
		vector <bool> digit(10, false);
		FOR(i,1,200)
		{
			n = i * N;
			
			int t = n;
			while(t > 0)
			{
				digit[t%10] = true;
				t = t / 10;
			}
			int c = 0;
			FOR(i,0,10)
			{
				if(digit[i]) c++;
			}
			if(c == 10)
			{
				cout << "Case #" << tc << ": " << n << endl;
				break;
			}
		}
		int c = 0;
		FOR(i,0,10)
		{
			if(digit[i]) c++;
		}
		if(c != 10)
		{
			cout << "Case #" << tc << ": INSOMNIA" << endl;
		}
	}
	return 0;
}
