// MagickTrick.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("input.in");
ofstream fout("output.out");
#define cin fin
#define cout fout

int main(int argc, char* argv[])
{
	int n;
	cin >> n;
	for (int i=1; i<n+1; i++)
	{
		int x, y, a[4][4], b[4][4];
		cin >> x;
		for(int j=0; j<4; j++)
			cin >> a[j][0] >> a[j][1] >> a[j][2] >> a[j][3];
		cin >> y;
		for(int j=0; j<4; j++)
			cin >> b[j][0] >> b[j][1] >> b[j][2] >> b[j][3];
		int count = 0, t;
		for(int j=0; j<4; j++)
			for(int l=0; l<4; l++)
				if(a[x-1][j]==b[y-1][l])
				{
					count++;
					t=a[x-1][j];
				}
		if(count==1)
			cout << "Case #" << i << ": " << t << endl;
		else if(count>1)
			cout << "Case #" << i << ": Bad magician!" << endl;
		else
			cout << "Case #" << i << ": Volunteer cheated!" << endl;

	}
	return 0;
}

