//
//  a.cpp
//  CodeJam
//
//  Created by 귤이 on 2016. 5. 8..
//  Copyright © 2016년 귤이. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    int T, N;
    int P[26];
    int total = 0;
    
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N;
		total = 0;
        for (int n = 0; n < N; n++) {
            cin >> P[n];
            total += P[n];
        }
        
        int maxi = 0;
        int max = 0;
        int first = 0;
        cout << "Case #" << t << ": ";
        while (total > 0) {
            maxi = 0;
            max = 0;
            for (int i = 0; i < N; i++) {
                if (max < P[i]) {
                    maxi = i;
                    max = P[i];
                }
            }
            
            
            cout << " " << (char)('A' + maxi);
            P[maxi]--;
            total--;
            if (total == 2) continue;
            
            maxi = 0;
            max = 0;
            for (int i = 0; i < N; i++) {
                if (max < P[i]) {
                    maxi = i;
                    max = P[i];
                }
            }
            cout << (char)('A' + maxi);
            P[maxi]--;
            total--;
        }
		cout << endl;
        
    }
}
