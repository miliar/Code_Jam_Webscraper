#include<iostream>
#include<conio.h>
#include<stdlib.h>
#include <stdio.h>

#define ll long long

using namespace std;

void arrayInitialise (int A[], int n) {
    int i;
    for (i=0;i<10;i++) A[i] = 0;
}

int findNew(int A[], ll n) {
    int mod, c=0;
    while (n>0) {
        mod = n%10;
        if (A[mod]==0) {
            A[mod] = 1;
            c++;
        }
        n = n/10;
    }
    return c;
}

ll operate(ll n) {
    int A[10], c = 0;
    arrayInitialise(A,n);
    ll val=0;
    while (1) {
        val = val + n;
        c = c + findNew(A,val);
        if (c == 10) break;
    }
    return val;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output1-large.out", "w", stdout);
    int t, i;
    cin >> t;
    for (i=1;i<=t;i++) {
        ll n;
        cin >> n;
        cout << "Case #" << i << ": " ;
        if (n==0) {
            cout << "INSOMNIA" << endl;
        }
        else {
            cout << operate(n) << endl;
        }
    }
    return 0;
}
