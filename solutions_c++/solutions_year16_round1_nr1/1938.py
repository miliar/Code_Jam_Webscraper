#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    int test;
	cin >> test;
	for (int t=0; t<test; t++) {
		string word;
		cin >> word;
		string last_word = "";
		for (int i=0; i<word.length(); i++) {
			int j;
			for (j=0; j<last_word.length(); j++) {
				if (word[i] > last_word[j]) {
					last_word = word[i] + last_word;
					break;
				}
				else if (word[i] < last_word[j]) {
					last_word = last_word + word[i];
					break;
				}
			}
			if (j == last_word.length()) {
				last_word = last_word + word[i];
			}
		}
		cout << "Case #" << t+1 << ": " << last_word << endl;
	}

    return 0;
}
