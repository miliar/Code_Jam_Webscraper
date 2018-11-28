#include<iostream>
#include<fstream>

using namespace std;

int f(int x, int r, int c)
{
	if (x >= 7)
		return 1;
	if ((r*c) % x != 0)
		return 1;
	if (x == 1 || x == 2)
		return 2;

	if (r < c)
		swap(r, c);
	if (r + c < x + 1)
		return 1;
	if (r < x )
		return 1;
	if (c < (x + 1) / 2)
		return 1;
	if (x == 4 && c == 2)
		return 1;

	if (x == 6 && c == 3)
		return 1;
	return 2;
}
int main()
{
	int t, x,r,c;
	ofstream fout;
	fout.open("d:\\ans.txt");
	cout.rdbuf(fout.rdbuf());

	ifstream fin;
	fin.open("d:\\1.in");
	cin.rdbuf(fin.rdbuf());

	cin >> t;
	for (int test = 1; test <= t; test++)
	{
		cin >> x>>r>>c;
		
		cout << "Case #" << test << ": " << (f(x,r,c)==1?"RICHARD":"GABRIEL") << endl;
	}

	return 0;
}