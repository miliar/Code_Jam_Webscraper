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
        string w = "";
        string s; 
        cin >> s; 
        w = w + s[0];
        for (int i = 1; i < s.length (); i++){
            if (s[i] + w < w + s[i])
                w = w + s[i];
            else
                w = s[i] + w;
        }
        cout << w << "\n";
    }
}
