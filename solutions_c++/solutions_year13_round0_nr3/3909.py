#include <iostream>
#include <string>
#include <stdint.h>
#include <vector>
#include <gmp.h>
#include <gmpxx.h>
#include <sstream>
#include <map>
#include <algorithm>
using namespace std;
vector<string> oikeat;
int64_t maara = 0;
int64_t laskuri = 0;
bool comp(const string & a, const string & b) {
    if (a.length() < b.length()) {
        return 1;
    }
    if (a.length() > b.length()) {
        return 0;
    }
    for (int i = 0; i < a.size(); ++i) {
        if (a[i] < b[i]) {
            return 1;
        }
        if (a[i] > b[i]) return 0;
    }
    return 0;
}
struct comp2 {
    bool operator() (const string & a, const string & b) {
    if (a.length() < b.length()) {
        return 1;
    }
    if (a.length() > b.length()) {
        return 0;
    }
    for (int i = 0; i < a.size(); ++i) {
        if (a[i] < b[i]) {
            return 1;
        }
        if (a[i] > b[i]) return 0;
    }
    return 0; 
    }
};

void lollero(string & a) {
    ++laskuri;
    //if (laskuri % 1000000 == 0) cout << laskuri << '\n';
    mpz_t luku, tulos;
    mpz_init(luku);
    mpz_init(tulos);
    mpz_set_str(luku, a.c_str(), 10);
    mpz_pow_ui(tulos, luku, 2);
    mpz_class lol(tulos);
    //cout << a << ' ' << lol << '\n';
    char * tmp = mpz_get_str(NULL, 10, tulos);
    
    string b = tmp;

    free(tmp);
    for (int i = 0; i < b.size(); ++i) {
        if (b[i] != b[b.size()-1-i]) {
            return;
        }
    }
    ++maara;
    //cout << b << '\n';
    oikeat.push_back(b);
}
int64_t alusta() {
    for (int i = 1; i < (1 << 25); ++i) {
     //   if (i % 100000 == 0) cout << i << '\n';
        if (i > 10000) break; 
        int koko = 0;
        int tmp = i;
        while (tmp > 0) {
            ++koko; 
            tmp = tmp >> 1;
        } 
       // cout << koko << '\n';
        string luku;
        for (int j = 0; j < koko; ++j) {
            luku.push_back(0);
        }
        tmp = i;
        for (int j = koko-1; j >= 0; --j) {
            luku[j] = (tmp & 1)+48;
            tmp = tmp >> 1;
        }
        //cout << luku << '\n';
        string tmp3 = luku;
        int koko2 = tmp3.size();
        for (int j = koko2-1; j >= 0; --j) {
            tmp3.push_back(tmp3[j]);
        }
        lollero(tmp3);
        tmp3 = luku;
        for (int j = koko2-2; j >= 0; --j) {
            tmp3.push_back(tmp3[j]);
        }
        lollero(tmp3);
        //continue;
        for (int j = 0; j < luku.size(); ++j) {
            int vanha = luku[j];
            luku[j] = '2';
            tmp3 = luku;
            for (int k = koko2-1; k >= 0; --k) {
                tmp3.push_back(tmp3[k]);
            }
            lollero(tmp3);
            tmp3 = luku;
            for (int k = koko2-2; k >= 0; --k) {
                tmp3.push_back(tmp3[k]);
            }
            lollero(tmp3); 
            luku[j] = vanha;
            j = luku.size()-1;
        }
        if (i == 1) {
            oikeat.push_back("9");
        }
        //liikaa kakkosia koitetaan
    }  
    return 0;
}

int main() {
    alusta();
    map<string, int64_t, comp2> maarat;
    sort(oikeat.begin(), oikeat.end(), comp);
    for (int i = 0; i < oikeat.size(); ++i) {
        maarat[oikeat[i]] = i+1;
    }
    //cout << maara << '\n';
    int t;
    cin >> t; 
    string a;
    string b;
    //for (map<string, int64_t, comp2>::iterator it = maarat.begin(); it != maarat.end(); ++it) {
     //   cout << it->first << ' ' << it->second << '\n';
    //}
    for (int i = 0; i < t; ++i) {
        a.clear();
        b.clear();
        cin >> a >> b;
        map<string, int64_t, comp2>::iterator d, e;
        d = maarat.lower_bound(a);
        e = maarat.upper_bound(b);
        int64_t c = (e->second)-(d->second);
        cout << "Case #" << i+1 << ": ";
        
        if (c > 0) {
            cout << c << '\n';
        }
        else cout << 0 << '\n';

        
     }
    
}
