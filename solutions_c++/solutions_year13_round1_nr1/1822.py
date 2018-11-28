#include <fstream>
using namespace std;

int main(int argc, char const *argv[])
{
	int T, n, r, t, i, nb;
	ifstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");
	in>>T;
	n = T;
	for (i = 1; i <= n; i++)
	{
		in>>r>>t;
		nb = 0;
		while((t -= (2 * r + 1)) >= 0)
		{
			nb++;
			r += 2;
		}
		out<<"Case #"<<i<<": "<<nb<<endl; 
	}
	in.close();
	out.close();
	return 0;
}