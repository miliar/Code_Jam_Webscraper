#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll maxx;

ll to_ll(string a) {
    int n = a.size();
    ll ans = 0;
    for(int i = 0; i < n; ++i)
        ans = ans * 10LL + (a[i] - '0');
    return ans;
}

void ret(int poz, string &A, string &B, string &a, string &b, int larger) {
    if(poz == (int) A.size()) {
        ll f = to_ll(A);
        ll s = to_ll(B);
        
        if(abs(f - s) == maxx && (A == a) && (B < b)) {
            a = A;
            b = B;
        }

        if(abs(f - s) == maxx && A < a) {
            a = A;
            b = B;
        }

        if(abs(f - s) < maxx) {
            maxx = abs(f - s);
            a = A;
            b = B;
        }
        return;
    }

    if(A[poz] != '?' && B[poz] != '?') {
        if(larger == 0 && A[poz] > B[poz])
            larger = -1;
        else if(larger == 0 && A[poz] < B[poz])
            larger = 1;
        ret(poz + 1, A, B, a, b, larger);
    } else if(A[poz] == '?' && B[poz] == '?') {
        if(larger != 0) {
            A[poz] = '0';
            B[poz] = '9';
            if(larger == 1)
                swap(A[poz], B[poz]);
            ret(poz + 1, A, B, a, b, larger);
        } else {
            A[poz] = '0';
            B[poz] = '0';
            ret(poz + 1, A, B, a, b, larger);
            A[poz] = '1';
            ret(poz + 1, A, B, a, b, -1);
            A[poz] = '0';
            B[poz] = '1';
            ret(poz + 1, A, B, a, b, 1);
        }
        A[poz] = '?';
        B[poz] = '?';
    } else if(A[poz] == '?') {
        if(larger != 0) {
            if(larger == -1)
                A[poz] = '0';
            else
                A[poz] = '9';
            ret(poz + 1, A, B, a, b, larger);
        } else {
            A[poz] = B[poz];
            ret(poz + 1, A, B, a, b, larger);
            if(B[poz] != '9') {
                A[poz] = B[poz] + 1;
                ret(poz + 1, A, B, a, b, -1);
            } 

            if(B[poz] != '0') {
                A[poz] = B[poz] - 1;
                ret(poz + 1, A, B, a, b, 1);
            }
        }
        A[poz] = '?';
    } else if(B[poz] == '?') {
        if(larger != 0) {
            if(larger == -1)
                B[poz] = '9';
            else
                B[poz] = '0';
            ret(poz + 1, A, B, a, b, larger);
        } else {
            B[poz] = A[poz];
            ret(poz + 1, A, B, a, b, larger);
            if(A[poz] != '9') {
                B[poz] = A[poz] + 1;
                ret(poz + 1, A, B, a, b, 1);
            } 

            if(A[poz] != '0') {
                B[poz] = A[poz] - 1;
                ret(poz + 1, A, B, a, b, -1);
            }
        }
        B[poz] = '?';
    }
}

int main() {
    ifstream cin("testB.in");
    ofstream cout("testB.out");
    
    int t; cin >> t;
    
    for(int t_case = 0; t_case < t; ++t_case) {
        cout << "Case #" << t_case + 1 << ": ";
        
        string A, B; cin >> A >> B;
        string a, b;
        
        maxx = 1000000000000000000LL;
        ret(0, A, B, a, b, 0);

        cout << a << " " << b << "\n";
    }
}
