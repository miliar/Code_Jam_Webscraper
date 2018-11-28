#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {

    ll t, n, m, i, j, k, a, b, x, th;
    t = 1;
    string s, c;
    cout<<"Case #1:"<<endl;
    while(t--) {
        n = 16; j = 50;
        th = 1000;
        s = "1000000000000001";
        while(j>0) {
            vector<ll> v;
            c = "000000000";
            a = 0;
            k = 0; x = 1; b = 2;
            for (i=15; i>=0; i--) {
                k += x*(s[i]-'0');
                x = x*b;
            }
            
            for (i=2; i<th; i++) {
                if (k%i == 0) {
                    break;
                }
            }
            
            if (i==th) {
                
                if (s[15] == '0') {
                s[15] = '1';
            }
            else {
                s[15] = '1';
                for (i=14; i>=0; i--) {
                    if (s[i]=='1') {
                        s[i] = '0';
                    }
                    else {
                        s[i] = '1';
                        break;
                    }
                }
            }
            continue;
                
            }
            v.push_back(i);
            c[a] = '1';
            a++;

            k = 0; x = 1; b = 3;
            for (i=15; i>=0; i--) {
                k += x*(s[i]-'0');
                x = x*b;
            }
            
            for (i=2; i<th; i++) {
                if (k%i == 0) {
                    break;
                }
            }

            if (i==th) {
                
                if (s[15] == '0') {
                s[15] = '1';
            }
            else {
                s[15] = '1';
                for (i=14; i>=0; i--) {
                    if (s[i]=='1') {
                        s[i] = '0';
                    }
                    else {
                        s[i] = '1';
                        break;
                    }
                }
            }
            continue;
            }
            v.push_back(i);
            c[a] = '1';
            a++;

            k = 0; x = 1; b = 4;
            for (i=15; i>=0; i--) {
                k += x*(s[i]-'0');
                x = x*b;
            }
            
            for (i=2; i<th; i++) {
                if (k%i == 0) {
                    break;
                }
            }

            if (i==th) {
                
                if (s[15] == '0') {
                s[15] = '1';
            }
            else {
                s[15] = '1';
                for (i=14; i>=0; i--) {
                    if (s[i]=='1') {
                        s[i] = '0';
                    }
                    else {
                        s[i] = '1';
                        break;
                    }
                }
            }
            continue;
            }
            v.push_back(i);
            c[a] = '1';
            a++;

            k = 0; x = 1; b = 5;
            for (i=15; i>=0; i--) {
                k += x*(s[i]-'0');
                x = x*b;
            }
            
            for (i=2; i<th; i++) {
                if (k%i == 0) {
                    break;
                }
            }

            if (i==th) {
                
                if (s[15] == '0') {
                s[15] = '1';
            }
            else {
                s[15] = '1';
                for (i=14; i>=0; i--) {
                    if (s[i]=='1') {
                        s[i] = '0';
                    }
                    else {
                        s[i] = '1';
                        break;
                    }
                }
            }
            continue;
            }
            v.push_back(i);
            c[a] = '1';
            a++;

            k = 0; x = 1; b = 6;
            for (i=15; i>=0; i--) {
                k += x*(s[i]-'0');
                x = x*b;
            }
            
            for (i=2; i<th; i++) {
                if (k%i == 0) {
                    break;
                }
            }

            if (i==th) {
                
                if (s[15] == '0') {
                s[15] = '1';
            }
            else {
                s[15] = '1';
                for (i=14; i>=0; i--) {
                    if (s[i]=='1') {
                        s[i] = '0';
                    }
                    else {
                        s[i] = '1';
                        break;
                    }
                }
            }
            continue;
            }
            v.push_back(i);
            c[a] = '1';
            a++;

            k = 0; x = 1; b = 7;
            for (i=15; i>=0; i--) {
                k += x*(s[i]-'0');
                x = x*b;
            }
            
            for (i=2; i<th; i++) {
                if (k%i == 0) {
                    break;
                }
            }

            if (i==th) {
                
                if (s[15] == '0') {
                s[15] = '1';
            }
            else {
                s[15] = '1';
                for (i=14; i>=0; i--) {
                    if (s[i]=='1') {
                        s[i] = '0';
                    }
                    else {
                        s[i] = '1';
                        break;
                    }
                }
            }
            continue;
            }
            v.push_back(i);
            c[a] = '1';
            a++;

            k = 0; x = 1; b = 8;
            for (i=15; i>=0; i--) {
                k += x*(s[i]-'0');
                x = x*b;
            }
            
            for (i=2; i<th; i++) {
                if (k%i == 0) {
                    break;
                }
            }

            if (i==th) {
                
                if (s[15] == '0') {
                s[15] = '1';
            }
            else {
                s[15] = '1';
                for (i=14; i>=0; i--) {
                    if (s[i]=='1') {
                        s[i] = '0';
                    }
                    else {
                        s[i] = '1';
                        break;
                    }
                }
            }
            continue;
            }
            v.push_back(i);
            c[a] = '1';
            a++;

            k = 0; x = 1; b = 9;
            for (i=15; i>=0; i--) {
                k += x*(s[i]-'0');
                x = x*b;
            }
            
            for (i=2; i<th; i++) {
                if (k%i == 0) {
                    break;
                }
            }

            if (i==th) {
                
                if (s[15] == '0') {
                s[15] = '1';
            }
            else {
                s[15] = '1';
                for (i=14; i>=0; i--) {
                    if (s[i]=='1') {
                        s[i] = '0';
                    }
                    else {
                        s[i] = '1';
                        break;
                    }
                }
            }
            continue;
            }
            v.push_back(i);
            c[a] = '1';
            a++;

            k = 0; x = 1; b = 10;
            for (i=15; i>=0; i--) {
                k += x*(s[i]-'0');
                x = x*b;
            }
            
            for (i=2; i<th; i++) {
                if (k%i == 0) {
                    break;
                }
            }

            if (i==th) {
                
                if (s[15] == '0') {
                s[15] = '1';
            }
            else {
                s[15] = '1';
                for (i=14; i>=0; i--) {
                    if (s[i]=='1') {
                        s[i] = '0';
                    }
                    else {
                        s[i] = '1';
                        break;
                    }
                }
            }
            continue;
            }
            v.push_back(i);
            c[a] = '1';
            a++;

            
            if (c=="111111111") {
                cout<<s;
                for (i=0; i<v.size(); i++) {
                    cout<<" "<<v[i];
                }
                cout<<endl;
                j--;
            }

            if (s[15] == '0') {
                s[15] = '1';
            }
            else {
                s[15] = '1';
                for (i=14; i>=0; i--) {
                    if (s[i]=='1') {
                        s[i] = '0';
                    }
                    else {
                        s[i] = '1';
                        break;
                    }
                }
            }
        }

    }


    return 0;

}