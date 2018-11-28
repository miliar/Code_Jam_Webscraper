#include <iostream>
#include <fstream>
#include <cstdint>
#include <algorithm>

#define READFROMFILE
#define WRITETOFILE

enum Quat : char { Error = 0, p1 = 1, pI, pJ, pK, m1, mI, mJ, mK };

struct RepeatedString
{
	Quat value[10001];
	int length;
	uint64_t repeatCount;
};

RepeatedString repeatedStr;
Quat stringResult[10002];
Quat stringLastResult;

const Quat mul[9][9] = {
	{ (Quat)0, (Quat)0, (Quat)0, (Quat)0, (Quat)0, (Quat)0, (Quat)0, (Quat)0, (Quat)0 },
	{ (Quat)0, p1, pI, pJ, pK, m1, mI, mJ, mK },
	{ (Quat)0, pI, m1, pK, mJ, mI, p1, mK, pJ },
	{ (Quat)0, pJ, mK, m1, pI, mJ, pK, p1, mI },
	{ (Quat)0, pK, pJ, mI, m1, mK, mJ, pI, p1 },

	{ (Quat)0, m1, mI, mJ, mK, p1, pI, pJ, pK },
	{ (Quat)0, mI, p1, mK, pJ, pI, m1, pK, mJ },
	{ (Quat)0, mJ, pK, p1, mI, pJ, mK, m1, pI },
	{ (Quat)0, mK, mJ, pI, p1, pK, pJ, mI, m1 }
};

const Quat minus[9] = { (Quat)0, m1, mI, mJ, mK, p1, pI, pJ, pK };

inline Quat operator*(Quat lhs, Quat rhs)
{
	return mul[lhs][rhs];
}

inline Quat operator/(Quat lhs, Quat rhs)
{
	return mul[minus[rhs]][lhs];
}

struct RepeatedStringIterator
{
	int pos;
	uint64_t repeatedCount;

	RepeatedStringIterator() : pos(-1), repeatedCount(1ULL)
	{
	}

	RepeatedStringIterator(const RepeatedStringIterator &rhs, uint64_t usedRepeatedCount = 0) : pos(rhs.pos), repeatedCount(rhs.repeatedCount - usedRepeatedCount)
	{
	}

	inline Quat get()
	{
		return repeatedStr.value[pos];
	}

	inline bool hasNext()
	{
		return pos + 1 < repeatedStr.length;
	}

	inline bool next()
	{
		pos++;
		return pos < repeatedStr.length;
	}

	Quat getNext()
	{
		if (next())
			return repeatedStr.value[pos];
		else
			return Error;
	}

	Quat getNextPrecalced()
	{
		if (next())
			return stringResult[pos];
		else
			return Error;
	}

	inline bool isEnd()
	{
		return pos >= repeatedStr.length;
	}
};

struct Substring
{
	Quat result;
	bool leftAttachable;
	bool rightAttachable;
	int leftAttachedCount;
	int rightAttachedCount;

	Substring(Quat result, bool leftAttachable, bool rightAttachable, int leftAttachedCount = 0, int rightAttachedCount = 0)
		:result(result), leftAttachable(leftAttachable), rightAttachable(rightAttachable), leftAttachedCount(leftAttachedCount), rightAttachedCount(leftAttachedCount)
	{
	}

	inline int getAttachedCount() const
	{
		return leftAttachedCount + rightAttachedCount;
	}

	inline bool isLeftAttachable() const
	{
		return leftAttachable && (leftAttachedCount < 4);
	}

	inline bool isRightAttachable() const
	{
		return rightAttachable && (rightAttachedCount < 4);
	}

	Substring attachLeft() const
	{
		Substring newSubstr(*this);
		newSubstr.leftAttachedCount++;

		newSubstr.result = stringLastResult * newSubstr.result;

		return newSubstr;
	}

	Substring attachRight() const
	{
		Substring newSubstr(*this);
		newSubstr.rightAttachedCount++;

		newSubstr.result = newSubstr.result * stringLastResult;

		return newSubstr;
	}
};


bool test(Substring &left, Substring &middle, Substring &right, uint64_t repeatsLeft)
{
	if ((repeatsLeft) % 4 == 0)
	{
		if (left.result == pI && middle.result == pJ && right.result == pK)
			return true;
		if (repeatsLeft == 0)
			return false;
	}
	//uint64_t totalUsedRepeats = left.getAttachedCount() + middle.getAttachedCount() + right.getAttachedCount();

	if (left.isLeftAttachable() && test(left.attachLeft(), middle, right, repeatsLeft - 1)) return true;
	if (left.isRightAttachable() && test(left.attachRight(), middle, right, repeatsLeft - 1)) return true;

	if (middle.isLeftAttachable() && test(left, middle.attachLeft(), right, repeatsLeft - 1)) return true;
	if (middle.isRightAttachable() && test(left, middle.attachRight(), right, repeatsLeft - 1)) return true;

	if (right.isLeftAttachable() && test(left, middle, right.attachLeft(), repeatsLeft - 1)) return true;
	if (right.isRightAttachable() && test(left, middle, right.attachRight(), repeatsLeft - 1)) return true;

	return false;
}


