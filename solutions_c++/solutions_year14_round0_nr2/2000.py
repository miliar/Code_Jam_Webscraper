#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		double c,f,x;

		cin >> c >> f >> x;

		double rate = 2;
		double cur = x / rate;
		double t = 0;
		double next = cur;
		do {
			cur = next;
			t += c / rate;
			rate += f;
			next = t + x / rate;
		} while (next < cur);

		std::cout.setf( std::ios::fixed, std:: ios::floatfield );
		std::cout.precision(8);
		cout << "Case #" << (q + 1) << ": " << cur;
		cout << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}