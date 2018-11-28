#include <iostream>

using namespace std;

int main()
{
    int t,x,r,c;
    cin >> t;
    for(int i=0;i<t;i++)
    {
        cin >> x >> r >> c;
        cout << "Case #" << i + 1 << ": ";
        if (r > x-2 && c > x-2 && (r*c)%x==0 && x<7)
            cout << "GABRIEL" << endl;
        else
            cout << "RICHARD" << endl;
    }

    return 0;
}
