#include <iostream>
#include <fstream>
#include <string>



int computeNumberFlips(const std::string &stack)
{
	int numberFlips = 0;


	int nbPancakes = stack.length();
	bool *happyStack = new bool[nbPancakes];
	bool *newHappyStack = new bool[nbPancakes];

	for(std::string::size_type i = 0; i < nbPancakes; i++) {
		happyStack[i] = (stack[i] == '+');
	}

	int nbIteration = 0;
	while (true) {

		// std::cout << "Current stack: ";
		// for (int i = 0; i < nbPancakes; i++)
		// 	std::cout << (happyStack[i] ? '+' : '-');
		// std::cout << std::endl;

		// Find first pancake not like the first one
		int cutIndex = 0;
		bool isFirstPancakeHappy = happyStack[cutIndex];
		while (cutIndex < nbPancakes && happyStack[cutIndex] == isFirstPancakeHappy)
			cutIndex++;

		// std::cout << "Cut index: " << cutIndex << std::endl;
		if (cutIndex == nbPancakes) {
			// All pancakes are in the same order: If they are all unhappy, one last switch required
			if (isFirstPancakeHappy)
				return nbIteration;
			else
				return nbIteration + 1;
		}

		nbIteration++;

		for (int i = 0; i < cutIndex; i++)
			newHappyStack[i] = !isFirstPancakeHappy;
		for (int i = cutIndex; i < nbPancakes; i++)
			newHappyStack[i] = happyStack[i];

		// std::cout << "New stack: ";
		// for (int i = 0; i < nbPancakes; i++)
		// 	std::cout << (newHappyStack[i] ? '+' : '-');
		// std::cout << std::endl;


		// Switch stacks
		happyStack = newHappyStack;
		newHappyStack = happyStack;
//		std::cout << "====================" << std::endl;
	}



	return numberFlips;
}


int main(int argc, char *args[])
{
	std::ifstream input(args[1]);

	int nbCase;

	input >> nbCase;

	for (int curCase = 1; curCase <= nbCase; curCase++)
	{
		std::string stack;
		input >> stack;

		int result = computeNumberFlips(stack);
		std::cout << "Case #" << curCase << ": " << result << std::endl;
	}
	return 0;
}
