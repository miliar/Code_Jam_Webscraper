#include "com.hpp"

class Notation
{
public:
	Notation(int r) :radix_(r),val_()
	{
	}
	void bitTo(ll n)
	{
		while (n)
		{
			int m = __builtin_ctz(n&-n);
			val_ += pow(radix_, m);
			n &= n - 1;
		}
	}
	ll toDecimal()const
	{
		return val_;
	}
	ll getDivisor()const
	{
		ll v = val_;
		for (ll d = 2; d < v;++d)
		{
			if (v%d == 0)return d;
		}
		return 0;
	}
private:
	ll val_;
	int radix_;

};
static string toBin(int n, int len)
{
	string bin(len, '0');
	while (n)
	{
		int m = __builtin_ctz(n&-n);
		bin[len-m-1] = '1';
		n &= n - 1;
	}
	return bin;
}
static auto solve = []()
{
	INPUT(ll, N);
	INPUT(ll, J);
	ll r = 0;
	bool iscontinue = false;
	for (int i = (1 << (N - 1)); i < (1 << N)-1; ++i)
	{
		if ((i & 1) == 0)continue;
		Notation n[] = { 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		if (![&]()
		{
			for (auto& j : n)
			{
				j.bitTo(i);
				if (isPrime(j.toDecimal()))
				{
					return false;
				}
			}
			return true;
		}()
			)continue;

		cout << toBin(i, N);
		for (auto& j : n)
		{
			cout << " " << j.getDivisor();
		}
		cout << endl;
		if (!--J)
		{
			break;
		}
	}

	return r;
};

#define IONAME "2016Qual/C/C-small-attempt0"

int main(int argv, char* argc[])
{

	ifstream in(IONAME".in");
	cin.rdbuf(in.rdbuf());
	ofstream ofs(IONAME".out", ios_base::out);
	cout.rdbuf(ofs.rdbuf());
	INPUT(int, caseNum);
	for (int i = 0; i < caseNum; ++i)
	{
		cout << "Case #" << i + 1 << ": " << endl;
		solve();

	}
	return 0;
}