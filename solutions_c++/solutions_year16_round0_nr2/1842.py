//proof:
//if res = groups - 1, it must be the shortest solution because
//we decrease groups at most 1 after a slip. 
//
//if res = groups - 1 + 1, it also be the shortest solution because
//we can't have groups - 1 solution:
//
//if we have groups - 1 solution, we decrease groups after each flip
//that is to say, l and the r point have the same side which is 
//different from r + 1 before the flip and same after the flip.
//that is to say, the new l point "copy" the old l point's side as if
//the l/top pancake flip itself at l. that is to say, if we decrease
//the groups in groups - 1 steps, the top/l pancake flip each time and 
//the side will be the same after any groups - 1 decreasing steps.
//if the side is not happy side, we have to flip it again whatever the 
//groups - 1 decreasing steps.
//
//O(T*|S|)
#include <iostream>
#include <string>
using namespace std;
int main(int argc, char **argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0), cout.precision(15);
    //1 100
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; cas ++){
        //size 1 100
        string S;
        cin >> S;
        int n = S.size();
        int diffs = 0;
        for(int i = 1; i < n; i++){
            if(S[i] != S[i - 1]){
                //different group
                diffs ++;
            }
        }
        //<= n
        int res = diffs;
        if(((S[0] == '+') && (diffs%2)) || ((S[0] == '-') && ((diffs%2) == 0))){
            res ++;
        }
        cout << "Case #" << cas << ": " << res << endl;
    }
    return 0;
}
