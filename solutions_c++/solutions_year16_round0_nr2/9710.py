#include<bits/stdc++.h>

using namespace std;

string flip(string str, int i) {
    while (i >= 0) {
        if (str[i] == '+') str[i--] = '-';
        else str[i--] = '+';
    }

    return str;
}

int main() {
    int n,j,len,t,i;
    string pankakes;

    //freopen("Code Jam Classification - (A).txt", "w", stdout);

    cin >> n;
    for (j=1; j<=n; j++) {
        cin >> pankakes;

        t=0;
        len = (pankakes.size()-1);

        for (i=0; i<len; i++) {
            if (pankakes[i] != pankakes[i+1]) {
                pankakes = flip(pankakes,i);
                t++;
            }
        }
        if (pankakes[i] == '-') {
            pankakes = flip(pankakes,i);
            t++;
        }

        cout << "case #" << j << ": " << t << endl;
    }

    //fclose(stdout);
    return 0;
}