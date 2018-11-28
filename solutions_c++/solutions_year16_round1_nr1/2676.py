#include<cstdio>
#include<string>
#include<iostream>
using namespace std;

int T, C=1;
string S;

int main(){
    scanf("%d", &T);
    while(T--){
        string w = "";
        cin >> S;
        w = S[0];
        for(int i = 1; i < S.size(); ++i){
            if(S[i] >= w[0]) w = S[i] + w;
            else w = w + S[i];
        }
        printf("Case #%d: %s\n", C++, w.c_str());
    }
}
