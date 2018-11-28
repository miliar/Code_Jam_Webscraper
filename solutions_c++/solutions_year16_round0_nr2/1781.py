#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>

using namespace std;



int main(){
    FILE *KAC;
    KAC = fopen("/Users/hashimototatsuya/Downloads/B-large.in","r");
    
    int T;
    fscanf(KAC,"%d",&T);
    for (int t=0; t < T; t++) {
        char S[108];
        fscanf(KAC,"%s",S);
        int len = strlen(S);
        int Fcount = 0;
        
        int i;
        for ( i = 1; i < len; i++) {
            if (S[i] != S[i-1]) {
                Fcount++;
            }
        }
        if(S[i-1] == '-'){
            Fcount++;
        }
        cout << "Case #" << t+1 << ": " << Fcount << endl;
    }
    
    fclose(KAC);
    return 0;
}