#include "com.hpp"


static auto solve = [](string N)
{
	ll r = 0;
	for (auto i = N.begin(), j = ++N.begin(); j != N.end(); ++i, ++j)
	{
		if (*i != *j)
		{
			++r;
		}
	}
	if (*N.rbegin() == '-')
	{
		++r;
	}
	return r;
};

#define IONAME "2016Qual/B/B-large"

int main(int argv, char* argc[])
{

	ifstream in(IONAME".in");
	cin.rdbuf(in.rdbuf());
	ofstream ofs(IONAME".out", ios_base::out);
	cout.rdbuf(ofs.rdbuf());
	INPUT(int, caseNum);
	for (int i = 0; i < caseNum; ++i)
	{
		INPUT(string, N);
		cout << "Case #" << i + 1 << ": " << solve(N) << endl;

	}
	return 0;
}