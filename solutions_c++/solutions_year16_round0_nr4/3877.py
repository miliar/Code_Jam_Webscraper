#include <iostream>

using namespace std;

int main()
{
    int T,t;
    cin >> T;
    for(t=1;t<=T;++t)
    {
        int k,c,s;
        cin >> k >> c >> s;
        cout << "Case #" << t << ":";
        for(c=1;c<=k;++c) cout << " " << c;
        cout << "\n";
    }
    return 0;
}
