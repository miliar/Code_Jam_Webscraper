#include <iostream>

using namespace std;

int do_case() {
	unsigned int max_shy;
	cin >> max_shy;

	string in;
	cin >> in;
	unsigned int extra_people = 0;
	unsigned int total_people = 0;
	for( unsigned int shy=0; shy<=max_shy; ++shy ) {
		unsigned int num = in[shy]-'0';
		if( total_people < shy ) {
			extra_people += shy-total_people;
			total_people += shy-total_people;
		}
		total_people += num;
	}
	return extra_people;
}

int main() {
	unsigned int T;
	cin >> T;

	for( unsigned int i=0; i<T; ++i ) {
		cout << "Case #" << (i+1) << ": " << do_case() << endl;
	}
}
