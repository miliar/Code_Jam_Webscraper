#include <iostream>

using namespace std;

int main() {
    int T, i, j, k;
    double c, f, x, r=2.0, tm, t1, t2;

    cin>>T;

    for (int i=1; i<=T; ++i) {

        cin >> c >> f >> x;

        t2 = 0;
        t1 = 0;
        r = 2;
        tm = x/r;
        while (true) {
            t2 = t1 + c/r + (x)/ (r + f);
            //cout<<"t2 = "<<t2<<"\n";
        
            if (t2 >= tm) {
                break;
            }

            tm = t2;

            t1 = t1 + c/r;
            r += f;
            //cout<<"t1 = "<<t1<<" r="<<r<<"\n";
        }

        printf("Case #%d: %.7f\n", i, tm);
    }

    return 0;
}

