#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;

bool palin(int n)
{
	stringstream in; 
	in << n;
	string tmp = in.str();
	for (int i = 0; i < tmp.size(); i++)
		if (tmp[i] != tmp[tmp.size()-i-1])
			return false;
	return true;
}

int main()
{
	int t, a, b, ans;
	cin >> t;
	for (int z = 1; z <= t; z++){
		cin >> a >> b;
		ans = 0;
		for (int i = ceil(sqrt(a)); i <= floor(sqrt(b)); i++)
			if (palin(i) && palin(i*i)) {
				++ans;
			}
		cout << "Case #" << z << ": " << ans << endl;
	}
	return 0;
}
