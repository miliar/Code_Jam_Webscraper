#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

void problem(int cn) {
    int n;
    cin >> n;
    char z[n];
    for(int i=0; i<=n; i++)
        cin >> z[i];
    
    int br = z[0]-'0';
    int x = 0;
    for(int i=1; i<=n; i++) {
        if(br+x<i) x++;
        br += z[i]-'0';
    }
    cout << "Case #" << cn << ": " << x << endl;
}

int main() {
    int T;
    cin >> T;
    for(int i=1; i<=T; i++)
        problem(i);
    return 0;
}
