#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
    int T, n;
    double d;
    cin >> T;

    for (int t=0; t<T; ++t) {
        vector<double> Naomi;
        vector<double> Ken;

        cin >> n;
        for (int i=0; i<n; ++i) {
            cin >> d;
            Naomi.push_back(d);
        }
        for (int i=0; i<n; ++i) {
            cin >> d;
            Ken.push_back(d);
        }

        int w=0, dw=0;

        sort(Naomi.begin(), Naomi.end());
        sort(Ken.begin(), Ken.end());

        /*
        for (int i=0; i<n; ++i) {
           cout << Naomi[i] << " ";
           }
           cout << endl;

           for (int i=0; i<n; ++i) {
           cout << Ken[i] << " ";
           }
           cout << endl;
           */

        vector<bool> f(Naomi.size(), true);

        int a = 0, b = n-1;

        for (int pN=n-1; pN>=0; --pN) {
            if (Ken[b] < Naomi[pN]) {
                f[a] = false;
//                cout << "Ken select " << a << ", a = " << a << endl;
                a++;
                w++;
                continue;
            }
            int select = b;
            while (select >=0 && Ken[select] > Naomi[pN]) {
                if (!f[select]) {
                    --select;
                    continue;
                }
                select--;
            }
            select++;
            while (!f[select]) ++select;
            f[select] = false;
            w += (Naomi[pN] > Ken[select]);
//            cout << "Ken select " << select << ", b = " << b << endl;
            b -= (select == b);
            while (b>=0 && !f[b]) --b;
        }

        // deceitful war
        a = 0, b = n-1;

        for (int pK=n-1; pK>=0; --pK) {
            if (Ken[pK] < Naomi[b]) dw++, --b;
            else ++a;
        }

        cout << "Case #" << t+1 << ": " << dw << " " << w << endl;

           
    }

    return 0;
}
