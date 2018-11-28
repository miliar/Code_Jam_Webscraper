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
    int T , S, ans , stand ,needed;
    cin >> T;
    int x,c =0;
    char arr[1005];
    for (int i=1; i<=T; i++){
        c =0;
        ans =0;
        stand =0;
        cin >> S;
        int f=S;
        cin >> arr;
        int diff =0;
        for (int j=0; j<=f; j++){
            needed=j;
            diff =0;
            if (j>stand && (arr[j]-'0')!=0){
                diff =(j-stand);
                ans+=diff;
            }
            stand += (arr[j]-'0');
            stand += diff;
        }

        cout << "Case #" << i<< ": " << ans << endl;
    }
    return 0;
}
