#include <iostream>
#include <iomanip>
#include <cstdio>

using namespace std;

class Game
{
    double C,F,X;

public:
    void read() {
        cin >> C >> F >> X;
    }

    double count() {
        double res = X/2;
        double T=0;
        double cur = 2.0;

        for ( int i=1;1;++i) {
            T += C/cur;
            cur += F;
            if ( T > res )
                break;
            double new_res = T+X/cur;
            if ( new_res < res)
                res = new_res;
        }
        return res;
    }
};

void run_test( int t)
{
    Game G;
    G.read();
    cout << "Case #" << t+1 << ": " << fixed << setprecision(7) << G.count() << endl;
}

int main()
{
    freopen( "output.txt", "w", stdout);
    freopen( "input.txt", "r", stdin);
    int T;
    cin >> T;
    for (int t=0;t<T;++t)
    {
        run_test(t);
    }

    return 0;
}
