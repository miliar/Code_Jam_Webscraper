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
        int n;
        cin >> n;
        vector <bool> seen (10, 0);
        int c = 0;
        for (int i = 1; i <= 1000; i++){
            string s = to_string (i*n);
            for (int j = 0; j < s.length (); j++){
                if (seen[s[j] - 48])
                    continue;
                seen[s[j] - 48] = 1;
                c++;
            }
            if (c == 10){
                cout << s << "\n";
                break;
            }
        }
        if (c == 10)
            continue;
        cout << "INSOMNIA\n";
    }
}
