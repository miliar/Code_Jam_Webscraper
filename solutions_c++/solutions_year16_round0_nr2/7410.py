#include <iostream>
#include <fstream>

int main(){
	std::ifstream in("input.in");
	std::ofstream out("output.out");
	int t, flips, i;
	size_t size, j;
	char prev;
	std::string s;
	in >> t;
	for (i = 1; i <= t; i++){
		out << "Case #" << i << ": ";
		in >> s;
		flips = 0;
		size = s.length();
		prev = s[0];
		for (j = 1; j < size; j++){
			if (prev != s[j]){
				flips++;
				prev = s[j];
			}
		}
		if (prev == '-') flips++;
		out << flips << "\n";
	}
	return 0;
}
