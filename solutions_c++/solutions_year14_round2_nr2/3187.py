#include <iostream>


int pair(int A, int B, int K)
{
	int c = 0;
	for (unsigned int i = 0; i < A; ++i)
		for (unsigned int j = 0; j < B; ++j)
			if ((i & j) < K)
                ++c;
	return c;
}

int main(int argc, const char * argv[])
{
	int T = 0;
	std::cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int A = 0, B = 0, K = 0;
		std::cin >> A >> B >> K;
        
		std::cout << "Case #" << i + 1 << ": " << pair(A, B, K) << std::endl;
	}
    return 0;
}
