#include <iostream>
#include <algorithm>
using namespace std;

int levels[1002];

int process(int M) {
    int re = 0;
    int prev = levels[0];
    for(int i=1; i<=M; i++){
        if(i <= prev) {
            prev += levels[i];
        } else {
            re += i - prev;
            prev = i + levels[i];
        }
    }
    return re;
}

int main() {
    int T;
    cin>>T;
    for(int tcas=1; tcas<=T; tcas++) {
        int M;
        string input;
        cin>>M>>input;
        for(int i=0; i<=M; i++) 
            levels[i] = input[i] - '0';
        cout<<"Case #"<<tcas<<": "<<process(M)<<endl;
    }
}
        
