#include <iostream>
#include <string>
using namespace std;

int solve(string a)
{
	int sum = 0, total = 0;
	for(int i = 0; i < a.size(); i++) {
		sum += (a[i] - '0');
		if(sum < i + 1) {
			total += (i + 1) - sum;
			sum += (i + 1) -sum;
		}
	}
	return total;
}


int main()
{
	int N;
	cin >> N;
	for(int i = 1; i <= N; i++) {
		int sn;
		string a;
		cin >> sn >> a;
		cout << "Case #" << i << ": " << solve(a) << endl;
	}
}

