#include <cstdio>
#include <cassert>
#include <vector>
#include <string>
using namespace std;

#define I 'i'
#define J 'j'
#define K 'k'

int T;
char buf[10001];
char imos[100000001];
vector<vector<char> > vec;

char calc(char a, char b) {
    bool neg = false;

    if (a < 0) {
        a = -a;
        neg = !neg;
    }

    if (b < 0) {
        b = -b;
        neg = !neg;
    }

    return vec[a][b] * (neg ? -1: 1);
}

char rev(char mul, char a) {
    char ret = 0;

    if (a < 0) {
        a = -a;
        mul = -mul;
    }

    if (vec[a][1] == mul) ret = 1;
    if (vec[a][I] == mul) {
        assert(!ret);
        ret = I;
    }
    if (vec[a][J] == mul) {
        assert(!ret);
        ret = J;
    }
    if (vec[a][K] == mul) {
        assert(!ret);
        ret = K;
    }

    return ret;
}

int main() {
    scanf("%d", &T);

    vec.resize(256);
    for (int i=0; i<256; i++) {
        vec[i].resize(256);
    }

    vec[1][1] = 1; 
    vec[1][I] = I; 
    vec[1][J] = J; 
    vec[1][K] = K; 
    vec[I][1] = I; 
    vec[I][I] = -1; 
    vec[I][J] = K; 
    vec[I][K] = -J; 
    vec[J][1] = J; 
    vec[J][I] = -K; 
    vec[J][J] = -1; 
    vec[J][K] = I; 
    vec[K][1] = K; 
    vec[K][I] = J; 
    vec[K][J] = -I; 
    vec[K][K] = -1; 

    for (int t=0; t<T; t++) {
        int l, x;
        char result;
        bool possible = false;
        string s;

        scanf("%d %d", &l, &x);
        scanf("%s", buf);
        for (int i=0; i<x; i++) {
            s += buf;
        }

        result = s[0];
        imos[0] = result;
        for (int i=1; i<s.length(); i++) {
            result = calc(result, s[i]);
            imos[i] = result;
        }

        for (int i=0; i<s.length(); i++) {
            if (imos[i] != I) continue;

            for (int j=i+1; j<s.length()-1; j++) {
                if (rev(imos[j], imos[i]) == J && rev(imos[s.length()-1], imos[j]) == K) {
                    possible = 1;
                    break;
                }
            }

            if (possible) break;
        }

        if (possible) {
            printf("Case #%d: YES\n", t+1);
        } else {
            printf("Case #%d: NO\n", t+1);
        }
    }
}
    
