/* 
 * File:   main.cpp
 * Author: Anton Boytsov
 *
 * Created on 12 Май 2013 г., 14:54
 */

#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool iscon(char c) {
    
    if (c == 'a' || c == 'u' || c == 'i' || c == 'o' || c == 'e')
        return false;
    return true;
    
}

vector<int> a, b;

int main() {
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    //ios_base::sync_with_stdio(false);
    
    int t;
    cin >> t;
    for (int q = 0; q < t; q++) {
        
        string s;
        int n;
        cin >> s >> n;
        
        a.clear();
        a.assign(s.size(), 0);
        
        if (iscon(s[0]))
            a[0] = 1;
        
        for (int i = 1; i < s.size(); i++) {
            if (iscon(s[i]))
                a[i] = a[i - 1] + 1;
            else
                a[i] = 0;
        }
        

        b.clear();
        for (int i = 0; i < a.size(); i++) {
            if (a[i] >= n) {
                b.push_back(i - n + 1);
            }
        }
        
        long long all = 0;
        int k = 0;
        for (int i = 0; i < a.size(); i++) {
            if (b[k] < i)
                k++;
            if (k >= b.size())
                break;
            long long l = a.size() - (b[k] + n - 1);
            all += l;
        }
        
        cout << "Case #" << (q + 1) << ": " << all << "\n";
        
    }
    
    return 0;
}