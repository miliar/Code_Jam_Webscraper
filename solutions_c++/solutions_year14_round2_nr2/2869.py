#include <iostream>
#include <fstream>

using namespace std;
int A, B, K;

int main(int argc, char **argv)
{
	fstream in, out;
	in.open("B-small-attempt0.in", ios::in);
	out.open("output.txt", ios::out);
	int TC;
	int sol = 0;
	
	in >> TC;
	for(int tc=1; tc<=TC; tc++) {
		// GET DATAS
		in >> A >> B >> K;
		// SOLVE
		for(int a=0; a<A; a++) {
			for(int b=0; b<B; b++) {
				if((a & b) < K) {
					sol++;
				}
			}
		}
		out << "Case #" << tc << ": " << sol << endl;
		sol = 0;
	}
	
	fcloseall();
	return 0;
}
