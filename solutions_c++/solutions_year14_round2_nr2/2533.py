#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;


int main()
{
	int a, b, k, t, cw;
	ifstream in("B-small-attempt0.in");
	ofstream out("Output.out");
	in >> t;
	int cases = 1;
	while (cases <= t){
		in >> a >> b >> k;
		cw = 0;
		for (int l = 0; l < k; l++){
			for (int i = 0; i < a; i++){
				for (int j = 0; j < b; j++){
					if ((i&j) == l)
						cw++;
				}
			}
		}
		out << "Case #" << cases << ": " << cw << endl;
		cases++;
	}
	return 0;
}