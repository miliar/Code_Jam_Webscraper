#include <iostream>
#include <iomanip>
#include <fstream>

#define DBG while(0)cout

using namespace std;

int main()
{
    //ifstream fin("input.txt", ios::in);
    //ifstream fin("B-small-attempt0.in", ios::in);
    ifstream fin("B-large.in", ios::in);
    ofstream fout("output.txt", ios::out);

    int T;

    fin >> T;

    double C, F, X;
    for (int nCase = 1; nCase <= T; ++nCase)
    {
	fin >> C >> F >> X;

	double rate = 2.0;
	double ans = X / rate;
	DBG << "ans = " << X << " / " << rate << " = " << ans << endl;
	
	// f: number of farms
	int f = 0;
	double t = 0;
	double t_prev = 0;
//	for (int f = 0; f <= 10; ++f)
	while (t <= t_prev || f <= 5)
	{
	    t_prev = t;
	    t = 0;
	    for (int i = 0; i < f; ++i)
	    {
		DBG << C / (rate + (double)i * F) << " ";
		t += C / (rate + (double)i * F);
	    }
	    DBG << X / (rate + (double)f * F) << endl;
	    t += X / (rate + (double)f * F);
	    DBG << "t = " << t << endl;

	    if (t < ans)
	    {
		ans = t;
		DBG << "ans changed to " << ans << endl;
	    }
	    ++f;
	}
	DBG << endl;
	fout << "Case #" << nCase << ": " << fixed << setprecision(7) << ans << endl;
    }

    return 0;
}
