#include <bits/stdc++.h>
#define file "A-small-attempt0"
typedef long long LL;
using namespace std;

const int MOD = 1e9 + 9;
const int N = 30;

void print_two(pair<int, char> *a, int i){
    cout << "Case #" << i << ": ";
    while(a[0].first < a[1].first){
        cout << a[1].second << " ";
        a[1].first--;
    }
    while(a[0].first--)
        cout << a[0].second << a[1].second << " ";
    cout << endl;
}

void print_three(pair<int, char> *a, int i){
    cout << "Case #" << i << ": ";
    while(a[1].first < a[2].first){
        cout << a[2].second << " ";
        a[2].first--;
    }
    while(a[0].first < a[1].first){
        cout << a[1].second << a[2].second << " ";
        a[1].first--;
        a[2].first--;
    }
    while(a[0].first--){
        cout << a[0].second << " " << a[1].second << a[2].second << " " ;
    }
    cout << endl;
}

int main(){
    freopen(file".in", "r", stdin);
    freopen(file".out", "w", stdout);
    int test;
    cin >> test;
    for(int i = 1; i <= test; ++i){
        int n;
        pair<int, char> a[N];
        cin >> n;
        for(int j = 0; j < n; ++j){
            cin >> a[j].first;
            a[j].second = char(j + 'A');
        }
        sort(a, a + n);
        if(n == 2) print_two(a, i);
        else print_three(a, i);
    }
    return 0;
}
