#include <iostream>
#include <cstring>

using namespace std;

int T, tcase;
string S;
char ch;
int p, cnt;

int main()
{
    cin >> T;
    tcase = 1;
    while (tcase<=T) {
        S = "";
        cin >> S;

        p = 0;
        ch = S[p];
        cnt = 0;
        while ( (++p)<S.size() ) {
            if (ch!=S[p]) {
                cnt++;
                ch = S[p];
            }
        }

        if (S[p-1]=='-') {
            cnt++;
        }

        cout << "Case #" << tcase++ << ": " << cnt << endl; 
    }
}
