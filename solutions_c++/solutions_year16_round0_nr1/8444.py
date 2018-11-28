#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ofstream ofs("ans.txt");
	int t;
	cin >> t;
	int cnum = 1;
	while (cnum <= t) {
		int arr[10] = { 0 };
		int num;
		cin >> num;
		int count = 0;
		

		if (num == 0) {
			ofs << "Case #" << cnum++ << ": INSOMNIA" << endl;
		}
		else {
			int mul = 2;
			int tmp = num;
			int ans = tmp;
			while (count != 10) {
				

				while (tmp) {
					if (arr[tmp % 10] == 0) {
						arr[tmp % 10]++;
						count++;
					}
					tmp /= 10;
				}

				if (count != 10) {
					tmp = num * mul;
					ans = tmp;
					mul++;
				}
			}

			ofs << "Case #" << cnum++ << ": " << ans << endl;
		}
	}
	ofs.close();
}