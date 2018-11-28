#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

string words[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int letter[256] = {0};
int res[16] = {0};

void output() {
    for (int i = 0; i <= 9; i++) {
        if (res[i] > 0) {
            for (int j = 0; j < res[i]; j++) {
                cout << i;
            }
        }
    }
    cout << endl;
}

void search(int d, int size) {
    if (size == 0) {
        output();
        return;
    }

    if (d < 0) {
        return;
    }

    map<char, int> minus;
    for (int i = 0; i < words[d].size(); i++) {
        if (minus.find(words[d][i]) == minus.end()) {
            minus[words[d][i]] = 1;
        } else {
            minus[words[d][i]]++;
        }
    }

    search(d - 1, size);
    
    int num = 0;
    while (true) {
        num++;
        bool cont = true;
        for (auto i = minus.begin(); i != minus.end(); i++) {
            char c = i->first;
            int x = i->second;
            if (letter[c] < x * num) {
                cont = false;
                break;
            }
        }

        if (cont) {
            for (auto i = minus.begin(); i != minus.end(); i++) {
                letter[i->first] -= i->second * num;
                size -= i->second * num;
            }
            res[d] += num;
            search(d - 1, size);
            res[d] -= num;
            for (auto i = minus.begin(); i != minus.end(); i++) {
                letter[i->first] += i->second * num;
                size += i->second * num;
            }
        } else {
            break;
        }
    }
}

int main(int argc, char *argv[])
{
    int T = 0;
    cin >> T;

    for (int cas = 1; cas <= T; cas++) {
        string N;
        cin >> N;

        memset(letter, 0, sizeof(letter));
        for (int i = 0; i < N.size(); i++) {
            letter[N[i]]++;
        }
        
        cout << "Case #" << cas << ": ";
        memset(res, 0, sizeof(res));
        search(9, N.size());
    }
    
    return 0;
}
