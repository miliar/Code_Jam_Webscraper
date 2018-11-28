#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>

using namespace std;

int main() {
	std::ifstream in("A-large.in");
	std::ofstream out("a.out");
	int n, t;
	in >> t;
	for(int i = 1; i <= t; i++) {
		in >> n;
		if (n == 0) {
			out << "Case #" << i << ": " <<  "INSOMNIA";
		} else {
			int j = 1;
			int match[10] = {}, count = 0;
			bool found = false;
			while (!found) {
				long long m = n*j++;
				while(m > 0) {
					if(match[m%10] == 0) {
						count++;
						match[m%10] = 1;
					}
	//				cout << m%10 << " " << match[m%10] << " " << count << endl;
	//				getch();
					m = m / 10;
					if (count == 10) {
						out << "Case #" << i << ": " <<  n*(j-1);
						found = true;
						break;
					}
				}
			}
		}
		if (i < t) {
			out << endl;
		}
	}
}
