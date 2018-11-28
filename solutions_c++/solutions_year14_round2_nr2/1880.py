#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main() {

	ifstream input("input.txt");
	ofstream out("out.txt");
	int t;
	input >> t;
	for (int i=0;i<t;i++) {
		unsigned int a,b,k;
		input >> a >> b >> k;
		int result=0;
		for (int x=0;x<a;x++)
			for (int y=0;y<b;y++) {
				int a = x&y;
				if (a<k) result++;
			}
		out << "Case #" << (i+1) << ": " << result << endl;
	}
	out.close();
	return 0;
}