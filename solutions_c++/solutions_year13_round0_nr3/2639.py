#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <set>
#include <algorithm>
#include <sstream>

using namespace std;

bool is_palin(int n)
{
	ostringstream s;
	s << n;
	string str = s.str();
	for (int i=0;i<str.size()/2;i++) {
		if (str[i] != str[str.size() - i - 1])
			return false;
	}
	return true;
}

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	vector<int> vals;
	for (int i=0;i<1000;i++) {
		if (is_palin(i) && i*i < 1000 && is_palin(i*i))
			vals.push_back(i*i);
	}

	for (int q=0;q<z;q++) {
		int a, b;
		cin >> a >> b;
		int count = 0;
		for (int i=0;i<vals.size();i++) {
			if (vals[i] >= a && vals[i] <= b)
				count++;
		}

		cout << "Case #" << (q+1) << ": " << count << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}