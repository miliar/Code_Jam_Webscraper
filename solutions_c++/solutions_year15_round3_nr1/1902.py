#include <iostream>
#include <vector>

using namespace std;

int printResult(int C, int W)
{
    if(W == C)
        return W;
    else if(C <= 2*W)
        return W+1;
    else
        return 1+printResult(C-W,W);
}

int main()
{
    int T;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        int R, C, W;
        cin >> R >> C >> W;
        
        cout << "Case #" << i+1 << ": " << printResult(C, W) << endl;
    }
}
