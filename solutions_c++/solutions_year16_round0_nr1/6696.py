#include<iostream>
using namespace std;

int main() {
	int cnt;
	cin >> cnt;
	for (int itr = 0; itr < cnt; itr++)
	{
		int a;
		cin >> a;
		bool* check = new bool[10];
		for (int i = 0; i < 10; i++)
		{
			check[i] = false;
		}
		int chk = false;
		int i = 0;
		for (i = 0; i < 100; i++)
		{
			int tmp = a*(i+1);
			while (1) {
				check[tmp % 10] = true;
				tmp = tmp / 10;
				if (tmp == 0) {
					break;
				}
			}
			for (int j = 0; j < 10; j++)
			{
				if (j == 0) {
					chk = check[j];
				}
				else {
					chk = chk&&check[j];
				}
			}
			if (chk) {
				break;
			}

		}
		cout << "Case #" << itr + 1 << ": ";
		if(chk){
			cout << a*(i + 1) << endl;
		}
		else {
			cout << "INSOMNIA" << endl;
		}
		
	}
	return 0;
}