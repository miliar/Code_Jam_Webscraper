#include <cstdio>
#include <string>

using namespace std;

struct Quatemions
{
	enum class Character
	{
		_1,
		i,
		j,
		k
	};
	
	Quatemions(char _char)
		: minus(false)
	{
		switch (_char)
		{
		case '1':
			character = Character::_1;
			break;
		case 'i':
			character = Character::i;
			break;
		case 'j':
			character = Character::j;
			break;
		case 'k':
			character = Character::k;
			break;
		}
	}

	bool operator==(const Quatemions& right)
	{
		return minus == right.minus && character == right.character;
	}

	Quatemions& operator*=(const Quatemions& right)
	{
		minus = (minus != right.minus);

		switch (character)
		{
		case Character::_1:
			character = right.character;
			break;
		case Character::i:
			switch (right.character)
			{
			case Character::i:
				character = Character::_1;
				minus = !minus;
				break;
			case Character::j:
				character = Character::k;
				break;
			case Character::k:
				character = Character::j;
				minus = !minus;
				break;
			}
			break;
		case Character::j:
			switch (right.character)
			{
			case Character::i:
				character = Character::k;
				minus = !minus;
				break;
			case Character::j:
				character = Character::_1;
				minus = !minus;
				break;
			case Character::k:
				character = Character::i;
				break;
			}
			break;
		case Character::k:
			switch (right.character)
			{
			case Character::i:
				character = Character::j;
				break;
			case Character::j:
				character = Character::i;
				minus = !minus;
				break;
			case Character::k:
				character = Character::_1;
				minus = !minus;
				break;
			}
			break;
		}
		
		return *this;
	}
	
	Character character;
	bool minus;
};

char chars[10010];

int Find(const string& totalChars, int start, const Quatemions& desired)
{
	int len = totalChars.length();
	
	Quatemions to('1');
	for (int iter=start; iter<len; ++iter)
	{
		to *= totalChars[iter];
		if (to == desired)
		{
			return iter;
		}
	}

	return -1;
}

bool IsPossible(const string& totalChars)
{
	bool isPossible = true;
	int toI = Find(totalChars, 0, Quatemions('i'));
	if (toI < 0)
	{
		return false;
	}

	int toJ = Find(totalChars, toI+1, Quatemions('j'));
	if (toJ < 0)
	{
		return false;
	}

	Quatemions toEnd('1');
	for (int iter=toJ+1; iter<totalChars.length(); ++iter)
	{
		toEnd *= totalChars[iter];
	}

	return toEnd == Quatemions('k');
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int caseCount=1; caseCount<=t; ++caseCount)
	{
		int L, X;
		scanf("%d %d %s", &L, &X, chars);

		string totalChars;
		for (int i=0; i<X; ++i)
			totalChars += chars;

		printf("Case #%d: %s\n", caseCount, IsPossible(totalChars) ? "YES" : "NO");
	}
	
	return 0;
}