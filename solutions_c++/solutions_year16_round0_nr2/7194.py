#include <iostream>
using namespace std;

int main() {
    int t,cnt,i,j;
    char s[100], prev;
    cin >> t;
    for(i=1; i<=t; i++) {
        cin >> s;
        prev = s[0];
        cnt = 0;
        for(j=1; s[j]; j++) {
            if(s[j] != prev)
                cnt++;
            prev = s[j];
        }
        if (prev == '-')
            cnt++;
        cout << "Case #" << i << ": " << cnt << endl;
    }

    return 0;
}
