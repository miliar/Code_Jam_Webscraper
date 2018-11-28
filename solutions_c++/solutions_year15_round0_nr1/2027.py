#include <iostream>
#include <string>
using namespace std;

#define	For(i,a,b)				for(int i=(a);i<(b);++i)
#define	rep(i,n)				For(i,0,(n))

int solve()
{
	int Smax;
	string Si;

	cin >> Smax >> Si;
	int so = 0;
	int res = 0;

	so = Si[0] - '0';
	For(i, 1, Smax + 2) {
		if(Si[i] != '0') {
			if(i > so) {
				res += i - so;
				so = i;
			}
			so += Si[i] - '0';
		}
	}
	return res;
}

int main()
{
	int T;
	cin >> T;
	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << solve() << endl;
}
