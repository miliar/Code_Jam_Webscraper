#include <fstream>

using namespace std;

ifstream cin ("input.txt");
ofstream cout ("output.txt");

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        string s;
        int n;
        cin >> s >> n;
        long long int Count = 0, Ans = 0, g = 0;
        for (int j = 0; j < s.size(); ++j)
        {
            while (g < s.size() && Count < n)
            {
                if (s[g] != 'a' && s[g] != 'o' && s[g] != 'i' && s[g] != 'e' && s[g] != 'u')
                {
                    ++Count;
                }
                else
                {
                    Count = 0;
                }
                ++g;
            }
            //cout << g << " " << Count << endl;
            if (Count >= n)
            {
                Ans += s.size() - g + 1;
            }
            if (s[j] != 'a' && s[j] != 'o' && s[j] != 'i' && s[j] != 'e' && s[j] != 'u')
            {
                if (Count > 0 && g - n == j)
                {
                    --Count;
                }
            }
        }
        cout << "Case #" << i + 1 << ": " << Ans << endl;
    }
}
