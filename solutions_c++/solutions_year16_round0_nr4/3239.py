#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <set>
#include <algorithm>
#include <sstream>
#include <set>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << (q+1) << ": ";
		for (int i=0;i<k;i++) {
			cout << (i+1) << " ";
		}
		cout << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}