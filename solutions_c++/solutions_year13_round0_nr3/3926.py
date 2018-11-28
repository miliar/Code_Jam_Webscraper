#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

bool is_palin(int d)
{
	vector <int> v;
	while (d > 0)
	{
		v.push_back(d % 10);
		d /= 10;
	}
	int s = v.size();
	for (int i = 0 ; i < s / 2 ; i ++)
		if (v[i] != v[s-1-i])
			return 0;
	return 1;
}

int main()
{
	int T, A, B;
	int s, e;
	int cnt;
	cin >> T;
	for (int t = 1 ; t <= T ; t ++)
	{
		cin >> A >> B;
		cnt = 0;
		s = (int)sqrt(A-1) + 1;
		e = (int)sqrt(B);
		
		for (int i = s ; i <= e ; i ++)
			if (is_palin(i) && is_palin(i*i))
				cnt ++;
		
		cout << "Case #" << t << ": " << cnt << endl;
	}
	return 0;
}
