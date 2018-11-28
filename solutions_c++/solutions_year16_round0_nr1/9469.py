#include <fstream>
#include <string>

class MicroBool {//why waste a byte for each bool, when you can have 8 bools in a byte?
private:
	uint16_t data;
public:
	void set(uint8_t i, bool b = 1) {
		this->data = data | (b << i);
	}
	void zero() {
		this->data = 0;
	}
	bool full() const {
		return (this->data == 1023 ? true : false); // if all are set
	}
	MicroBool() {
		this->data = 0;
	}
};

int main(void) {
	std::ifstream fi("A-large.in");
	std::ofstream fo("A-large.out");
	if (fi.is_open())
	if (fo.is_open()) {
		std::string input;//current line
		std::getline(fi, input);
		auto T = std::stoi(input);//number of cases
		MicroBool mb;//keeps track of all nubmers seen
		for (auto C = 1; C <= T; C++) {//set of cases
			mb.zero();
			std::getline(fi, input);
			uint32_t S = std::stoi(input);//original number on sheep
			for (uint32_t N = 1; !mb.full() && N <= 1000000; N++) {//multiple of each case
				input = std::to_string(S * N);//string of number on sheep
				for (auto i = 0; i < input.length(); i++)
					mb.set(input[i] - 48);
			}
			fo << "Case #" << C << ": " << (mb.full() ? input : "INSOMNIA") << "\n";
		}
	}
	fi.close();
	fo.close();
	return 0;
}
