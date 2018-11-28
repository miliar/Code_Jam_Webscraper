#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstring>
#include <string>
using namespace std;
int a[20];
void myFill(long long num) {
	while (num > 0) {
		a[num % 10] = 1;
		num = num / 10;
	}
}
bool check() {
	for (int i = 0; i < 10; i++)
	{
		if (a[i] == 0)
			return 0;
	}
	return 1;
}
int main() {
	//ifstream cin("in.in");
	//ofstream cout("out.out");
	int t;
	cin >> t;
	for (int l = 0; l < t; l++)
	{
		memset(a, 0, 15 * sizeof(int));
		long long n;
		cin >> n;
		bool flag = 0;
		for (int i = 0; i < 100; i++)
		{
			myFill(i*n);
			if (check()) {
				flag = 1;
				cout <<"Case #"<<l+1<<": "<< i*n << endl;
				break;
			}
		}
		if (!flag)
			cout << "Case #" << l+1 << ": " << "INSOMNIA" << endl;
	}
	return 0;
}
