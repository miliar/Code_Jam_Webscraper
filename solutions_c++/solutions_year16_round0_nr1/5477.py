#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int d[10], z;

void vezi(unsigned long long n){
	while (n > 0){
		int c = n % 10;
		if (d[c] == 0){
			d[c] = 1;
			z--;
		}
		n /= 10;
	}
}

int main(){
	ifstream f("date.in");
	ofstream g("date.out");

	int T;
	f >> T;

	for (int t = 1; t <= T; ++t){
		unsigned long long n;
		f >> n;
		if (n){
			z = 10;
			int j = 0;
			for (int i = 0; i < 10; ++i)
				d[i] = 0;
			while (z > 0){
				j++;
				vezi(n*j);
			}
			g << "Case #" << t << ": " << n * j << "\n";
		}
		else
			g << "Case #" << t << ": INSOMNIA\n";
	}

	f.close();
	g.close();

	return 0;
}
