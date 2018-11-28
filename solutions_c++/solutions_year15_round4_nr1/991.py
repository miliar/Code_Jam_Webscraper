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

enum Tcell {
	empty,
	up,
	down,
	right,
	left
};

class Problem {
	int R, C;
	Tcell* data;
	Tcell& cell(int x, int y) { return data[x*R + y]; }
public:
	void read(std::istream& in) {
		in >> R >> C;
		validate(R, 1, 100);
		validate(C, 1, 100);
		data = new Tcell[R*C];
		for(int i = 0; i < R; ++i) {
			std::string row;
			in >> row;
			for(int j = 0; j < C; ++j) {
				Tcell& target = cell(j, i);
				switch(row[j]) {
				case '.': target = empty; break;
				case '^': target = up; break;
				case 'v': target = down; break;
				case '<': target = left; break;
				case '>': target = right; break;
				default: throw std::exception("unknown cell");
				}
			}
		}
	}
	void solve_print(std::ostream& out) {
		int r = solve();
		if(-1 == r) out << "IMPOSSIBLE";
		else out << r;
	}
private:
	int solve() {
		int badarrows = 0;
		for(int x = 0; x < C; ++x)
			for(int y = 0; y < R; ++y) {
				bool isok = false;
				switch(cell(x,y)) {
					case empty: 
						isok = true; 
						break;//nothing to change
					case up: {
						isok = false;
						for(int ty = y - 1; ty >= 0; --ty) 
							if(empty != cell(x, ty)) {
								isok = true;
								break;
							}
						break;
					}
					case down: {
						isok = false;
						for(int ty = y + 1; ty < R; ++ty)
							if(empty != cell(x, ty)) {
								isok = true;
								break;
							}
						break;
					}
					case left: {
						isok = false;
						for(int tx = x - 1; tx >= 0; --tx)
							if(empty != cell(tx, y)) {
								isok = true;
								break;
							}
						break;
					}
					case right: {
						isok = false;
						for(int tx = x + 1; tx < C; ++tx)
							if(empty != cell(tx, y)) {
								isok = true;
								break;
							}
						break;
					}
				}
				if(!isok) { //check if arrow is fixable
					for(int ty = y - 1; ty >= 0; --ty) 
						if(empty != cell(x, ty)) {
							isok = true;
							break;
						}
					if(!isok)
					for(int ty = y + 1; ty < R ; ++ty) 
						if(empty != cell(x, ty)) {
							isok = true;
							break;
						}
					if(!isok)
					for(int tx = x - 1; tx >= 0; --tx)
						if(empty != cell(tx, y)) {
							isok = true;
							break;
						}
					if(!isok)
					for(int tx = x + 1; tx < C; ++tx)
						if(empty != cell(tx, y)) {
							isok = true;
							break;
						}

					if(isok) {//fixable
						++badarrows;
					}
					else {
						return -1;
					}
				}
			}
		return badarrows;
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
		(*out) << std::setprecision(7) << std::fixed;

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