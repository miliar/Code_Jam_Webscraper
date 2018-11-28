#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>


using namespace std;

ifstream in("small_B.in");
ofstream out("small_B.out");

int main()
{
	int test, t;
	in >> test;
	for (t = 1; t <= test; ++t)
	{
        int A, B, K;
        in >> A >> B >> K;
        vector <int> ans(K, 0);
        for (int i = 0; i < A; ++i)
            for (int j = 0; j < B; ++j)
            {
                int u = i&j;
                if (u < K)
                    ans[u]++;
            }
        int answer = 0;
        for (int i = 0; i < K; ++i)
            answer += ans[i];
        out << "Case #" << t << ": " << answer << endl;
	}

	return 0;
}