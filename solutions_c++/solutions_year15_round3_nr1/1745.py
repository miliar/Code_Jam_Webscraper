#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <utility>
#include <set>
#include <math.h>
#include <bitset>
const int MaxN = int (1e5);
using namespace std;

int main()
{
     freopen( "in.txt" , "r" , stdin);
    freopen( "out.txt" , "w" , stdout);
    int T , C, R,W;
    int ans =0 , temp =0;
    cin >> T;
    for (int i=1; i<=T; i++){
        cin >> R >> C >> W;
        if (W==1){
            ans = R*C;
        }
        else if (W == C){
            ans = W;
        }
        else if (W == R){
            ans = R;
        }
        else {
            temp = (C/W);
            if (((temp*W) < C) ){
                ans = temp + 1 + (W-1);
            }
            else {
                ans = temp + (W-1);
            }
        }
        cout << "Case #" << i<< ": " << ans << endl;
    }


}
