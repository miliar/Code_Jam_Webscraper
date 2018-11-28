#include "code_jam.hpp"
#include <string>
#include <unordered_map>
#include <algorithm>
#include <cmath>

typedef unsigned long long Int;

Int solve(Tokens& tokens)
{
	const auto machine1_max = tokens.next_token<Int>();
	const auto machine2_max = tokens.next_token<Int>();
	const auto user_max = tokens.next_token<Int>();

	//Brute force!

	Int result = 0;

	for(Int i = 0; i < machine1_max; ++i)
		for(Int j = 0; j < machine2_max; ++j)
			if((i & j) < user_max)
				++result;

	return result;
}

MAIN(solve)
