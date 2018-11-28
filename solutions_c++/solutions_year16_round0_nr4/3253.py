#include <fstream>

using namespace std;

int main() {
	int T = 0;
	ifstream in("in.txt");
	ofstream out("out.txt");
	in >> T;
	for (int i = 0; i < T; ++i)
	{
		int K = 0;
		in >> K;
		int C = 0;
		in >> C;
		int S = 0;
		in >> S;
		out<<"Case #"<<i+1<<":";
		for (int j = 0; j < K; ++j)
		{
			out<<" "<<j+1;
		}
		out<<endl;
	}
}