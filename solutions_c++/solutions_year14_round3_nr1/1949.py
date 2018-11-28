#include<iostream>
using namespace std;
class FEN
{
	long long B;
	long long gcd(long long A, long long B);
	void simplify();
public:
	long long A;
	int operator>(const FEN &);
	FEN &operator+=(const FEN &);
	FEN &operator-=(const FEN &);
	FEN &div2();
	FEN(long long, long long);
};
long long FEN::gcd(long long A, long long B)
{
	return (A == 0) ? B : gcd(B % A, A);
}
void FEN::simplify()
{
	long long Ci = gcd(A, B);
	A /= Ci;
	B /= Ci;
}
int FEN::operator>(const FEN &T)
{
	long long Ai = this->A * T.B;
	long long Bi = this->B * T.A;
	return (Ai >= Bi) ? 1 : 0;
}
FEN &FEN::operator+=(const FEN &T)
{
	long long Ai = this->A * T.B;
	long long Bi = this->B * T.A;
	long long Ci = this->B * T.B;
	A = Ai + Bi;
	B = Ci;
	this->simplify();
	return (*this);
}
FEN &FEN::operator-=(const FEN &T)
{
	long long Ai = this->A * T.B;
	long long Bi = this->B * T.A;
	long long Ci = this->B * T.B;
	A = Ai - Bi;
	B = Ci;
	this->simplify();
	return (*this);
}
FEN &FEN::div2()
{
	B *= 2;
	this->simplify();
	return (*this);
}
FEN::FEN(long long Ai, long long Bi)
{
	A = Ai;
	B = Bi;
	this->simplify();
}
int main()
{
	int T, Ti;
	Ti ^= Ti;
	cin >> T;
	while (Ti++ < T)
	{
		char ch;
		int Ai, Bi;
		cin >> Ai >> ch >> Bi;
		FEN want(Ai, Bi);
		FEN ruler(1, 1);
		int for_i = 0;
		int for_n = 41;
		while (for_i <= 40)
		{
			if (want.operator>(ruler))
			{
				want.operator-=(ruler);
				for_n = (for_i < for_n) ? for_i : for_n;
				if (want.A == 0) break;
			}
			ruler.div2();
			for_i++;
		}
		cout << "Case #" << Ti << ": ";
		if (for_i <= 40) cout << for_n << endl;
		else cout << "impossible" << endl;
	}
	return 0;
}