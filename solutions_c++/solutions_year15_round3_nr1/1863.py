#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

//#define DEBUG

#ifdef DEBUG
ifstream fin("A.in");
ofstream fout("A.out");
#else
ifstream fin("A1-small.in.txt");
ofstream fout("A1-small.out.txt");
#endif

void solve()
{
    int R, C, W;
    fin >> R >> C >> W;
    int ans = 0;
    if(C == W) {
	ans = W;
    }
    else {
	while(C > 2*W) {
	    C -= W;
	    ans++;
	}
	ans += W + 1;
    }
    fout << ans << endl;
}

int main()
{
    int T; fin >> T;
    for(int c = 1; c <= T; c++)
    {
	fout << "Case #" << c << ": ";
	solve();
    }

    return 0;
}
