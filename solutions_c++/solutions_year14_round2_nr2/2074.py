#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream f ("B0.in");
    ofstream g ("B0.out");
    int T, A, B, K;
    f >> T;
    for (int t = 0; t < T; t++)
    {
        g << "Case #" << t+1 << ": ";
        f >> A >> B >> K;
        int answer = 0;
        for (int i = 0; i < A; i++)
        for (int j = 0; j < B; j++)
            if ((i&j) < K)
                answer++;
        g << answer << '\n';
    }
    return 0;
}
