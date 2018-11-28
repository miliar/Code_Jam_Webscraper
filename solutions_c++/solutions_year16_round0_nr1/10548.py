#include<iostream>
#include<string>
#include<set>
#include<cstdio>
using namespace std;

int N;
unsigned long long n, nn;

string solve() {
    if (n==0) return string("INSOMNIA");

    set<char> c_set;
    string nn_str;
    int i = 1;
    while ( c_set.size() < 10 ) {
        nn = n * (i++);
        nn_str = std::to_string(nn);
        for (int j = 0;j < nn_str.length();j++) {
            c_set.insert(nn_str[j]);
        }
    }

    return nn_str;
}

int main() {
    scanf("%d", &N);

    for ( int i = 1;i <= N;i++) {
        scanf("%llu", &n);
        string result = solve();
        printf("Case #%d: %s\n", i, result.c_str());
    }

    return 0;
}
