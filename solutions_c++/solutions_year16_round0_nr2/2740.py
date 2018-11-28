/**
 * @name Revenge of the Pancakes
 */
#include <iostream>
#include <string>
using namespace std;

/**
 * Greedy pancake 'sorting' yields the optimal number of steps.
 */
int solve(const string& pancakes)
{
	size_t flips = 0;

	// Invariant: the [0, idx) pancakes are all + or -, determined
	// by pancakes[idx]
	for (size_t idx = 1; idx < pancakes.size(); ++idx)
	{
		// Skip through non-transitions
		if (pancakes[idx] == pancakes[idx - 1])
			continue;

		// Transition, we flip the 0..idx-1 pancakes to make them
		// the same as the idx pancake
		++flips;
	}

	// If the last pancake was -, flip everything to +
	if (pancakes[pancakes.size() - 1] == '-')
		++flips;

	return flips;
}

int main()
{
	size_t num_cases;
	cin >> num_cases;

	for (size_t c = 1; c <= num_cases; ++c)
	{
		string pancakes;
		cin >> pancakes;

		cout << "Case #" << c << ": " << solve(pancakes) << endl;
	}
}