// [~~1~~/ /~~2~~] [~~~~~~~~~]
bool handleSubstrings(Quat first, Quat second)
{
	Quat third = stringLastResult;
	// third is at leftmost
	if (third == pI && test(Substring(third, false, false), Substring(first, true, false), Substring(second, false, true), repeatedStr.repeatCount - 2))
		return true;
	// third is at rightmost
	if (third == pK && test(Substring(first, true, false), Substring(second, false, true), Substring(third, false, false), repeatedStr.repeatCount - 2))
		return true;

	third = minus[third];
	// third is at leftmost
	if (third == pI && test(Substring(third, false, false), Substring(first, true, false), Substring(second, false, true), repeatedStr.repeatCount - 4))
		return true;
	// third is at rightmost
	if (third == pK && test(Substring(first, true, false), Substring(second, false, true), Substring(third, false, false), repeatedStr.repeatCount - 4))
		return true;
	
	return false;
}

// [~1~/ /~2~/ /~3~]
bool handleSubstrings(Quat first, Quat second, Quat third)
{
	return second == pJ && test(Substring(first, true, false), Substring(second, false, false), Substring(third, false, true), repeatedStr.repeatCount - 1);
}

// [~~1~~/ /~~2~~][~~3~~/ /~~4~~]
bool handleSubstrings(Quat first, Quat second, Quat third, Quat fourth)
{
	Quat repeatedPart = p1;
	int repeatLimit = 4ULL > repeatedStr.repeatCount - 2ULL ? (int)repeatedStr.repeatCount - 2 : 4;
	for (int i = 0; i < repeatLimit; i++)
	{
		Quat middle = second * repeatedPart * third;
		if (middle == pJ && test(Substring(first, true, false), Substring(middle, false, false), Substring(fourth, false, true), repeatedStr.repeatCount - 2 - i))
			return true;
		repeatedPart = repeatedPart * stringLastResult;
	}

	return false;
}


bool split()
{
	Quat left = p1;
	Quat right = stringLastResult;

	RepeatedStringIterator it;
	while (it.hasNext())
	{
		Quat next = it.getNext();
		left = left * next;
		right = right / next;

		// split the string into 2 parts
		if (repeatedStr.repeatCount > 1)
		{
			if (handleSubstrings(left, right))
				return true;
		}

		// split last substring into 2 parts so that we have 3 substrings
		{
			Quat middle = p1;
			Quat rightSplitted = right;

			RepeatedStringIterator it2(it);

			while (it2.hasNext())
			{
				Quat next2 = it2.getNext();
				middle = middle * next2;
				rightSplitted = rightSplitted / next2;

				if (handleSubstrings(left, middle, rightSplitted))
					return true;
			}
		}

		// split another string into 2 parts so that we have 4 substrings
		if (repeatedStr.repeatCount > 1)
		{
			Quat secondLeft = p1;
			Quat secondRight = stringLastResult;

			RepeatedStringIterator it2;

			while (it2.hasNext())
			{
				Quat next2 = it2.getNext();
				secondLeft = secondLeft * next2;
				// split the string into 2 parts
				secondRight = secondRight / next2;

				if (handleSubstrings(left, right, secondLeft, secondRight))
					return true;
				//if (handleSubstrings(secondLeft, secondRight, left, right))
				//	return true;
			}
		}
	}
	return false;
}

int main()
{
	int numOfTestCases;

#ifdef READFROMFILE
	std::ifstream input("ProblemC.in", std::ifstream::in);
#else
	std::istream &input = std::cin;
#endif

#ifdef WRITETOFILE
	std::ofstream output("ProblemC.out", std::ofstream::out);
#else
	std::ostream &output = std::cout;
#endif

	input >> numOfTestCases;

	for (int testCase = 1; testCase <= numOfTestCases; testCase++)
	{
		input >> repeatedStr.length >> repeatedStr.repeatCount;


		char q;
		for (int i = 0; i < repeatedStr.length; i++)
		{
			input >> q;
			switch (q)
			{
			case 'i': repeatedStr.value[i] = pI; break;
			case 'j': repeatedStr.value[i] = pJ; break;
			case 'k': repeatedStr.value[i] = pK; break;
			}
		}

		stringResult[0] = repeatedStr.value[0];
		for (int pos = 1; pos < repeatedStr.length; pos++)
		{
			stringResult[pos] = stringResult[pos - 1] * repeatedStr.value[pos];
		}

		stringLastResult = stringResult[repeatedStr.length - 1];

		//verify();
		output << "Case #" << testCase << ": " << (split() ? "YES" : "NO") << std::endl;
		std::cout << testCase << ": Done!" << std::endl;
	}
}