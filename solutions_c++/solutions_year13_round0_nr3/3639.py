#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;

bool checkForP(long long n)
{
	bool flag = true;
	string str = to_string(n);
	long long index = str.length() - 1;
	for (int i = 0; i < str.length(); i++) {
		if (str[i] != str[index - i])
			flag = false;
	}

	return flag;
}

int main() {

	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int T;
	long long A, B;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> A >> B;
		int count = 0;
		long long  sqrtA = (long long)ceil(sqrt((long double)A));
		long long  sqrtB = (long long)floor(sqrt((long double)B));
		for (long long j = sqrtA; j <= sqrtB; j++) {
			if (checkForP(j)) {
				if (checkForP(j*j))
					count++;
			}
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}