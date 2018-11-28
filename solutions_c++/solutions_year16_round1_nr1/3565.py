#include<iostream>
using namespace std;

int main(){
    int T, N, i, cases, right;
    string S, lastWord;
    cin>>T;
    cases = 1;
    while(cases <= T){
        cin>>S;
        N = S.length();
        lastWord = S[0];
        right = 0;
        for(i = 1; i < N; i++){
            if(S[i] >= lastWord[0]){
                lastWord = S[i] + lastWord;
                right++;
            }
            else{
                lastWord = lastWord + S[i];
                right++;
            }
        }
        cout<<"Case #"<<cases++<<": "<<lastWord<<endl;
    }
    return 0;
}
