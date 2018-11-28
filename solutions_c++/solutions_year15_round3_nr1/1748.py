#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        int R, C, W;
        cin >> R >> C >> W;

        int maxHitGuessesPerRow = C / W;
        int maxGuessesPerRow = maxHitGuessesPerRow + W - 1;
        bool lastHitAtEndOfShip = C % W == 0;
        if (!lastHitAtEndOfShip)
            ++maxGuessesPerRow;

        cout << "Case #" << i << ": " << maxGuessesPerRow * R << endl;
    }
    return 0;
}
