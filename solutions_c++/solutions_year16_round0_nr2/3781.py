#include <iostream>

using namespace std;

struct Stack {
    void flip(int idx) {
        auto j = idx;
        for(auto i = 0; i <= j; i++, j--) {
            auto tmp = happy[i];
            happy[i] = not happy[j];
            happy[j] = not tmp;
        }

        for(; (rightmost_sad >= 0) and (happy[rightmost_sad]); rightmost_sad--);
        if(rightmost_sad == -1) {
            leftmost_sad = -1;
        } else {
            for(leftmost_sad = 0; (happy[leftmost_sad]) and (leftmost_sad < rightmost_sad); leftmost_sad++);
        }
    }

    bool happy[128];
    int rightmost_sad;
    int leftmost_sad;

} stack;

void solve()
{
    string input;
    cin >> input;

    stack.rightmost_sad = -1;
    stack.leftmost_sad = -1;
    int ans = 0;
    for(auto i = 0u; i < input.size(); i++) {
        if(not (stack.happy[i] = (input[i] == '+'))) {
            if(stack.leftmost_sad == -1) {
                stack.leftmost_sad = i;
            }
            stack.rightmost_sad = i;
        }
    }

    while(stack.rightmost_sad >= 0) {
        /*
        for(int i = 0; i < input.size(); i++) {
            cout << (stack.happy[i] ? '+' : '-');
        }
        cout << endl << stack.leftmost_sad << " " << stack.rightmost_sad << endl;
        */

        ans++;
        if(stack.happy[0]) {
            stack.flip(stack.leftmost_sad - 1);
        } else {
            stack.flip(stack.rightmost_sad);
        }
    }

    /*
    for(int i = 0; i < input.size(); i++) {
        cout << (stack.happy[i] ? '+' : '-');
    }
    cout << endl << stack.leftmost_sad << " " << stack.rightmost_sad << endl;
    */
    cout << ans;
}

int main()
{
    unsigned int cases;
    cin >> cases;
    for(auto i = 1u; i <= cases; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
