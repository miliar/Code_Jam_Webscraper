#include <iostream>
#include <string>

using namespace std;

int main () {

    unsigned int t;
    cin >> t;

    for (unsigned int i = 1; i <= t; i++) {
        unsigned int max_s;

        unsigned int total = 0;     // já em pé
        unsigned int res = 0;       // resposta (amigos convidados)
        string audience;

        cin >> max_s >> audience;

        for (int j = 0; j <= max_s; j++) {
            if (total < j) {
                res += j - total;
                total = j;
            }

            total += (audience[j] - '0');
        }

        cout << "Case #" << i << ": " << res << endl;
    }

    return 0;
}
