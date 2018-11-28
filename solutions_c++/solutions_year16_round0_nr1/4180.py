#include "com.hpp"


static auto solve = [](ll N)
{
	if (N == 0)return string("INSOMNIA");
	ll n = N;
	ll r = 0;
	bool a[10] = {};
	while (++r)
	{
		string t(to_string(N*r));
		sort(t.begin(), t.end());
		auto end = unique(t.begin(), t.end());
		for (auto i = t.begin(); i != end;++i)
		{
			a[*i-'0'] = true;
		}
		if (all_of(a, a + 10, [](int i){ return i; }))
			return to_string(N*r);
	}
};

#define IONAME "2016Qual/A/A-large"

int main(int argv, char* argc[])
{

	ifstream in(IONAME".in");
	cin.rdbuf(in.rdbuf());
	ofstream ofs(IONAME".out", ios_base::out);
	cout.rdbuf(ofs.rdbuf());
	INPUT(int, caseNum);
	for (int i = 0; i < caseNum; ++i)
	{
		INPUT(int, N);
		cout << "Case #" << i + 1 << ": " << solve(N) << endl;

	}
	return 0;
}