#include <iostream>
#include <fstream>
using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

bool ans[1005 * 1000];

bool ispal(int xx) {
    int rev = 0, x = xx;
    while(xx) {
        rev = rev * 10 + xx % 10;
        xx /= 10;
    }
    return x == rev;
}

void gen() {
    for(int i = 1; i <= 1000; i++)
        if (ispal(i) && ispal(i * i))
            ans[i*i] = true;
}

int main() {
    gen();
    int tt, a, b, cnt;
    in>>tt;
    for(int t = 0; t < tt; t++) {
        in>>a>>b;
        cnt = 0;
        for(int i = a; i <= b; i++)
            cnt += ans[i];
        out<<"Case #"<<t+1<<": "<<cnt<<"\n";
    }
    return 0;
}
