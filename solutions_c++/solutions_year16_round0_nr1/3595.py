#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

bool mark[10];

int main(){
	ifstream myfile;
	ofstream outfile;
	myfile.open("A-large.in");
	outfile.open("output.out");
	int t;
	int o = 0;
	myfile >> t;
	while (t--){
		o++;
		fill(mark,mark + 10, false);
		long long n;
		myfile >> n;
		bool ok = false;
		if (n != 0){
			for (long long i = 1; i*n <= 1e9 && i <= 1000; i++)
			{
				long long p = i*n;
				while (p > 0){
					mark[p % 10] = true;
					p /= 10;
				}
				bool e = true;
				for (int j = 0; j < 10; j++)
					if (!mark[j])
						e = false;
				if (e){
					outfile << "Case #" << o << ": " << i*n << endl;
					ok = true;
					break;
				}
			}
		}
		if (!ok)
			outfile << "Case #" << o << ": INSOMNIA" << endl;
	}

	return 0;
}