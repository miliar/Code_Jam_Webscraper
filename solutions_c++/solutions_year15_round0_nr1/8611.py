#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; i++) {
        int maxShyness;
        cin >> maxShyness;

        string audience;
        cin >> audience;

        int friends = 0; // :(
        int standing = 0;
        for (int needed = 0; needed <= maxShyness; needed++) {
            int audienceThisShy = audience[needed] - '0';
            if (audienceThisShy > 0 && needed > standing) {
                friends += needed - standing;
                standing += needed - standing;
            }

            standing += audienceThisShy;
        }

        printf("Case #%d: %d\n", i + 1, friends);
    }
    
    return 0;
}
