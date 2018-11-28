#include <iostream>

using namespace std;

int T;
int maxS;
int szum;
int added;

int main()
{
    cin >> T;

    for(int t=1; t<=T; t++) {
        cin >> maxS;
        szum = added = 0;
        char c;
        for(int i=0; i<=maxS; i++) {
            if(szum < i) {
                added++;
                szum++;
            }
            cin >> c;
            c -= '0';
            szum += c;
        }

        cout << "Case #" << t << ": " << added << endl;
    }

    return 0;
}
