#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <functional>
#include <algorithm>

class State
{
public:
	std::vector<bool> Pancakes;
	unsigned int Flips;
	unsigned int Sad;

	State()
	{

	}
	State(const std::vector<bool> Pancakes, const unsigned int Flips, const unsigned int Sad)
	{
		this->Pancakes = Pancakes;
		this->Flips = Flips;
		this->Sad = Sad;
	}
};

struct HeuristicCompare
{
	inline bool operator() (const State *One, const State *Two) const
	{
		return One->Flips > Two->Flips;
	}
};

struct OrderCompare
{
	inline bool operator() (const State &One, const State &Two) const
	{
		for (unsigned int x = 0; x < One.Pancakes.size(); x++)
		{
			if (One.Pancakes[x] && !Two.Pancakes[x])
				return true;
			else if (!One.Pancakes[x] && Two.Pancakes[x])
				return false;
		}
		return false;
	}
};

void Flip(std::vector<bool> &Pancakes, const unsigned int Amount)
{
	if (Amount > Pancakes.size())
		throw std::exception();

	std::reverse(Pancakes.begin(), Pancakes.begin() + Amount);
	for (unsigned int x = 0; x < Amount; x++)
		Pancakes[x] = !Pancakes[x];
}

int main(int argc, char *argv[])
{
	std::ifstream In("In.txt");
	std::ofstream Out("Out.txt");

	unsigned int T;
	In >> T;

	for (unsigned int t = 0; t < T; t++)
	{
		std::string Line;
		In >> Line;
		std::vector<bool> Pancakes;
		Pancakes.resize(Line.size());
		unsigned int SadCount = 0;
		for (unsigned int x = 0; x < Line.size(); x++)
		{
			Pancakes[x] = Line[x] == '+';
			if (!Pancakes[x])
				SadCount++;
		}

		State Root(Pancakes, 0, SadCount);
		std::set<State, OrderCompare> Visited;
		Visited.emplace(Root);

		std::priority_queue<const State*, std::vector<const State*>, HeuristicCompare> States;
		States.push(&Root);

		while (States.top()->Sad > 0)
		{
			const State *Top = States.top();
			States.pop();

			unsigned int Happy = 0;
			for (unsigned int x = 0; x < Top->Pancakes.size(); x++)
			{
				if (!Top->Pancakes[x])
					Happy++;

				State New = State(Top->Pancakes, Top->Flips + 1, Top->Sad);
				Flip(New.Pancakes, x + 1);
				New.Sad += (x + 1 - Happy) - Happy;

				std::pair<std::set<State, OrderCompare>::iterator, bool> Result = Visited.emplace(New);
				if (Result.second)
					States.push(&(*Result.first));
			}
		}

		Out << "Case #" << t + 1 << ": " << States.top()->Flips << std::endl;
	}


	In.close();
	Out.close();

	return 0;
}