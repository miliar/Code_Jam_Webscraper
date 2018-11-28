#include <iostream>
#define ll long long
#define MAX_IN 1000001

using namespace std;

ll answers[MAX_IN];

void final_num(int n)
{
	ll flag = 0, final = 0;
	for(int i = 0; i < 10; ++i)
		final = (final | (2 << i));
	int multiplier = 1;
	while(flag != final) {
		ll ans = n * multiplier;
		while(ans){
			int digit = ans % 10;
			flag = (flag | (2 << digit));
			if(flag == final) {
				answers[n] = n * multiplier;
				return;
			}
			ans = ans/10;
		}
		++multiplier;
	}
}


int main()
{
	for(int i = 1; i <= 1000000; ++i)
		final_num(i);

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i) {
		int n;
		cin >> n;
		cout << "Case #" << i << ": ";
		if(!n)
			cout << "INSOMNIA" << endl;
		else
			cout << answers[n] << endl;
	}
	return 0;
}