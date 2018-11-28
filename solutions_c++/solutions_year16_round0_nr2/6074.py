# include <string>
# include <iostream>

using namespace std;

int main() {
    int testes, len, feliz, count, I = 0;
    string pilha;
    cin >> testes;

    while(testes--) {
        cin >> pilha;
        len = pilha.size();

        feliz = 1;
        count = 0;
        for (int i = len - 1; i >= 0; --i) {
            if(pilha[i] == '-' && feliz == 1) {
                feliz = 0;
                ++count;
            } else if (pilha[i] == '+' && feliz == 0) {
                ++count;
                feliz = 1;
            }
        }

        cout << "Case #" << ++I << ": " << count << endl;
    }
    return 0;
}
