#include <algorithm>
#include <iostream>
#include <set>
#include <iterator>

using namespace std;

static const int BAD_MAGICIAN = 0;
static const int VOLUNTEER_CHEATED = -1;

int CalculateCase(istream& in);
void CalculateAll(istream& in, ostream& out);

int main()
{
	CalculateAll(cin, cout);
	return 0;
}

void CalculateAll(istream& in, ostream& out)
{
	int T;
	in >> T;
	for (int t = 0; t < T; ++t)
	{
		out << "Case #" << t + 1 << ": ";
		const int result = CalculateCase(in);
		switch (result)
		{
		case BAD_MAGICIAN:
			out << "Bad magician!" << endl;
			break;
		case VOLUNTEER_CHEATED:
			out << "Volunteer cheated!" << endl;
			break;
		default:
			out << result << endl;
		}
	}
}

set<int> GetRow(int choice, istream& in)
{
	set<int> result;
	for (int row = 1; row <= 4; ++row)
	{
		int n[4];
		for (int i = 0; i < 4; ++i)
		{
			in >> n[i];
		}
		if (row == choice)
		{
			result.insert(&n[0], &n[4]);
		}
	}
	return result;
}

int CalculateCase(istream& in)
{
	int choice1;
	in >> choice1;
	const set<int> set1(GetRow(choice1, in));
	int choice2;
	in >> choice2;
	const set<int> set2(GetRow(choice2, in));
	set<int> options;
	set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(), inserter(options, options.end()));
	int result;
	switch (options.size())
	{
	case 0:
		result = VOLUNTEER_CHEATED;
		break;
	case 1:
		result = *options.begin();
		break;
	default:
		result = BAD_MAGICIAN;
	}
	return result;
}
