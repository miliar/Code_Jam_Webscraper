#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;

	for(int i = 1; i <= t; ++i) {
		int num;
		cin >> num;
		int new_num = 0;
		bool check[10] = {false, false, false, false, false, false, false, false, false, false};
		bool done = false;
		int ctr = 0;

		while(!done && ctr < 500) {
			new_num = new_num + num;
			int temp = new_num;
			while(temp > 0) {
				check[temp%10] = true;
				temp = temp/10;
			}
		
			if(check[0] && check[1] && check[2] && check[3] && check[4] && check[5] && check[6] && check[7] && check[8] && check[9])
				done = true;

			ctr++;
		}
		
		if(done)
			cout << "Case #" << i << ": " << new_num << endl;
		else
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
	}

	return 0;
}