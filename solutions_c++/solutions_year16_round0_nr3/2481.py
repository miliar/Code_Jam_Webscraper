#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int p[100001];
int np;
void sieve()
{
    int n=100000;
    int i,j;
    int a[100001];
    memset (a, 0, sizeof(a));
    for (i=4; i<=n; i=i+2) a[i]=1;
    for(i=3;i*i<=n;i++) {
        if (a[i]==0){
            j=i*i;
            while (j<=n) {
                a[j]=1;
                j=j+2*i;
            }
        }
    }
    j = 0;
    for (i = 2; i<100001; i++) {
        if(a[i] == 0) {
            p[j++] = i;
        }
    }
    np = j;
}            
 
string next(string s) {
    int j = s.length()-2;
    while (s[j] != '0' && j>=0) j--;
    if (j<0) return s;
    s[j] = '1';
    for (int k = j+1; k < s.length() -1; k++) {
        s[k] = '0';
    }
    return s;
}
unsigned long long pow(int b, int n) {
    unsigned long long res = 1;
    for (int i=0; i<n; i++) {
        res *= b;
    }
    return res;
}

unsigned long long cal(string s, int b) {
    unsigned long long res = 0;
    for (int i=0; i<s.length(); i++) {
        if (s[i] != '0') res += (unsigned long long) pow(b, s.length() -i -1);
    }
    return res;
}
unsigned long long check(unsigned long long n) {
    for (int i = 0; i < np && p[i] < n; i++) {
        if (n % p[i] == 0) {
            return p[i];
        }
    }
    return 0;
}
bool process(string s) {
    unsigned long long a[9];
    memset(a, 0, sizeof(a));
    int i;
    for (i=2; i<11; i++) {
        unsigned long long t = check (cal (s, i));
        if (t != 0) {
            a[i-2] = t;
        } else {
            return false;
        }
    }
    if (i==11) {
        cout << s << " ";
        for (int j=0; j<8; j++) {
            cout << a[j] << " ";
        }
        cout << a[8] << endl;
        return true;
    }
    return false;
}
int main () {
    int m;
    sieve();
    cin >> m;
    for (int i=0; i<m; i++) {
        cout << "Case #" << i+1 << ":" << endl;
        int n, j;
        cin >> n >> j;
        string s;
        if ( n == 6) {
            s = "100001";
        }
        else if (n == 16) {
            s = "1000000000000001";
        } else {
            s = "10000000000000000000000000000001";
        }
        int count = 0;
        while (count < j) {
            if (process(s) == true) count++;
            s = next(s);
        }
     }
  return 0;
}
