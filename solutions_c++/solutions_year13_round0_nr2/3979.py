#include <iostream>
#include <fstream>
using namespace std;


class Lawn {
    private:
	int lawn[100][100];
	const int N, M;
    public:
	Lawn(int r, int c) :  N(r), M(c) { for (int i = 0; i < r; ++i) for(int j = 0; j < c; ++j) lawn[i][j] = 100; }
	void read(fstream&);
	bool check(void);
	bool check(int, int);
};

void Lawn::read(fstream& f)
{
    for(int i =0; i < N; ++i) {
	for(int j = 0; j < M; ++j) {
    	    int c;
	    f >> c;
	    lawn[i][j] = c;
	}
    }
    return;
}

bool Lawn::check(void)
{
    for(int i =0; i < N; ++i) {
	for(int j = 0; j < M; ++j) {
	    if (!check(i, j)) return false;
	}
    }
    return true;
}

bool Lawn::check(int x, int y)
{
    int val = lawn[x][y]; 
    bool rowOk = true, colOk = true;
    bool right = true, left = true;
    for(int j = 0; j < M; ++j) {
	if (lawn[x][j] > val) {
	    rowOk = false;
	}
    }
    for(int i = 0; i < N; ++i) {
	if (lawn[i][y] > val) {
	    colOk = false;
	}
    }
    return rowOk || colOk;
}

int main() 
{

    fstream f("in", fstream::in);
    int T;
    f >> T;
    for (int i = 1; i <= T; ++i) {
	int N, M;
	f >> N >> M;
    	Lawn g(N, M);
    	g.read(f);
	string ans = g.check() ? "YES" : "NO";
    	cout << "Case #" << i << ": " << ans << endl; 
    }
    return 0;

}
