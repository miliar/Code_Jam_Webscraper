#include <iostream>
#include <string.h>
#include <string>

using namespace std;

void proc(int round)
{
	int max, num, total, add;
	string s;

	cin >> max >> s;

	total = 0;
	add = 0;
	for (int i = 0; i <= max; i++) {
		num = s[i] - '0';
		if (total < i) {
			add += i - total;
			total = i;
		}
		total += num;
	}

	cout << "Case #" << round << ": " << add << endl;
}

int main()
{
    int k;
    cin >> k;
    for (int i = 1; i <= k; i++)
    	proc(i);
    return 0;
}