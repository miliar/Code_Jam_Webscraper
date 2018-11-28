# include <cstdio>
# include <cstring>
# include <iostream>

using namespace std;

int main() {
    long long int loop, x, I = 0;
    long long int count, vet[10], resposta, mult, aux, y;
    cin >> loop;

    while(loop--) {
        cin >> x;

        if(!x) {
            cout << "Case #" << ++I << ": INSOMNIA\n";
            continue;
        }

        count = 0;
        mult = 0;
        memset(vet, 0, sizeof vet);
        while(count < 10) {
            aux = (++mult)*x;
            while(aux) {
                y = aux % 10;
                aux /= 10;
                if(vet[y] == 0) {
                    count++;
                    vet[y] = 1;
                }
            }
        }

        cout << "Case #" << ++I << ": " << (mult)*x << "\n";
    }

    return 0;
}
