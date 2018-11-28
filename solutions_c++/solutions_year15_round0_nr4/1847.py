#include<iostream>
#include<algorithm>
using namespace std;

int T, X, R, C, noc=1;

main()
{
    ios_base::sync_with_stdio(0);
    cin >> T;
    while(T--)
    {
        bool richard=true; // Richard choose
        cin >> X >> R >> C;
        if(R>C) swap(R, C);

        if(X==1) richard=false;
        if(X==2 && (R*C)%2==0) richard=false;
        if(X==3)
        {
            if(R==2 && C==3) richard=false;
            if(R==3 && C>=3) richard=false;
        }
        if(X==4)
        {
            if(R>=3 && C==4) richard=false;
        }

        cout << "Case #" << noc++ << ": ";
        if(richard) cout << "RICHARD" << endl;
        else cout << "GABRIEL" << endl;
    }
    return 0;
}
