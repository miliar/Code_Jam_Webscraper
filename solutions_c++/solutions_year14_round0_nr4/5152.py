#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;


int main()
{
	int t, n, cw = 0, w = 0, ultim = 0, counter = 0, counter2 = 0;
	double v1[1001],v2[1001];
	bool gasit = false, cheat = false;;
	ifstream in("D-large.in");
	ofstream out("Output.out");
	in >> t;
	int cases = 1;
	while (cases <= t){
		in >> n;
		for (int i = 0; i < n; i++){
			in>>v1[i];
			
		}
		for (int i = 0; i < n; i++){
			in >> v2[i];
		}
		sort(v1, v1 + n);
		sort(v2, v2 + n);
		cheat = false;
		ultim = 0;
		counter = 0;
		counter2 = 0;
		int j = 0;
		if (n>1){
			for (int i = 0; i<n; i++){
				if (v1[i]>v2[j]){
					counter++;
					j++;
				}
			}
			cw = counter;
			for (int i = 0; i < n; i++){
				gasit = false;
				for (int j = ultim; j < n; j++){
					if (v1[i] < v2[j]){
						gasit = true;
						v2[j] = 0;
						ultim = j;
						counter2++;
						break;
					}
				}
				if (!gasit){
					break;
				}
			}
			w = n - counter2;

		}
		else{
			if (v1[0] > v2[0]){
				w = cw = 1;
			}
			else{
				w = cw = 0;
			}
		}
		out << "Case #" << cases << ": " <<cw<<" "<<w<< endl;
		cases++;
	}
	return 0;
}