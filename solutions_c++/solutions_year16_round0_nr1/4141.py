#include <fstream>
using namespace std;

inline bool done(bool seen[]) {
    for (int i = 0; i < 10; i++)
        if (!seen[i])
            return false;
    return true;
}

void digits(int N, bool seen[]) {
    while (N >= 10) {
        seen[N % 10] = true;
        N /= 10;
    }
    seen[N] = true;
}

int main()
{
    int T, N;
    ifstream in("input.txt");
    ofstream out("output.txt");
    in >> T;
    for (int i = 0; i < T; i++)
    {
        bool seen[10];
        for (int k = 0; k < 10; k++)
            seen[k] = false;
        in >> N;
        if (N == 0)
                out << "Case #" << i + 1 << ": INSOMNIA" << endl;
        else {
            int cur = N;
            do {
                digits(cur, seen);
                cur += N;
            } while (!done(seen));
            out << "Case #" << i + 1 << ": " << cur - N << endl;
        }
    }
}
