#include <iostream>
#include <string>

bool get_one_input(int* state)
{
	char one_char;
	bool notyet = false;

	for (int i = 0; i < 16; ++i)
	{
		std::cin >> one_char;

		switch (one_char)
		{
			case 'X':
				state[i] = 1;
				break;
			case 'O':
				state[i] = 2;
				break;
			case 'T':
				state[i] = -1;
				break;
			case '.':
				state[i] = 3;
				notyet = true;
				break;
		}
	}

	//std::cin >> one_char; // for '\n'

	return notyet;
}

class Result { public: enum type { Xwon, Owon, Draw, Notyet }; };

Result::type decide_row(int* state)
{
	int decider;
	for (int i = 0; i < 4; ++i)
	{
		decider = 1;
		for (int j = 0; j < 4; ++j)
		{
			decider *= state[4*i + j];
		}

		if (decider == -8 || decider == 16)
		{
			return Result::Owon;
		}
		else if (decider == -1 || decider == 1)
		{
			return Result::Xwon;
		}
	}

	return Result::Notyet;
}

Result::type decide_column(int* state)
{
	int decider;
	for (int i = 0; i < 4; ++i)
	{
		decider = 1;
		for (int j = 0; j < 4; ++j)
		{
			decider *= state[i + 4*j];
		}

		if (decider == -8 || decider == 16)
		{
			return Result::Owon;
		}
		else if (decider == -1 || decider == 1)
		{
			return Result::Xwon;
		}
	}

	return Result::Notyet;
}

Result::type decide_diag(int* state)
{
	int decider;

	decider = state[0] * state[5] * state[10] * state[15];

	if (decider == -8 || decider == 16)
	{
		return Result::Owon;
	}
	else if (decider == -1 || decider == 1)
	{
		return Result::Xwon;
	}

	decider = state[3] * state[6] * state[9] * state[12];

	if (decider == -8 || decider == 16)
	{
		return Result::Owon;
	}
	else if (decider == -1 || decider == 1)
	{
		return Result::Xwon;
	}

	return Result::Notyet;
}

void print_one(int casen, Result::type result)
{
	switch (result)
	{
		case Result::Xwon:
			std::cout << "Case #" << casen << ": X won" << std::endl;
			return;
		case Result::Owon:
			std::cout << "Case #" << casen << ": O won" << std::endl;
			return;
		case Result::Draw:
			std::cout << "Case #" << casen << ": Draw" << std::endl;
			return;
		default:
			std::cout << "Case #" << casen << ": Game has not completed" << std::endl;
	}
}

int main()
{
	int cases;
	int casen = 0;
	std::cin >> cases;

	int state[16];
	bool notyet = true;
	
	while (cases--)
	{
		casen++;

		notyet = get_one_input(state);

		Result::type result = decide_row(state);
		if (result == Result::Xwon || result == Result::Owon)
		{
			print_one(casen, result);
			continue;
		}
		result = decide_column(state);
		if (result == Result::Xwon || result == Result::Owon)
		{
			print_one(casen, result);
			continue;
		}
		result = decide_diag(state);
		if (result == Result::Xwon || result == Result::Owon)
		{
			print_one(casen, result);
			continue;
		}

		if (notyet) print_one(casen, Result::Notyet);
		else print_one(casen, Result::Draw);
	}

	return 0;
}
