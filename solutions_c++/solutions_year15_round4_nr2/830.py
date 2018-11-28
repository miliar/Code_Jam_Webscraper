#include <fstream>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

void Solve()
{
	cout.precision(10);
	int n;
	double V,T,r0,x0,r1,x1,v0,v1,Time;
	cin >> n >> V >> T;
	if (n==1)
	{
		cin >> r0 >> x0;
		if (x0 == T) 
		{
			cout << fixed << V/r0;
		}
		else cout << "IMPOSSIBLE";
	}
	if (n==2)
	{
		cin >> r0 >> x0;
		cin >> r1 >> x1;
		
		if (x0 == x1)
		{
			if (x0 == T)
			{
				cout << fixed << V/(r0+r1);
			}
			else cout << "IMPOSSIBLE";
			return;
		}
		
		if ((x0<T && x1<T) || (x0>T && x1>T))
		{
			cout << "IMPOSSIBLE";
			return;
		}
		
		v1 = (V*(T-x0)) / (x1-x0);
		v0 = V - v1;
		
		Time = max(v0/r0,v1/r1);
		if (v0>=0.0 && v1>=0.0) cout << fixed << Time;
		else cout << "IMPOSSIBLE";
	}
	/*cout << "\n" << v0 << " " << v1 << "\n";
	cout << v0 + v1 << "\n";
	cout << (v0*x0 + v1*x1) / (v0+v1);*/
}
int main()
{
	int q,t;
	cin >> t;
	for (q=0; q<t; q++)
	{
		cout << "Case #" << q+1 << ": ";
		Solve();
		cout << "\n";
	}
	return 0;
}
