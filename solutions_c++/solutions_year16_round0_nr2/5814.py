#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int n, k;
string str;

int ar[1000];

bool check(int len){
    for (int i = 0; i < len; ++i){
        if (ar[i] == 0){
            return true;
        }
    }
    return false;
}

void solve(string str){
    int n = str.size();
    for (int i = 0; i < n; ++i){
        ar[i] = (str[i] == '+') ? 1 : 0;
    }

    int last = 0;
    int first = 0;
    int count = 0;

    while (check(n)){
        //cout << "count: " << count << endl;
        last = n - 1;
        while (last >= 0 && ar[last]) last --;
        last ++;
        //cout << last << endl;
        first = 0;
        while (first <= n && ar[first]) first ++;
        //cout << first << endl;
        if (first){
            count++;
            for (int i = 0; i < first; ++i){
                ar[i] = 0;
            }
        }
        count ++;
        for (int i = 0; i < last / 2 + last % 2; ++i){
            //cout << i << " " << last - i << endl;
            int temp = ar[i];
            ar[i] = 1 - ar[last - 1 - i];
            ar[last - 1 - i] = 1 - temp;
        }
        //for (int i = 0; i < n; ++i){
        //    cout << ar[i];
        //}
        //cout << endl;
    }

    cout << count << endl;
}

int main(){

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> k;
    for (int i = 0; i < k; ++i){
        cin >> str;
        cout << "Case #" << i + 1 << ": ";
        //cout << endl << str << endl;
        solve(str);
    }

    return 0;
}
