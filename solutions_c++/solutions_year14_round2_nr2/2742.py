#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int cases;
	cin >> cases;

	for (int i=0; i<cases; i++) {
		unsigned int A;
		cin >> A;

		unsigned int B;
		cin >> B;

		unsigned int K;
		cin >> K;

		unsigned int winning = 0;

		//Old machine
		for (int i=0; i<A; i++) {

			//New machine
			for (int j=0; j<B; j++) {
				if ( (i&j) < K ) {
					winning++;
				}
			}
		}

		cout << "Case #" << i + 1 << ": " << winning << endl;
	}

	return 0;
}