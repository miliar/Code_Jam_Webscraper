#include <exception>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>

template<typename T>
void validate(T parameter, T min, T max) {
	if(parameter < min || parameter > max)
		throw std::exception("invalid parameter");
}
typedef long long ll;

struct Source {
	double Rate; //liters per second
	double C; //celsium temperature
};

class Problem {
	int N;
	double V, X;
	Source* sources;
	double minC, maxC;
public:
	void read(std::istream& in) {
		minC = 100.;
		maxC = 0.;

		in >> N >> V >> X;
		validate(N, 1, 100);
		validate(V, 0.0001, 10000.0);
		validate(X, 0.1, 99.9);
		sources = new Source[N];
		for(int i = 0; i < N; ++i) {
			in >> sources[i].Rate >> sources[i].C;
			validate(sources[i].Rate, 0.0001, 10000.0);
			validate(sources[i].C, 0.1, 99.9);
			if(sources[i].C < minC) minC = sources[i].C;
			if(sources[i].C > maxC) maxC = sources[i].C;
		}
	}
	void solve_print(std::ostream& out) {
		if(X < minC || X > maxC) {
			out << "IMPOSSIBLE";
		} else {
			out << solve();
		}
	}
private:
	double solve() {
		if(N == 1) {
			return V / sources[0].Rate;
		}
		else if(N == 2) {
			if(sources[0].C == sources[1].C) {//double got directly from input, same number expected to be exactly equal
				return V / (sources[0].Rate + sources[1].Rate);
			}
			if(X == sources[0].C) {
				return V / sources[0].Rate;
			}
			else if(X == sources[1].C) {
				return V / sources[1].Rate;
			}

			double x0 = V * (X - sources[1].C) / (sources[0].C - sources[1].C) / sources[0].Rate;
			double x1 = V * (X - sources[0].C) / (sources[1].C - sources[0].C) / sources[1].Rate;
			return std::max(x0, x1);
		}
		return 0;
	}
};


int main(int argc, char** argv) {
	std::istream* in = &std::cin;
	std::ostream* out = &std::cout;
	if(argc > 1) {
		in = new std::ifstream(argv[1]);

		std::string fout(argv[1]);
		int ext = fout.rfind('.');
		fout = fout.substr(0, ext);
		fout += ".out";
		out = new std::ofstream(fout);
	}

	try {
		int T;
		(*in) >> T;
		validate(T, 1, 100);
		(*out) << std::setprecision(9) << std::fixed;

		for(int iT = 1; iT <= T; ++iT) {
			Problem p;
			p.read(*in);
			(*out) << "Case #" << iT << ": ";
			p.solve_print(*out);
			(*out) << std::endl;
		}

	}
	catch(std::exception& x) {
		std::cerr << "something went wrong: " << x.what();
	}
	catch(...) {
		std::cerr << "unknown exception";
	}
	return 0;
}