#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen ("D-small-attempt1.in","r",stdin);
    //freopen ("output.txt", "w",stdout);
    int t;
    cin >> t;
    for (int q=0;q<t;q++)
    {
        int x,r,c;
        cin >> x >> r >> c;
        if (x==1)
        {
            cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;
        }
        if (x==2)
        {
            if (r==1 && c==1){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==1 && c==2){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==1 && c==3){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==1 && c==4){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==2 && c==1){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==2 && c==2){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==2 && c==3){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==2 && c==4){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==3 && c==1){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==3 && c==2){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==3 && c==3){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==3 && c==4){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==4 && c==1){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==4 && c==2){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==4 && c==3){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==4 && c==4){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
        }
        if (x==3)
        {
            if (r==1 && c==1){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==1 && c==2){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==1 && c==3){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==1 && c==4){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==2 && c==1){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==2 && c==2){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==2 && c==3){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==2 && c==4){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==3 && c==1){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==3 && c==2){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==3 && c==3){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==3 && c==4){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==4 && c==1){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==4 && c==2){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==4 && c==3){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==4 && c==4){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
        }
        if (x==4)
        {
            if (r==1 && c==1){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==1 && c==2){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==1 && c==3){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==1 && c==4){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==2 && c==1){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==2 && c==2){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==2 && c==3){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==2 && c==4){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==3 && c==1){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==3 && c==2){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==3 && c==3){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==3 && c==4){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==4 && c==1){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==4 && c==2){cout << "Case #" << q+1 << ": " << "RICHARD" << endl;}
            if (r==4 && c==3){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
            if (r==4 && c==4){cout << "Case #" << q+1 << ": " << "GABRIEL" << endl;}
        }
    }
    return 0;
}
