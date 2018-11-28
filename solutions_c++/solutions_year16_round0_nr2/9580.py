#include <fstream>
#include <string>

int main(void) {
	std::ifstream fi("B-large.in");
	std::ofstream fo("B-large.out");
	if (fi.is_open())
	if (fo.is_open()){
		std::string input;//current line
		std::getline(fi, input);
		auto T = std::stoi(input);
		for (auto C = 1; C <= T; C++) {
			bool b = 0;					//previous side //0=+ //1=-
			auto flips = 0;	//number of flips for case
			std::getline(fi, input);
			for (int i = input.length() - 1; i >= 0; i--) {
				if (input[i] == '-') {
					flips += b ?0:1;
					b = 1;
				}
				else {
					flips += b ?1:0;
					b = 0;
				}
			}
			fo << "Case #" << C << ": " << flips << "\n";
		}
	}
	fi.close();
	fo.close();
	return 0;
}
