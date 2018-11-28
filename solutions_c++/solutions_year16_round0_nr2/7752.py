#include<cstdio>
#include<iostream>
int main() {
    int n, x;
    scanf("%d\n", &n);
    for (int i = 1; i <= n; ++i) {
        std::string pancakes;
        std::getline (std::cin, pancakes);
        bool start = false;
        int moves = 0;
        for(int j = 0; j < pancakes.length(); ++j) {
            if(pancakes[j] == '+') {
                start = true;
            } else {
                while(pancakes[j] == '-' && j != pancakes.length() - 1)
                    ++j;
                if(pancakes[j] == '+')
                    --j;
                if(start)
                    moves += 2;
                else
                    moves += 1;
                start = true;
            }
        }
        printf("Case #%d: %d\n", i, moves);
    }
}
