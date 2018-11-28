#include <iostream> 
#include <fstream> 
#include <string>
using namespace std;

// Problem A. Standing Ovation

int main(int argc, char* argv[])
{
	ifstream in("A-small-attempt1.in");
	ofstream out("A-output1.txt");
	int T;
	in >> T;
	for (int i = 1; i <= T; ++i)
	{
		int n;
		string auds;
		in >> n >> auds;
		int req = 0;
		int sum = 0;
		for (int k = 0; k <= n; ++k)
		{
			int m = auds[k] - '0';
			if (m == 0) continue;

			if (sum + req < k)
				req += (k - sum);
			sum += m;
		}
		out << "Case #" << i << ": " << req << endl;
	}

	return 0;
}
