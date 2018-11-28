#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>


using namespace std;

int match[10];
unsigned long nomatch, n;

void putMatch(unsigned long n) {
    while(n != 0) {
        if(match[n%10] == 0) {
            match[n%10] = 1; nomatch++;
        }
        n /= 10;
    }
}

unsigned long process() {
    if( n== 0 ) return 0;
    int i = 0;
    for(i=0;i<10;i++) match[i] = 0;
    nomatch = 0;
    for(i=1;;i++) {
        putMatch(n*i);
        if(nomatch == 10) break;
    }
    return n*i;
}

int main() {
    int tcase;
    cin>>tcase;
    for(int i=1;i<=tcase;i++) {
        cin>>n;
        unsigned long num = process();
        cout<<"Case #"<<i<<": ";
        if(num == 0) cout<<"INSOMNIA"<<endl;
        else cout<<num<<endl;
    }
    return 0;
}
