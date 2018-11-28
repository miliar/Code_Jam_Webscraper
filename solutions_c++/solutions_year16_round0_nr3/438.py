#include <fstream>
#include <cassert>
#include <iostream>
#include <vector>

static void
pushNumToVec(std::vector<int>& d, int a)
{
	while (a > 0) {
		d.push_back(a % 10);
		a /= 10;
	}
}

class superint
{
public:
	superint(int a);

	void multiply(int a);
	void inc(int a);
	void print(std::ostream& os) const;
private:
	std::vector<int> d_;
};

superint::superint(int a)
{
	pushNumToVec(d_, a);
}

void
superint::inc(int a)
{
	for (int i = 0; i < d_.size() && a > 0; ++i) {
		a += d_[i];
		d_[i] = a % 10;
		a /= 10;
	}

	pushNumToVec(d_, a);
}

void
superint::multiply(int a)
{
	int remain = 0;
	for (int i = 0; i < d_.size(); ++i) {
		remain += a * d_[i];
		d_[i] = remain % 10;
		remain /= 10;
	}
	pushNumToVec(d_, remain);
}

void
superint::print(std::ostream& os) const
{
	for (std::vector<int>::const_reverse_iterator i = d_.rbegin();
        i != d_.rend(); ++i) {
		os << (*i);
	}
}

std::ostream&
operator<<(std::ostream& os, const superint& s)
{
	s.print(os);
	return os;
}



int main()
{
	const int N = 32;
	const int J = 500;

	//const int N = 16;
	//const int J = 50;

	std::ofstream outfile("outfile.txt");
	outfile << "Case #1:" << std::endl;


	const int M = N / 2;
	const int K = M - 2;
	assert((1 << K) > J);

	std::vector<superint> factors;
	for (int i = 2; i <= 10; ++i) {
		superint a(1);
		for (int m = 0; m < M; ++m) {
			a.multiply(i);
		}

		a.inc(1);
		factors.push_back(a);
	}

	for (unsigned int j = 0; j < J; ++j) {
		std::string s;
		for (int k = 0; k < K; ++k) {
			s = (((j >> k) & 1) ? '1' : '0') + s;
		}

		outfile << '1' << s << "11" << s << '1';
		for (std::vector<superint>::const_iterator it = factors.begin();
			  it != factors.end(); ++it) {
			outfile << ' ' << (*it);
		}
		outfile << std::endl;
	}

	return 0;
}
