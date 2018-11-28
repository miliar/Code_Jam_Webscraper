#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

typedef uint32_t u32;
typedef int64_t i64;

void flip(std::string & s, i64 count)
{
	if (count < 0)
		return;
	size_t const to = size_t(count);
	for (size_t i = 0; i < to && i < s.size(); ++i)
		s[i] = '-' == s[i] ? '+' : '-';
}

int main()
{
	using namespace std;

	ifstream in("b.in");
	ofstream out("b.out");

	u32 T;
	in >> T;

	for (u32 i = 0; i < T; ++i)
	{
		string line;
		in >> line;
		out << "Case #" << (i + 1) << ": ";

		u32 res = 0;
		for (i64 last = line.rfind('-'); string::npos != last; last = line.rfind('-', last), ++res)
		{
			i64 const minuses = std::count(line.begin(), line.begin() + last + 1, '-');
			flip(line, minuses * 2 >= last + 1 ? last + 1 : line.rfind('+', last) + 1);
		}
		out << res << endl;
	}
	return 0;
}
