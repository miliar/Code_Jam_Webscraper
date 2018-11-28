#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int n;
	cin >> n;
	for(int cas=1; cas<=n; ++cas)
	{
		double c,f,x;
		cin >> c >> f >> x;
		double lt;
		double ls = 0;
		double dt = 2.0;
		double nt = x/2.0;
		do{
			lt = nt;
			nt = x/(dt+f) + ls + c/dt;
			ls += c/dt;
			dt += f;
			//cout << lt << "->" << nt << "@" << dt << ls << endl;
		}while(nt<lt);
		printf("Case #%d: %.7f\n",cas,lt);
	}
	return 0;
}
// 0.0 2.0 500.0  4.0  2000.0 1
// 500.0/2.0=250s 500.0 2.0 500.0 4.0 0     0.0 6.0 500.0 4.0 2000.0
// 2000/2 = 1000s
// 500/2 + 2000/6 = 585.333333
// 500/2 + 500/6 + 2000/10 = 250 + 83.333333 + 200 = 533.333333
// 500/2 + 500/6 + 500/10 + 2000/14 = 526.1904762
// 500/2 + 500/6 + 500/10 + 500/14 +2000/18 = 530.+
