#include <iostream>
#include <set>

using namespace std;

int main() {
	set<int> sets;
	int t;
	cin >> t;

	for (int i = 1; i<=t; i++) {
		int n;
		int result;
		int c = 0;

		cin >> n;
		result = 0;
		sets.clear();
		while (sets.size() < 10) {
			c++;

			if (result == (result + n)){
				break;
			}

			result += n;
			int b = result;

			while(b>0) {
				
				sets.insert(b%10);
				b = b/10;
				
			}


		}

		if (sets.size() == 10) {
			cout <<"Case #" << i <<": " << result <<endl;	
		} else 
			cout <<"Case #" << i <<": INSOMNIA" << endl;



	}

	

	return 0;
}