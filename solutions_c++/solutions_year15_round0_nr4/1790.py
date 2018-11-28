#include <bits/stdc++.h>
//#define DEBUG
using namespace std;

int main()
{
    #ifndef DEBUG

    ifstream in("qd_s2.in");
    cin.rdbuf(in.rdbuf());
    ofstream out("qd_s2.out");
    cout.rdbuf(out.rdbuf());

    #endif
    int T;
    cin>>T;
    for(int A = 1; A <= T; A++)
    {
        int X,R,C;
        cin>>X>>R>>C;
        bool p = true;
        if(R*C%X != 0)  p = false;
        if(X > 2*min(R,C) || X > max(R,C))  p = false;
        if(X == 4 && R*C == 8)  p = false;
        if(p)
            cout<<"Case #"<<A<<": "<<"GABRIEL"<<endl;
        else
            cout<<"Case #"<<A<<": "<<"RICHARD"<<endl;

    }
    return 0;
}
