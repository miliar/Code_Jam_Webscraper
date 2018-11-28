#include "common.hpp"

using namespace std;

int main() {
	forEachTestCase([]() {
		int maxShyness;
		string s;
		cin >> maxShyness >> s;
		assert(maxShyness + 1 == s.size());

		int friends = 0;
		int standing = 0;
		for (int i = 0; i <= s.size(); i++) {
			int x = s[i] - '0';
			while (standing + friends < i) friends++;
			standing += x;
		}

		return friends;
	});
}