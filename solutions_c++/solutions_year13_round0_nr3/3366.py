#include<stdio.h>
#include<stdlib.h>
#include<vector>
using namespace std;
vector <long long int> res;
long long int dig[20];
int p;
bool resp;
bool ver (long long int k) {
    p = 0;
    while(k != 0) {
        dig[++p] = k%10;
        k = k/10;
    }
    resp = true;
    for (int ca = 1; ca <= p/2; ca++) {
        if (dig[ca] != dig[p-ca+1]) resp = false;
    }
    return resp;
}
int maior (long long int k) {
    int x = res.size()-1;
    if (k > res[x]) return x+1;
    int ini = 0;
    int fim = x;
    while (fim-ini>1) {
        int m = (ini+fim)/2;
        if (res[m] == k) return m;
        else if (res[m] > k) fim = m;
        else ini = m;
    }
    if (res[ini] > k) return ini;
    return fim;
}
int menor (long long int k) {
    int x = res.size()-1;
    if (k < res[0]) return 0;
    int ini = 0;
    int fim = x;
    while(fim-ini>1) {
        int m = (ini+fim)/2;
        if (res[m] == k) return m;
        else if (res[m] > k) ini = m;
        else fim = m;
    }
    if (res[fim] < k) return fim;
    return ini;
}
int main () {
    int t;
    ver(100001*100001);
    for (long long int michel = 1; michel <= 10000000; michel++) {
        if (ver(michel)) {
            if (ver(michel*michel)) {
                res.push_back(michel*michel);
            }
        }
    }
    scanf("%d", &t);
    long long int a, b;
    for (int lo = 1; lo <= t; lo++) {
        scanf("%lld %lld", &a, &b);
        printf("Case #%d: ", lo);
        int A, B;
        for (int c = 0; c < res.size(); c++) {
            if (res[c] >= a){
                A = c;
                break;
            }
        }
        for (int c = 0; c < res.size(); c++) {
            if (res[c] > b){
                B = c-1;
                break;
            }
        }
        printf("%d\n", B-A+1);
    }
    return 0;
}
    
        
