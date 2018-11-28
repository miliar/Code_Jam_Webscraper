#include <iostream>

using namespace std;

int test(){
    int maxLevel;
    int helper = 0;
    int total = 0;
    cin >> maxLevel;
    // blank
    getchar();
    for ( int i = 0; i < maxLevel + 1; ++i ){
        int num = getchar() - '0';
        // cout << num;
        if (num == 0) {
            continue;
        }
        if (total < i) {
            helper += i - total;
            total = i;
        }
        total += num;
    }

    return helper;
}

int main(int argc, char const *argv[]){
    int nCase;
    cin >> nCase;

    for ( int k = 0; k < nCase; ++k ){
        int ans = test();
        cout << "Case #" << k + 1 << ": " << ans << endl; 
    }

    return 0;
}