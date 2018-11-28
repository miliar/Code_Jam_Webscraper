#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <string>
#include <array>

using namespace std;

int main()
{
	ifstream in("small.in");
	//ifstream in("A-large.in");
	ofstream out("small.out");
	
	unsigned long long int T, k, c, s, result, many, jc;
	string line;
	if (in.is_open()){
		in >> T;
		
		for (int i = 1; i <= T; i++){
			in >> k;
			in >> c;
			in >> s;
			//cout << k << " " << c << " " << s << endl;
			out << "Case #" << i << ":";
			if (s < k / c)
				out << " IMPOSSIBLE";
			else {
				for (int j = 1; j <= k; j++) {
					out << " " << j;
				}
				/*if (c == 1) {
					many = k;
					for (int j = 1; j <= many; j++) {
						out << " " << j;
					}
				}
				else {
					many = k / c;
					if (k % c > 0) {
						many++;
					}

					for (int j = 1; j <= many; j++) {
						result = (j - 1) * c * pow(k, c - 1);
						result += pow(k, c - 1) + 
						jc = j * c;
						while (jc > k) {
							jc -= k;
						}
						result += jc;
						while (result > pow(k, c))
							result -= k;
						out << " " << result;
					}
				}*/
			}
			out << endl;
		}
		in.close();
	}
	out.close();
	return 0;
}