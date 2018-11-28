#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

const string base = "1ijk";

pair<int, char> table[][4] 
{
    { {1, '1'}, {1, 'i'}, {1, 'j'}, {1, 'k'} },
    { {1, 'i'}, {-1, '1'}, {1, 'k'}, {-1, 'j'} },
    { {1, 'j'}, {-1, 'k'}, {-1, '1'}, {1, 'i'} },
    { {1, 'k'}, {1, 'j'}, {-1, 'i'}, {-1, '1'} }
};

int main()
{
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test)
    {
        int L, X;
        string S;

        cin >> L >> X >> S;
        size_t size = S.size();

        int is = 0, js = 0, ks = 0;

        for (size_t i = 0; i < size; i++)
        {
            switch (S[i]) {
            case 'i':
                is = 1;
                break;

            case 'j':
                js = 1;
                break;

            case 'k':
                ks = 1;
                break;
            }

            if (is + js + ks > 1)
                break;
        }

//printf("sum = %d\n", is + js + ks);
        if (is + js + ks < 2)
        {
            cout << "Case #" << test << ": NO" << endl;
            continue;
        }

        ostringstream os;
    
        for (int i = 0; i < X; i++)
            os << S;

        S = os.str();
        size = S.size();

//cout << "\nS = [" << S << "]" << endl;

        pair<int, char> res[] { {1, '1'}, {-1, 'i'}, {-1, 'j'}, {-1, 'k'} };
        int index = 3;
        pair<int, char> p = res[index];
        
        for (int i = size - 1; i >= 0; i--)
        {
            int signal = p.first;
            int x = base.find(p.second);
            int y = base.find(S[i]);

            p = table[y][x];
            p.first *= signal;

//printf("partial = %c%c\n", (p.first == 1 ? ' ': '-'), p.second);

            if (p == res[0] and index)
            {
                --index;
                p = res[index];
//printf("new p = %c%c\n", (p.first == 1 ? ' ': '-'), p.second);
            }
        }

//printf("final = %c%c\n", (p.first == 1 ? ' ': '-'), p.second);
        if (p == res[0])
            cout << "Case #" << test << ": YES" << endl;
            else
                cout << "Case #" << test << ": NO" << endl;
    }

    return 0;
}
