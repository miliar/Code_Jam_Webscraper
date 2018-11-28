#include <cstdio>
#include <cstring>
#include <fstream>
#include <stdint.h>
#include <algorithm>
#include <math.h>
#define for0(i, n) for(int i = 0; i < n; i++)
using namespace std;
bool isPalidrom(uint64_t x){
    char s[110];
    sprintf(s, "%I64d", x);
    int l = strlen(s);
    if( l < 2){
        return true;
    }
    for(int i = 0; i < l / 2; i++){
        if(s[i] != s[l - 1 - i]){
            return false;
        }
    }
    return l % 2 ? true : s[l / 2 - 1] == s[l / 2];
}
int main() {
    ifstream in("common.in");
    ofstream out("common.out");
    uint64_t testCount, a, b;
    in>>testCount;

    for0(k, testCount){
        out<<"Case #"<<(k + 1)<<": ";
        in>>a>>b;
        int c = sqrt(b);
        int count = 0;
        uint64_t i = sqrt(a);
        while(i * i < a){
            i++;
        }
        for(; i <= c; i++){
            if(isPalidrom(i) && isPalidrom(i * i)){
                count++;
            }
        }
        out<<count<<"\n";
    }
    return 0;
}
