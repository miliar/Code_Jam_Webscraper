#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i=1; i<=T;i++) {
		string str;
		cin >> str;
		int flips=0;
		for (int j=str.size()-1; j>=0; j--) {
			if (str[j] == '+' && flips&1) {
				flips++;
			} else if  (str[j] == '-' && !(flips&1)) {
				flips++;
			}
		}
		cout << "Case #" << i << ": " << flips << endl;
	}
	return 0;
}