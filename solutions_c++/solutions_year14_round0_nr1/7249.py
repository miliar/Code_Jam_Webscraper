#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <cstddef>
#include <vector>

using namespace std;

int main (){
	ifstream in ("input.in");
	ofstream out ("output.out");
	int t;
	in >> t;
	for (int i=0; i<t; i++)
	{
		int n, k, com = 0;
		vector <int> s, f;
		s.resize (4);
		f.resize (4);
		in >> n;
		for (int q=0; q< 4*(n-1); q++) in >> k;
		for (int j=0; j<4; j++) in >> s[j];
		for (int q=4*n; q<16; q++)in >> k;
		in >> n;
		for (int q=0; q< 4*(n-1); q++) in >> k;
		for (int j=0; j<4; j++) in >> f[j];
		for (int q=4*n; q<16; q++) in >> k;
		for (int j=0; j<4; j++){
			for (int q=0; q<4; q++){
				if (s[j]==f[q])
					if (com==0) com = s[j];
					else if (com != 0) com = -1;
			}
		}
		if (com > 0) out << "Case #" << i+1 << ": " << com << '\n';
		else if (com == 0) out << "Case #" << i+1 << ": Volunteer cheated!" << '\n';
		else out << "Case #" << i+1 << ": Bad magician!" << '\n';
	}

	in.close();
	out.close();
	return 0;
}