#include <iostream>
#include <string>
using namespace std;

typedef long long ll;

#include <fstream>
int main()
{
    int T;
    int N;
    int J;

    //ifstream cin("in.txt");
    //ofstream cout("out.txt");

    cin >> T;
    cin >> N;
    cin >> J;

    cout << "Case #" << T<<": " << endl;
    
    int a[N+1];

    for (int i = 1; i <= N; i++) a[i] = 0;
    a[N] = a[N-3] = a[4] = a[1] = 1;
    
    int b1, b2, b3, e1, e2, e3;
    b1 = 7; b2 = 2; b3 = 3;

    if (N % 3 == 1)
    {
        e1 = N - 6;
        e2 = N - 2;
        e3 = N - 1;
    }

    if (N % 3 == 0)
    {
        e1 = N - 2;
        e2 = N - 1;
        e3 = N - 6;
    }

    if (N % 3 == 2)
    {
        e1 = N - 1;
        e2 = N - 6;
        e3 = N - 2;
    }
    
    for (int i1 = b1; i1 <= e1; i1+=3)
    for (int i2 = b2; i2 <= e2; i2+=3)
    for (int i3 = b3; i3 <= e3; i3+=3)
    {

        if (i1 < e1) a[i1] = a[i1+3] = 1;
        if (i2 < e2) a[i2] = a[i2+3] = 1;
        if (i3 < e3) a[i3] = a[i3+3] = 1;
        
        if (J > 0) {
            for (int i = N; i > 0; i-- ) cout << a[i];
            cout << " 3 7 5 6 31 8 27 5 77"<< endl;
        }   

        if (i1 < e1) a[i1] = a[i1+3] = 0;
        if (i2 < e2) a[i2] = a[i2+3] = 0;
        if (i3 < e3) a[i3] = a[i3+3] = 0;
        J--;
    }

    return 0;
}
