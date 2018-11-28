// =====================================================================================
//
//       Filename:  A.cpp
//         Author:  Reyno Tilikaynen, r.tilikaynen@gmail.com
//   Organization:  University of Waterloo
//
// =====================================================================================

#include <bits/stdc++.h>

using namespace std; 

int main (){ 
    int tt; 
    cin >> tt; 
    for (int cases = 1; cases <= tt; cases++){
        printf ("Case #%d: ", cases);
        int k, c, s; 
        cin >> k >> c >> s; 
        for (int i = 1; i <= s; i++)
            cout << i << " ";
        cout << "\n";
    }
}
