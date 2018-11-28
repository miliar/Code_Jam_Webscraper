

//#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <vector>
#include <set>

int y[10];

void fun(long long int a){
    while (a>0){
        y[a%10]=1;
        a=a/10;
    }
}
using namespace std;
int main(){
//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
    long long int a;
    int t;
    cin >> t;
    for (int k = 0; k < t; ++k){
        string s;
        cin >> s;
        cout << "CASE #" << k+1 << ": ";
        bool frs = 0, lst = 0;
        if (s[0]=='+')
            frs = 1;
        if (s[s.length()-1]=='+')
            lst = 1;
        int minus = 0, plus = 0;
        string f;
        f.push_back(s[0]);
        for (int i = 1; i < s.length(); ++i){
            if (s[i] != s[i-1])
                f.push_back(s[i]);
        }
        for (int i = 0; i < f.length(); ++i)
            if (f[i] == '-')
                minus++;
        plus = f.length() - minus;
        if (plus == 0){
            cout << 1 << endl;
            continue;
        }
        if (minus == 0){
            cout << 0 << endl;
            continue;
        }
        int ans = 0;
        if (lst && frs){
            ans = 2*minus;
        }
        else if (lst && !frs){
            ans = 2*(plus-1)+1;
        }
        else if (!lst && frs){
            ans = 2*minus;
        }
        else if (!lst && !frs){
            ans = 2*plus+1;
        }
        cout << ans << endl;
    }
    return 0;
    
}