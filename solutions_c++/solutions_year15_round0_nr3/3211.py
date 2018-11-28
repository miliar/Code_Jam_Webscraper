#include <iostream>
#include <string>

using namespace std;

string mul_table[4][4] = {{"1", "i", "j", "k"}, {"i", "-1", "k", "-j"}, {"j", "-k", "-1", "i"}, {"k", "j", "-i", "-1"}};

string mul(string a, string b) {
    int num_a, num_b;
    int znak_a = 1, znak_b = 1;

    if(a[0] == '-') {
        znak_a = -1;
        a.erase(0, 1);
    }

    if(b[0] == '-') {
        znak_b = -1;
        b.erase(0, 1);
    }

    if(a == "1")
        num_a = 0;
    else if(a == "i")
        num_a = 1;
    else if(a == "j")
        num_a = 2;
    else
        num_a = 3;

    if(b == "1")
        num_b = 0;
    else if(b == "i")
        num_b = 1;
    else if(b == "j")
        num_b = 2;
    else
        num_b = 3;

    string wynik;
    if(znak_a * znak_b < 0)
        wynik += "-";
    wynik += mul_table[num_a][num_b];

    if(wynik[0] == '-' && wynik[1] == '-')
        wynik.erase(0, 2);

    return wynik;
}

int main() {
    int t, l, x;
    string tmp, text;
    cin >> t;
    for(int i = 0 ; i < t ; i++) {
        cin >> l >> x;
        cin >> tmp;
        text = "";
        for(int i = 0 ; i < x ; i++)
            text += tmp;

        string iloczyn;
        iloczyn += text[0];
        int a = 0;
        while(iloczyn != "i" && a < l * x) {
            string tmp;
            a++;
            tmp += text[a];
            iloczyn = mul(iloczyn, tmp);
        }

        if(a == l * x) {
            cout << "Case #" << i + 1 << ": NO" << endl;
            continue;
        }

        int b = a + 1;
        iloczyn = "";
        iloczyn += text[b];
        while(iloczyn != "j" && b < l * x) {
            string tmp;
            b++;
            tmp += text[b];
            iloczyn = mul(iloczyn, tmp);
        }

        if(b == l * x) {
            cout << "Case #" << i + 1 << ": NO" << endl;
            continue;
        }

        iloczyn = "";
        iloczyn += text[b + 1];
        for(int y = b + 2 ; y < l * x ; y++) {
            string tmp;
            tmp += text[y];
            iloczyn = mul(iloczyn, tmp);
        }

        if(iloczyn == "k")
            cout << "Case #" << i + 1 << ": YES" << endl;
        else
            cout << "Case #" << i + 1 << ": NO" << endl;
    }

    return 0;
}
