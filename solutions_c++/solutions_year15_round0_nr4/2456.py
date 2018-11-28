#include<iostream>
#include<iomanip> 
#include<fstream>
using namespace std;
int main()
{
	char filename[] = "d.out";
	ofstream fout(filename);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		int X, R, C;
		cin >> X >> R >> C;
		if (X >= 7) {
			fout<<"Case #" << i << ": RICHARD" <<endl;
		}
		if (X <= 6) {
			if ((R >= (X-1)) && (C >= (X-1)) && ((R*C)%X == 0)) 
				fout<<"Case #" << i << ": GABRIEL" <<endl;
			else
				fout<<"Case #" << i << ": RICHARD" <<endl; 
		}
	}
	return 0;
}
