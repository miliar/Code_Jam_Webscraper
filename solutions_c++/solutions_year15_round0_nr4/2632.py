#include <iostream>

using namespace std;

int main()
{
    int i,T,X,R,C;

    cin >> T;
    for(i=1;i<=T;i++)
    {
        cin >> X >> R >> C;
        if (R > X-2 && C > X-2 && (R*C)%X==0) cout << "Case #" << i << ": GABRIEL" << endl;
        else cout << "Case #" << i <<": RICHARD" << endl;
    }

    return 0;
}
