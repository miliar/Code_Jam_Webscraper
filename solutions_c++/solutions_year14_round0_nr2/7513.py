#include <fstream>
#include <iomanip>

int main()
{
	std::ifstream input("input-large.txt");
	std::ofstream output("output-large.txt");

	unsigned int total;
	input >> total;
	for (int i = 0; i < total; ++i)
	{
		double C, F, X;
		input >> C >> F >> X;

		double lastTime = X / 2;
		double cachedTime = C / 2;
		double time = cachedTime + X / (F + 2);
		unsigned int count = 1;
		while (time < lastTime)
		{
			lastTime = time;
			cachedTime += C / (count * F + 2);
			time = cachedTime + X / (++count * F + 2);
		}

		output << std::fixed;
		output << "Case #" << i + 1 << ": " << std::setprecision(7) <<
			lastTime << std::endl;
	}
}
