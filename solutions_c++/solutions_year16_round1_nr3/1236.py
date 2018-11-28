#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n;
int to[1008];

int maxkor[1008];
int maxlanc[1008];

void bejar(int kezd, int akt, int len) {

    //cout << "Bejaras " << kezd << " " << akt << " " << len << endl;
    if (len > maxlanc[kezd])
        maxlanc[kezd] = len;
    if (len>20)
        return;
    for (int i=1; i<=n; i++) {
        if (to[i] == akt && i!=to[kezd]) {
            bejar(kezd, i, len+1);
        }
    }

}

int main() {

    int test;
    cin >> test;

    for (int testnum=0; testnum<test; testnum++) {

        cin >> n;
        int osszlanc = 0;
        for (int i=1; i<=n; i++)
            cin >> to[i];

        for (int i=0; i<1006; i++) {
            maxkor[i] = 0;
            maxlanc[i] = 0;
        }


        for (int i=1; i<=n; i++) {
            /// Bejárás i-bõl
            int id[1008] = {0};
            int x = i;
            int db=1;
            //cout << "Bejaras " << i << endl;
            while (id[x] == 0) {

                id[x] = db;

                //cout << " (" << id[x] << ") " << x << endl;
                db++;
                x = to[x];

            }
            //cout << endl;
            if (x == i)// || id[x] == db - 2)
                maxkor[i] = db - id[x];
            else maxkor[i] = 0;
            //cout << i << " " <<maxkor[i] << endl;

        }

        int lnkor = *max_element(&maxkor[0], &maxkor[n]);


        for (int i=1; i<=n; i++) {
            /// Max lanc i-bol

            if (maxkor[i] == 2)
                bejar(i, i, 0);

            //cout << " maxlanc " << i << " " << maxlanc[i] << endl;
        }
        for (int i=1; i<=n; i++) {
            if (maxkor[i] == 2) {
                osszlanc += maxlanc[i];
                osszlanc += 1;
            }
        }

        cout << "Case #" << testnum+1 << ": ";
        cout << max(lnkor, osszlanc);
        cout << endl;

        //cout << endl << endl << endl;
    }
}
