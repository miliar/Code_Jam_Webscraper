#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long int64;
typedef pair<int, int> ii;

struct node{
    int x, y;
    node(int x = 0, int y = 0) : x(x), y(y) {}
};

unordered_map<int, int> bib;

void countDigits(int n){
    while ( n ){
        bib.insert(mp(n % 10, 1));
        n /= 10;
    }
}

int main(){
    ios::sync_with_stdio(false);
    int n, t;
    cin >> t;
    for ( int k = 1; k <= t; k++ ){
        cout << "CASE #" << k << ": ";
        cin >> n;
        int i = 1, flag = 0;
        while ( n != 0 ){
            countDigits(i*n);
            if ( bib.size() == 10 ){
                flag = true;
                break;
            }
            i++;
        }
        if ( flag ) cout << i*n << endl;
        else cout << "INSOMNIA\n";
        bib.clear();
    }
    return 0;
}