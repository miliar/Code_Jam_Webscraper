#include <iostream>
#include <iomanip>

int main() {
	int z;
	scanf("%d", &z);

	for (int i=1; i<=z; i++) {
		double C,F,X;

		std::cin >> C >> F >> X;

		double result = 0.0;

		double P = 2.0;

		while (X/P - C/P - X/(P+F) > 0.0000001) {
			result += C/P;
			P += F;

			// std::cout << C << " F=" << F << " X=" << X << " P=" << P << std::endl;
		}

		result+=X/P;

		std::cout << "Case #" << i << ": " << std::setprecision(10) << result << std::endl;
	}
}