#include<iostream>
#include<conio.h>
#include<stdlib.h>
#include <stdio.h>

#define ll long long

using namespace std;

int getCoun(int A[], int coun, ll n) {
    int k;
    //cout << "inside : n=" << n << endl;
    while (n>0) {
        k = n%10; //getch();
        //cout << "k = " << k;
        if (A[k]==0) {
            A[k]++; coun++;
            //cout << "YO";
        }
        //cout << endl;
        n = n/10;
    }
    return coun;
}

ll getAns(ll n) {
    if (n==0) return -1;
    int A[10], coun = 0;
    for (int i=0;i<10;i++) A[i] = 0;
    ll i = 2, k=n;

    while (coun != 10) {
        //cout << "C : " << coun << " N : " << k << endl;
        coun = getCoun(A,coun,k);
        k = n * i;
        i++;
    }
    return n*(i-2);
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output1-large.out", "w", stdout);
    int t, i;
    cin >> t;
    for (i=1;i<=t;i++) {
        cout << "Case #" << i << ": " ;
        ll n;
        cin >> n;
        ll ans = getAns(n);
        if (ans>0) cout << ans << endl;
        else cout << "INSOMNIA" << endl;
    }
    return 0;
}
