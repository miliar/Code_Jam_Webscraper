#include <iostream>
#include <string>
using namespace std;

//#define DEBUG(x) cout << #x << x << endl
#define DEBUG(x)

int main(int argc, char *argv[])
{
    string str;

    int T,cx;
    cin >> T;
    DEBUG(T);
    cx = 1;
    while (T--) 
    {
        int Smax;
        cout << "Case #" << cx++ << ": ";
        cin >> Smax;
        cin >> str;       
        DEBUG(str);
        register const char *s = str.c_str();
        register int p, f;
        p = 0; f = 0;
        for ( int i = 0; i <= Smax; i++ ) {
            if ( *s > '0' && (p+f) < i )
                f += (i - (p+f));
            p += (*s - '0');
            s++;
        }
        cout << f << endl;
    }

    return 0;
}
