#include<iostream>
using namespace std;

int main()
{
    int T, t;
    cin >> T;
    int C, c;
    char tmp;
    int s, e;
    for (t = 0; t < T; ++t)
    {
        cin >> C;
        //cout << " C = " << C << endl;

        cin.get();
        cin.get(tmp);
        s = (int)tmp - 48;
        //cout << s <<endl;
        e = 0;
        for (c = 1; c <= C; ++c)
        {
            cin.get(tmp);
            if (s < c)
            {
                e += c - s;
                s += (int)tmp + c - s - 48;
            }
            else
            {
                s += (int)tmp - 48;
            }
            //cout << "tmp = " << (int)tmp-48 << " s = " << s << " c = " << c << " ext = " << e << endl;
        }
        cin.get();
        cout << "Case #" << t+1 << ": " << e << endl;
    }
    return 0;
}
