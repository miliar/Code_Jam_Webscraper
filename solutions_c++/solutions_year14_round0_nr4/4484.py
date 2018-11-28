#include <fstream>
#include <algorithm>
#include <deque>
#include <cstring>
using namespace std;

#define in "test.in"
#define out "test.out"

ifstream f(in);
ofstream g(out);

int T, N;
deque < double > Naomi, Ken;
bool Is_Use[1009];

int main()
{
    f >> T;
    for(int t = 1; t <= T; ++t) {
        f >> N;
        Naomi.resize(N), Ken.resize(N);
        for(int i = 0; i < N; ++i)  f >> Naomi[i];
        for(int i = 0; i < N; ++i)  f >> Ken[i];

        sort(Naomi.begin(), Naomi.end());
        sort(Ken.begin(), Ken.end());

        int ans1 = 0, ans2 = 0;
        for(int i = 0; i < N; ++i)
            for(int j = 0; j < N; ++j)
                if(Naomi[i] < Ken[j] && !Is_Use[j])  {
                    Is_Use[j] = 1;
                    ++ans2;
                    break;
                }
        ans2 = N - ans2;
        while(Naomi.size()) {
            if(Naomi.back() > Ken.back())   {
                ++ans1;
                Naomi.pop_back(), Ken.pop_back();
            }
            else    {
                Ken.pop_back();
                Naomi.pop_front();
            }
        }
        g << "Case #" << t << ": " << ans1 << ' ' << ans2;
        if(t < T)   g << '\n';

        memset(Is_Use, 0, sizeof(Is_Use));
    }

}
