#include <fstream>
#include <map>

int main(int argc, char** argv)
{
	std::ifstream ifs(argv[1]);
	std::ofstream ofs(argv[2]);
	int T;
	ifs >> T;
	for (int i = 1; i <= T; ++i) {
		int num;
		std::map<int, int> digits;
		ifs >> num;
		int multiplier = 1;
		bool insomnia = false;
		if (num == 0) {
			insomnia = true;
		}
		while (!insomnia) {
			int mult_res = num * multiplier;
			while (mult_res != 0) {
				digits[mult_res % 10];
				mult_res /= 10;
			}
			if (digits.size() == 10) {
				break;
			}
			multiplier++;
		}
		ofs << "Case #" << i << ": ";
		if (insomnia)
			ofs << "INSOMNIA";
		else
			ofs << multiplier * num;
		ofs << std::endl;
	}
}
