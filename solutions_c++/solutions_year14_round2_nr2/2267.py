#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	std::ifstream in("B-small-attempt0.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
	
	std::ofstream out("out.txt");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!


	int T;
	cin >> T;

	for (int n = 0; n < T; ++n)
	{
		int A, B, K;
		cin >> A >> B >> K;

		int count = 0;
		for (int i = 0; i < A; ++i)
			for (int j = 0; j < B; ++j)
				if ((i & j) < K)
					++count;
		cout << "Case #" << n << ": " << count << endl;
	}

	system("pause");
}