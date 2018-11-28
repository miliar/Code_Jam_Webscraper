
#include <iostream>
#include <string>

int solve(int maxS, std::string values)
{
	int shyness = 0, sakura = 0;
	for (int i = 0; i <= maxS; ++i) {
		int people = values.at(i) - '0';
		if (i > shyness && people > 0) {
			sakura += i - shyness;
			shyness += i - shyness;
		}
		shyness += people;
	}
	return sakura;
}


int main() 
{
	int T;
	std::cin >> T;
	for (int i = 1; i <= T; ++i) {
		std::string maxSStr, audiences;
		std::cin >> maxSStr;
		std::cin >> audiences;
		int result = solve(std::stoi(maxSStr), audiences);
		std::cout << "Case #" << i << ": " << result << std::endl;
	}
	return 0;
}

