#include <cstdio>
#include <iostream>

using namespace std;

int T;
int sMax;
string people;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("Output.txt","w",stdout);
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int total = 0;
		int res = 0;
		cin >> sMax >> people;
		for (int j = 0; j <= sMax; ++j)
		{ 
			int n = people[j] - '0';
			if(total < j && n > 0){
				res += j - total;
				total += res + n;
			}
			else{
				total += n;
			}
		}
		printf("Case #%d: %d\n",i+1,res);
	}

	return 0;
}