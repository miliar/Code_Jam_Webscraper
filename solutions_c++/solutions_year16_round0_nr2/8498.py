#include <fstream>
#include <vector>

size_t putPancakesFaceUp(std::vector<bool>& pancakes)
{
	size_t res = 0;
	bool allFaceUp = false;
	const size_t pancakesNumber = pancakes.size();
	while (!allFaceUp)
	{
		size_t liftPancakesNumber = 1;
		for (size_t i = 1; i < pancakesNumber; ++i)
		{
			if (pancakes[i] == pancakes[i - 1])
			{
				++liftPancakesNumber;
			}
			else
			{
				break;
			}
		}

		if (pancakesNumber == liftPancakesNumber && true == pancakes[0])
		{
			allFaceUp = true;
		}
		else
		{
			for (size_t i = 0; i < liftPancakesNumber; ++i)
			{
				pancakes[i] = !pancakes[i];
			}
			++res;
		}
	}
	return res;
}

void main()
{
	std::ifstream in("D:\\GoogleCodeJam2016\\input.txt");
	std::ofstream out("D:\\GoogleCodeJam2016\\output.txt");

	size_t count = 0;
	in >> count;
	if (0 > count)
	{
		count = 0;
	}

	for (size_t i = 0; i < count && !in.eof(); ++i)
	{
		char sequence[101] = "";
		std::vector<bool> pancakes;
		in >> sequence;
		for (size_t i = 0; i < 101, sequence[i] != '\0'; ++i)
		{
			bool pancake = (sequence[i] == '+') ? true : false;
			pancakes.push_back(pancake);
		}

		const size_t res = putPancakesFaceUp(pancakes);

		out << "Case #" << i + 1 << ": ";
		out << res;
		out << std::endl;
	}

	in.close();
	out.close();
}