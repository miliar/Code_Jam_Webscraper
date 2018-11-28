#include <iostream>
#include <string>

#define FLIP(x) ((x) == '+' ? '-' : '+')

unsigned long int required_flips(std::string state, int idx, char goalSide)
{
    if (idx == 0)
        return (state[idx] == goalSide) ? 0 : 1;
    else if (state[idx] == goalSide)
        return required_flips(state, idx - 1, goalSide);
    else // state[idx] != goalSide
        return 1 + required_flips(state, idx - 1, FLIP(goalSide));
}

int main() {
    std::string Tstr;
    std::cin >> Tstr;
	unsigned int T = std::stoi(Tstr);

	for (unsigned int t = 1; t <= T; t++) 
	{
        std::string state;
        std::cin >> state;

        unsigned long int flips = required_flips(state, state.length() - 1, '+');
        std::cout << "Case #" << t << ": " << flips << std::endl;
	}
}
