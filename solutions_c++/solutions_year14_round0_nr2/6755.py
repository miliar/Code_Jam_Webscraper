#include <fstream>
#include <iomanip>

using namespace std;

ifstream in("large.in");
ofstream out("large.out");

int main()
{
	int test, t;
	in >> test;
	for (t = 1; t <= test; ++t)
	{
        double C, F, X;
        in >> C >> F >> X;
        double next = X / 2.0, ans;
        int k = 0;
        do
        {
            k++;
            ans = next;
            next = ans - (X - C) / (2.0 + (k - 1) * F) + X / (2 + k * F);
        } while (ans > next);
        out << "Case #" << t << ": " << fixed << setprecision(7) << ans << endl;
	}

	return 0;
}