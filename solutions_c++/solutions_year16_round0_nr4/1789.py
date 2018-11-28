#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0), cout.precision(15);
    //O(T*K)
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; cas ++){
        //K 1 100 C 1 100 K^C <= 1e18 S <= K
        int K, C, S;
        cin >> K >> C >> S;
        cout << "Case #" << cas << ":";
        if(C == 1){
            if(S == K){
                for(int i = 1; i <= K; i++){
                    cout << " " << i;
                }
                cout << endl;
            }else{
                cout << " IMPOSSIBLE" << endl;
            }
        }else{
            //ceil(K/2)
            int cnt = K/2;
            if(K%2) {
                cnt ++;
            }
            if(S >= cnt){
                //if find L at first group, then [1...k] groups are 
                //created from first L
                //
                //ith is L-group, jth(j = K + 1 - i) is also L-group
                //otherwise found G
                //
                //at most know two groups each step
                for(int i = 1, j = K; i <= j; i++, j--){
                    //<= K^2 <= 1e4
                    cout << " " << (i - 1)*K + j;
                }//if generate K L groups from the first L, no G.
                cout << endl;
            }else{
                cout << " IMPOSSIBLE" << endl;
            }
        }
    }
    return 0;
}
