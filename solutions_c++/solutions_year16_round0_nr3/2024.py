#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
using namespace std;
#define ll long long
#define TOP ((ll)3 << (N-2))
#define BOTTOM (ll)3
FILE * ifp = fopen("/Users/clsrn1581/Desktop/codejam/C/C-large.in", "r");
FILE * ofp = fopen("/Users/clsrn1581/Desktop/codejam/C/C-large.out", "w");
int Count = 0;
int T, N, J;
void printD(){
    for(int i = 2; i<= 10; i++)
        fprintf(ofp, "%d ", i+1);
    fprintf(ofp, "\n");
}
void printB(ll bit){
    vector<int> p;
    while(bit){
        p.push_back(bit%2);
        bit /= 2;
    }
    for(int i = (int)p.size()-1; i>= 0 ; i--)
        fprintf(ofp, "%d", p[i]);
    fprintf(ofp, " ");
}void back(int i, ll bit){
    
    if(Count >= J)
        return;
    if(i >= N-2){
        printB(bit);
        printD();
        Count++;
        return;
    }
    
    back(i+2, bit | ((ll)3<< i));
    back(i+2, bit);
}
void process(){
    //한 세트
    Count=0;
    back(2, TOP | BOTTOM);
}
int main(){
    fscanf(ifp, "%d", &T);
    for(int t = 1 ; t <= T; t++){
        fscanf(ifp, "%d%d", &N, &J);
        fprintf(ofp , "Case #%d: \n", t);
        process();
    }
}