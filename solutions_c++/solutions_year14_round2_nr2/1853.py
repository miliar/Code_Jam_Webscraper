#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	
	for (int t = 0; t < T; t++) {
		long long count(0);	
		int a, b, k;
		in >> a >> b >> k;
		for (int i=0; i < a; i++) {
			for (int j=0; j < b; j++) {
				if ((i & j) < k)
					count++;
			}
		}
		out << "Case #" << t+1 << ": "; 
		out << count << endl;
	}
	
}//main