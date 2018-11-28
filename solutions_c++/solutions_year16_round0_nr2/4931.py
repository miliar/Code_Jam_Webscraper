#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main() {
    int t, n, c, i, j, ret;
    char input[200];
    scanf("%d", &t);
    c = 1;
    while (c <= t) {
        cout<<"Case #"<<c<<": ";
        scanf("%s", input);
        ret = 0;
        for (i=0; input[i] != 0; i++) {
            if (input[i] == '-' && (input[i+1]=='+' || input[i+1]==0)) ret++;
        }
        ret *= 2;
        if (input[0]=='-') ret--;
        cout<<ret<<endl;
        c++;
    }
}
