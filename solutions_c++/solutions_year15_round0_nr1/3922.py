#include <bits/stdc++.h>
using namespace std;

int main () {
    int tcase;
    scanf("%d", &tcase);
    for (int j = 1; j <= tcase; ++j) {
        int target;
        scanf("%d", &target);
        char input[1005];
        scanf("%s", input);

        int total = 0, invite = 0;
        for (int i = 0; i <= target; ++i) {
            //cout << total << " i: " << i << " target: " << target << endl;
            if (total >= target) break;
            if (total >= i) total += (input[i]-'0');
            else {
                //cout << "i: " << i << "total: " << total << endl;
                invite += i-total;
                total += i-total;
                total += (input[i]-'0');
            }
        }

        printf("Case #%d: %d\n", j, invite);
    }
    return 0;
}
