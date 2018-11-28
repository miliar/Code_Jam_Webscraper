#include <fstream>

using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        long long int r, t;
        cin >> r >> t;
        int Count = 0;
        while ((r + 1) * (r + 1) - r * r <= t)
        {
            ++Count;
            t -= (r + 1) * (r + 1) - r * r;
            r += 2;
        }
        cout << "Case #" << i + 1 << ": " << Count << endl;
    }
}
