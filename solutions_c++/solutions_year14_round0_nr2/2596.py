#include <iostream>
#include <fstream>

using namespace std;

int main ()
{
	/*
	ifstream fin("t2.in");
	//fin.open("t2.in");
	ofstream fout;
	fout.open("t2.out");
	*/
	
	freopen("B-large.in","r",stdin);
	freopen("t2.out","w",stdout);

	double t,c,f,x,a,b;
	int tt,ttt;
	cin >> tt;
	for (ttt=1; ttt<=tt; ttt++)
	{
		cin >> c >> f >> x;
		a=2;
		t=0;
		while (1)
		{
			t=t+c/a;
			if (((x-c)/a)<(x/(a+f)))
			{
				t=t+(x-c)/a;
				break;
			}
			else 
			{
				a=a+f;
				//
			}
		}
		cout.setf(ios::fixed, ios::floatfield);
		cout.precision(8);
		cout << "Case #" << ttt << ": " << t << endl;
	}
}
