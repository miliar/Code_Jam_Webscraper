#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int T;
double C, F, X;

int main()
{
    fstream fin("B-large.in",ifstream::in);
    fstream fout("B-large.out",ofstream::out);
    fin >> T;
	fout.setf( std::ios::fixed, std:: ios::floatfield );
	fout.precision(7);
	//FILE *fout = fopen("B.out", "w");
	for(int tc=1;tc<=T;tc++)
    {
        fin >> C >> F >> X;
		//int N = 0;
		double Tprev = X / 2.;
		double Tnext = 0.;
		double Ttmp = 0.;
		for(int N=1;;++N) {
			Ttmp += C / (2. + (N-1.)*F);
			Tnext = Ttmp + X / (2. + N*F);
			if (Tnext>Tprev) {
				fout << "Case #" << tc << ": " << Tprev << "\n";
				cout << "Case #" << tc << ": " << Tprev << "\n";
				//fprintf(fout, "Case #%d: %.7lf\n", tc, Tprev);
				break;
			}
			Tprev = Tnext;
		}
    }
    fin.close();
    fout.close();
	//fclose(fout);
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
