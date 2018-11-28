#include <fstream>

using namespace std;

ifstream cin ("inb.txt");
ofstream cout ("outb.txt");

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int x, y;
        cin >> x >> y;
        cout << "Case #" << i + 1 << ": ";
        if (x > 0)
        {
            for (int j = 0; j < x; ++j)
            {
                cout << "WE";
            }
        }
        else if (x < 0)
        {
            for (int j = 0; j < -x; ++j)
            {
                cout << "EW";
            }
        }
        if (y > 0)
        {
            for (int j = 0; j < y; ++j)
            {
                cout << "SN";
            }
        }
        else
        {
            for (int j = 0; j < -y; ++j)
            {
                cout << "NS";
            }
        }
        cout << endl;
    }
}
