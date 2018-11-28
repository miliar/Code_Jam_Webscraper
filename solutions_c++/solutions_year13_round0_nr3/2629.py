#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solver {
private:
	vector<bool> fancys, fas;
	bool isFancy(int x)
	{
		stringstream ss;
		ss<<x;
		string s(ss.str());
		string t(s);
		reverse(t.begin(), t.end());

		return s == t;
	}
public:
	Solver(int fasMax)
	: fancys(fasMax + 100, false),
	  fas(fasMax + 100, false)
	{
		for (int i = 1; i < fancys.size(); ++i) {
			fancys[i] = isFancy(i);
		}
		const int baseMax = (int)sqrt((double)fasMax);
		for (int i = 1; i <= baseMax; ++i) {
			if (fancys[i] && fancys[i * i])
				fas[i * i] = true;
		}
		
	}

	int solve(int A, int B)
	{
		int res = 0;
		for (int i = A; i <= B; ++i) {
			if (fas[i])
				res++;
		}
		return res;
	}
};

int main()
{
	int T;
	cin>>T;

	Solver solver(2000);

	for (int i = 0; i < T; ++i) {
		int A, B;
		cin>>A>>B;
		cout<<"Case #"<<(i + 1)<<": "<<solver.solve(A, B)<<endl;
	}

	return 0;
}
