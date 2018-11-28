#include <iostream>
#include <string>
#include <set>

using namespace std;

string sheep(int64_t number, set<int>& c, int& count, int cc)
{
	if (number==0) return string("INSOMNIA");
	int64_t t = number*cc;
	while (t>0) {
		int digit = t % 10;
		if (c.find(digit)==c.end())
		{
			c.insert(digit);
			count += 1;
			if (count==10) {
				return to_string(number*cc);
			}
		}
		t /= 10;
	}
	return sheep(number, c, count, cc+1);
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; ++i)
	{
		int64_t number;
		set<int> c;
		int count = 0;
		cin >> number;
		cout << "Case #" << i+1 <<": " << sheep(number, c, count, 1) << endl;
	}
}