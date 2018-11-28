#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

#define ll long long
bool ck[10];
ll ckCount;

// 숫자 구성 확인 하는 모듈
void ckComposition(string & str){
    for(int i = 0 ; i < str.length(); i++){
        if(ck[str[i]-'0'] == 0){
            ckCount++;
            ck[str[i]-'0'] = true;
        }
    }
}
ll process(ll N){
    //초기화
    for(int i =0 ; i< 10 ; i++)
        ck[i] = 0;
    ckCount = 0;
    
    for(ll i = 1; i ; i++){
        string str = to_string(i*N);
        ckComposition(str);
        if(ckCount == 10){
            return i;
        }
    }
    return 0;
}

int main(){
    int T, N;
    FILE * ifp = fopen("/Users/clsrn1581/Desktop/codejam/A/A-large.in", "r");
    FILE * ofp = fopen("/Users/clsrn1581/Desktop/codejam/A/A-large.out", "w");
    
    fscanf(ifp, "%d", &T);
    for(int t = 1 ; t <= T; t++){
        fscanf(ifp, "%d", &N);
        if(N==0)
            fprintf(ofp, "Case #%d: INSOMNIA\n", t);
        else{
            ll ans = process(N);
            fprintf(ofp , "Case #%d: %lld\n", t, ans*N);
        }
    }
}