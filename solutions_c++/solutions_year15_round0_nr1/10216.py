#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>

#define REP(i,p,n) for(int i=p;i<n;++i)
#define rep(i,n) REP(i,0,n)

using namespace std;

int main()
{
    int T;
    cin >> T;

    rep(t, T)
    {
        int Smax, single_digits;
        cin >> Smax >> single_digits;

        int need = 0;   // •K—v‚È—F’B
        int current = (single_digits / static_cast<int>(pow(10, static_cast<double>(Smax)))) % 10;
        if(Smax > 0)
        {
            int next_s = 1;
            for(int i=Smax-1; i>=0; --i)
            {
                int next_p = (single_digits / static_cast<int>(pow(10, static_cast<double>(i)))) % 10;
                int tmp;
                if(current < next_s)
                {
                    tmp = next_s - current;
                    need += tmp;
                    current += tmp;
                }
                current += next_p;
                next_s++;
            }
        }

        cout << "Case #" << t+1 << ": " << need << endl;
    }

	return 0;
}
