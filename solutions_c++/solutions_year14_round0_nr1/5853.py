#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

class Game
{
    vector<int> v;

public:
    Game()
    {
        v.assign(16, 0);
    }

    void read()
    {
        int a, b;
        cin >> a;
        for ( int i=0; i<4;++i)
        {
            for (int j=0;j<4;++j)
            {
                int t;
                cin >> t;
                if ( i == a-1)
                    v[t-1]++;
            }
        }
        cin >> b;
        for ( int i=0; i<4;++i)
        {
            for (int j=0;j<4;++j)
            {
                int t;
                cin >> t;
                if ( i == b-1)
                    v[t-1]++;
            }
        }
    }

    void print()
    {
        int count = 0, res =0;
        for ( int i=0;i<16;++i)
        {
            if ( v[i]>1) {
                count++;
                res = i;
            }

        }
        if ( count == 1)
        {
            cout << res+1 << endl;
            return;
        }
        if (count >1 ) {
            cout << "Bad magician!" << endl;
        } else{
            cout << "Volunteer cheated!" << endl;
        }
    }

};

void run_test( int t)
{
    Game G;
    G.read();
    cout << "Case #" << t+1 << ": ";
    G.print();
}

int main()
{
    freopen( "output.txt", "w", stdout);
    freopen( "A-small-attempt0.in", "r", stdin);
    int T;
    cin >> T;
    for (int t=0;t<T;++t)
    {
        run_test(t);
    }
    return 0;
}
