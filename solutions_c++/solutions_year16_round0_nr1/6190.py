#include <cstdio>
#include <set>
#include <string>

void addDigitsToSet(std::string s, std::set<char> &set){
    for (char c : s)
        set.insert(c);
}

int main( void ) {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        int n;
        scanf("%d", &n);
        //from 1 up to 10^6 ( prooved by brute-force =D ) only 0 gives INSOMNIA
        if(n == 0) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        //loop until find all 10 digits
        std::set<char> digits;
        int j;
        for (j = 0; digits.size() != 10; ) {
            j += n;
            addDigitsToSet(std::to_string(j), digits);
        }
        
        printf("Case #%d: %d\n", i, j);
    }
    
}
