#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <memory.h>
#include <stack>
#include <iomanip>
#include <sstream>
#include <cmath>
using namespace std;

typedef long long int ll;

int main (int argc, char * const argv[]){
    #ifdef LOCAL
        freopen("A1_2.in", "r", stdin);
        freopen("A1.out", "w", stdout);
    #endif // LOCAL

    int ntest;
    while(cin>>ntest){
        for(int tt=0; tt < ntest; tt++){
            int rr;
            int matrix[4][4];
            int counter[17] = {};

            cin >> rr;
            for(int r=0; r<4; r++){
                for(int c=0; c<4; c++){
                    cin >> matrix[r][c];
                }
            }

            for(int c=0; c<4; c++){
                counter[matrix[rr-1][c]]++;
            }

            cin >> rr;
            for(int r=0; r<4; r++){
                for(int c=0; c<4; c++){
                    cin >> matrix[r][c];
                }
            }

            for(int c=0; c<4; c++){
                counter[matrix[rr-1][c]]++;
            }

            vector<int> ans;
            for(int i=1; i<=16; i++){
                if(counter[i] == 2){
                    ans.push_back(i);
                }
            }

            if(ans.size() >= 2){
                printf("Case #%d: Bad magician!\n", tt+1);
            }else if(ans.size() == 1){
                printf("Case #%d: %d\n", tt+1, ans[0]);
            }else {
                printf("Case #%d: Volunteer cheated!\n", tt+1);
            }

        }

    }








    return 0;
}
