# include <bits/stdc++.h>

using namespace std;

int c, tpal;
int loop, vet[3000];
string pal;
vector<int>resp;

void tira(string num, int n) {
    resp.push_back(n);
    int tnum = num.size();
    c -= tnum;
    for(int j = 0; j < tnum; ++j) {
        for (int i = 0; i < tpal; ++i) {
            if (num[j] == pal[i] && !vet[i]) {
                vet[i] = 1;
                break;
            }
        }
    }
}

int main() {
    int I = 0;
    cin >> loop;

    while(loop--) {
        resp.clear();
        memset(vet, 0, sizeof(vet));
        cin >> pal;
        tpal = pal.size();
        c = pal.size();

        for (int i = 0; i < pal.size() && c; ++i) {
            if (!vet[i] && pal[i] == 'Z') tira("ZERO", 0);
            if (!vet[i] && pal[i] == 'W') tira("TWO", 2);
            if (!vet[i] && pal[i] == 'X') tira("SIX", 6);
            if (!vet[i] && pal[i] == 'G') tira("EIGHT", 8);
        }

        if (c) {
            for (int i = 0; i < pal.size() && c; ++i) {
                if (!vet[i] && pal[i] == 'H') tira("THREE", 3);
                if (!vet[i] && pal[i] == 'U') tira("FOUR", 4);
                if (!vet[i] && pal[i] == 'S') tira("SEVEN", 7);
            }
        }

        if (c) {
            for (int i = 0; i < pal.size() && c; ++i) {
                if (!vet[i] && pal[i] == 'F') tira("FIVE", 5);
                if (!vet[i] && pal[i] == 'O') tira("ONE", 1);
            }
        }

        while(c) {
            resp.push_back(9);
            c -= 4;
        }

        sort(resp.begin(), resp.end());
        cout << "Case #" << ++I << ": ";
        for (int i = 0; i< resp.size(); ++i) {
            cout << resp[i];
        }
        cout << endl;
    }
    return 0;
}
