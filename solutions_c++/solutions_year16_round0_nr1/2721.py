#include <iostream>
#include <cstdio>

using namespace std;

bool digits[10] = {false};

bool nottrue() {
    for(int i = 0; i <= 9; i++) {
        if(!digits[i])
            return true;
    }
    return false;
}

int main() {
    
    freopen("sheep.in", "r", stdin);
    freopen("sheep.out", "w", stdout);

    int N;
    cin >> N;

    for(int i = 1; i <= N; i++) {
        long long num;
        cin >> num;
        long long ans = 0;
        if(num == 0)
            cout << "Case #" << i << ": INSOMNIA" << endl;
        else {
            while(nottrue()) {
                ans += num;
                long long tmp = ans;
                while(tmp > 0) {
                    digits[tmp%10] = true;
                    tmp /= 10;
                }
            }
            cout << "Case #" << i << ": " << ans << endl;
        }
        for(int j = 0; j < 10; j++)
            digits[j] = false;
    }
    return 0;
}
