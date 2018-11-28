#include <fstream>
#include <algorithm>
using namespace std;

int M, R, C;

char* m;
inline char& map(int r, int c){
	return *(m + r*C + c);
}

bool fillblock(int cr, int lc, int S, bool first = false){
	for (int i = lc; i >= 2; i--){
		if (S%i == 0)

			if (cr + S / i <= R){
				if (first && S / i == 1)
					continue;
				for (int r = cr; r < cr + S / i; r++)
					for (int c = 0; c < C; c++)
						map(r, c) = (c < i) ? '.' : '*';
				for (int r = cr + S / i; r < R; r++)
					for (int c = 0; c < C; c++)
						map(r, c) = '*';
				return true;
			}
		else
			break;
		
	}
	for (int i = lc; i >= 2; i--){
		for (int ncr = R; ncr > cr + first?1:0; ncr--)
			if (i*(ncr - cr) < S){
				for (int r = cr; r < ncr; r++)
					for (int c = 0; c < C; c++)
						map(r, c) = (c < i) ? '.' : '*';
				if (fillblock(ncr, i - 1, S - i*(ncr - cr)))
					return true;
			}
	}
	return false;
}

int main(int argc, char** argv){
	if (argc != 3)
		return -1;

	ifstream ifs;
	ifs.open(argv[1]);
	ofstream ofs;
	ofs.open(argv[2]);

	int T;
	ifs >> T;
	for (int i = 0; i < T; i++){
		ifs >> R >> C >> M;
		int S = R*C - M;
		bool swaped = false;

		ofs << "Case #" << (i + 1) << ":" << endl;
		m = new char[R*C];


		if (R == 1 || C == 1){
			for (int i = 0; i < R*C; i++)
				m[i] = (i < S) ? '.' : '*';
		}
		else if (S == 1)
			for (int r = 0; r < R; r++){
				for (int c = 0; c < C; c++)
					map(r, c) = '*';
			}
		else{

			if (!fillblock(0, C, S,true)){
				swap(R, C);
				swaped = true;
				if (!fillblock(0, C, S,true)){
					ofs << "Impossible" << endl;
					goto NextCase;
				}
			}

		}

		m[0] = 'c';

		if (!swaped){
			for (int r = 0; r < R; r++){
				for (int c = 0; c < C; c++)
					ofs << map(r, c);
				ofs << endl;
			}
		}
		else{
			for (int c = 0; c < C; c++){
				for (int r = 0; r < R; r++)
					ofs << map(r, c);
				ofs << endl;
			}
		}


	NextCase:
		delete[] m;
	}

	ifs.close();
	ofs.close();
}
