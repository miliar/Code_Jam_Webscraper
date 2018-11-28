#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int main()
{
    int T, D;
    priority_queue<int> P, TQ;
    int temp, top, max, give, solution;
    cin >> T;
    
    for(int i = 1; i <= T; i++){
        cin >> D;
        /* Reading */
        P = priority_queue<int>();
        for(int j = 0; j < D; j++){
            cin >> temp;
            P.push(temp);
        }
        /* Iterate over solutions */
        top = P.top();
        solution = top;
        for(give = 2; give <= (top+1)/2; give++){
            TQ = priority_queue<int>(P);
            for(int k = 1; k <= top; k++){
                 max = TQ.top();
                 TQ.pop();
                 TQ.push(give);
                 TQ.push(max-give);
                 solution = min( TQ.top() + k, solution);
             }
        }
        cout << "Case #" << i << ": " << solution << "\n";
    }
}

