#include <iostream>
using namespace std;

int main(){
	int test_cases;
	cin >> test_cases;
	int temp = test_cases;
	while(test_cases--){
		int k,c,s;
		cin >> k >> c >> s;
		cout << "Case #" << temp-test_cases << ": ";
		for (int i = 1; i <= k; ++i)
		{
			if(i==k)
				cout << i;
			else
				cout << i << " ";
		}
		cout << endl;

	}

	return 0;
}