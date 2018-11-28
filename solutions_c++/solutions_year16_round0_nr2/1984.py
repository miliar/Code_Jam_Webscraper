#include <iostream>
#include <string>
#include <vector>

inline void initStack(std::vector<bool> &stack, std::string stackString) 
{
	int size = stack.size();
	if (stackString.length() != size) { std::cerr << "Assert!" << std::endl; }
	for (int i = 0; i < size; i++) { // reversing input string too
		stack[i] = (stackString[size-i-1] == '+') ? true : false; // F Flat, T Smiley
	}
}
inline bool checkStack(std::vector<bool> &stack) 
{
	int size = stack.size();
	for (int i = 0; i < size; i++) {
		if (stack[i] == false) { return false; }
	}
	return true; // All Smileys
}
inline void printStack(std::vector<bool> &stack)
{
	int size = stack.size();
	for (int i = size - 1; i >= 0; i--) {
		std::cout << (stack[i] == true ? "+" : "-");
	}
	std::cout << std::endl;
}
inline void flipStack(int &flips, std::vector<bool> &stack, const int idx) 
{
	const int size = stack.size();
	for (int i = idx, topIdx = size -1; i <= topIdx; i++, topIdx--) 
	{
		// Swap and invert
		bool temp = !stack[i];
		stack[i] = !stack[topIdx];
		stack[topIdx] = temp;
	}
	flips++;
}

int optimalFlips(const std::string &stackString)
{
	int flips = 0;
	const int size = stackString.length();
	std::vector<bool> stack(size);
	initStack(stack, stackString);
	// std::cout << "BEFORE "; printStack(stack);
	// Greedy Algo:
	// all consecutive +s and -s are equiv to just one pancake
	// if bottom +ve reduce concentrate on reduced stack
	// if bottom -ve and top -ve flip full stack
	// if bottom -ve and top -ve flip consecutive -ves on the top
	//		followed by flip full stack
	int bottomIdx = 0; 
	while (bottomIdx < size) {
		if (stack[bottomIdx] == true) { bottomIdx++; continue; }
		int topIdx = size - 1;
		if (stack[topIdx] == false) { flipStack(flips, stack, bottomIdx); bottomIdx++; continue; }
		while (stack[topIdx] == true) { topIdx--; }
		flipStack(flips, stack, ++topIdx);
		flipStack(flips, stack, bottomIdx); bottomIdx++;
	}
	// std::cout << "AFTER "; printStack(stack);
	if (!checkStack(stack)) { std::cout << "CHECK RESULT!" << std::endl; }
	return flips;
}

int main()
{
	int NumTests = 0;
	std::cin >> NumTests;
	for (int i = 1; i <= NumTests;i++) {
		std::string stackString; std::cin >> stackString;
		int result = optimalFlips(stackString);
		std::cout << "Case #" << i << ": " << result << std::endl;
	}
}