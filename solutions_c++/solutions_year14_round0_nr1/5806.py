#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  
    int T;
    
    cin >> T;
    
    
    for (int _i = 0 ; _i < T; _i++){
        
        int x,y,t;
        
        vector<int> g1;
        vector<int> g2;
        
        cin >> x;
        
        for (int i = 0 ; i < 4 ; i++) {
            for (int j = 0 ; j < 4 ; j++) {
                cin >> t;
                if (i == x-1) {
                    g1.push_back(t);
                }
            }
        }
        
        cin >> y;
        
        for (int i = 0 ; i < 4 ; i++) {
            for (int j = 0 ; j < 4 ; j++) {
                cin >> t;
                if (i == y-1) {
                    g2.push_back(t);
                }
            }
        }
        
        vector<int> r;

        
        for (int i = 0 ; i < 4 ; i++) {
            for (int j = 0 ; j < 4 ; j++) {
                if (g1[i]==g2[j])
                    r.push_back(g1[i]);
            }
        }
        
        cout << "Case #" << _i+1 << ": ";
        
        if (r.size() == 0)
            cout << "Volunteer cheated!" << endl;
        else if (r.size() == 1)
            cout << r[0] << endl;
        else
            cout << "Bad magician!" << endl;
        
        
    }
    
    return 0;
}

