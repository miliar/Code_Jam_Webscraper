#include <bits/stdc++.h>

using namespace std;

set<int> seenNums;

void seeDigits(long long x)
{
	if (x==0) seenNums.insert(0);
	while(x>0){
		seenNums.insert(x%10);
		x/=10;
	}
}

long long lastNum(long long x)
{	
	int cur=1;
	while (seenNums.size()!=10){
		seeDigits(cur*x);
		cur++;
	}

	return (cur-1)*x;
}

int main()
{


	int tc,n,TC=0;
	cin >> tc;

	while (tc--){
		cin >> n;
		seenNums.clear();
		cout << "Case #" << ++TC << ": ";
		if (n==0){
			cout << "INSOMNIA" << endl;
			continue;
		}

		cout << lastNum(n) << endl;
	}





	return 0;
}