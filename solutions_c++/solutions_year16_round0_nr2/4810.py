// =====================================================================================
//
//       Filename:  B.cpp
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
        string s; 
        cin >> s;
        int it = 0;
        for (int i = 1; i < s.length (); i++)
            if (s[i] != s[i-1])
                ++it;
        if (s[s.length ()-1] == '-')
            it++;
        cout << it << "\n";
    }
}
