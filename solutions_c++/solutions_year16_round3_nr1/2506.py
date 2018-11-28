#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <string.h>
#include <cmath>

using namespace std;

int getFirstPosition(int* a, int n) {
    int res = 0;
    for (int i=1; i<n; i++) {
        if (a[i] > a[res]) {
            res = i;
        }
    }
    return res;
}

int getSecondPosition(int* a, int n) {
    int res;
    int first = getFirstPosition(a, n);
    if (first == 0) res = 1;
    else res = 0;
    //cout << "s";
    for (int i=1; i<n; i++) {
        //cout  <<  a[i] << endl;
        if (a[i] > a[res] && i!= first) {
            res = i;
        }
    }
    return res;
}
int main () {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        cout << "Case #" << i+1 << ": ";
        int m, sum=0;
        cin >> m;
        int a[m];
        for (int j=0; j<m; j++) {
            cin >> a[j];
            sum += a[j];
        }
        int num = 0;
        while(num != sum) {
            int first = getFirstPosition(a, m);
            int second = getSecondPosition(a, m);
            //cout << first << second << endl;
            if (a[first] > a[second] || (a[first] == 1 && num != sum -2)) {
                char c = 'A' + first;
                cout << c << " ";
                a[first]--;
                num++;
            } else {
                //cout << "bbb" << endl;
                char c1 = 'A' + first;
                char c2 = 'A' + second;
                cout << c1 << c2 << " ";
                a[first]--;
                a[second]--;
                num+=2;
            }
            //cout << endl;
            //for (int j=0; j<m; j++) {
            //    cout << a[j];
            //}
            //cout << endl;
        }
        cout << endl;
     }
  return 0;
}
