#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int TC;
    cin >> TC;
    int test= 1;
    while(TC--){
        int A, B, K;
        cin >> A >> B >> K;

        int ans= 0;
        for(int i= 0; i< A; i++){
            for(int j= 0; j< B; j++){
                if((i&j) < K){
                    ans++;
                }
            }
        }

        cout << "Case #" << test << ": " << ans << endl;
        test++;
    }
}
