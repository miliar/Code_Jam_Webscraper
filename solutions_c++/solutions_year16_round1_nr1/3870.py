#include <iostream>
#include <deque>

using namespace std;
int main()
{
	int T;
	char input[1001];
	cin >> T;
	deque<char> dq;
	for (int i = 1; i <= T; i++) {
		cin >> input;
		cout << "Case #"  << i << ": ";
		
		for(int m = 0; input[m] != '\0'; m++) {
			if (m == 0 ) 
				dq.push_back(input[m]);
			else {
				//cout << dq.at(0) << endl;
				if (dq.at(0) > input[m])
					dq.push_back(input[m]);
				else
					dq.push_front(input[m]);
			}
		}	
		for (int i=0; i<(signed)dq.size(); ++i) {
			cout << dq.at(i);
		}
		dq.clear();
		cout << endl;			
	}
	return 0;
}