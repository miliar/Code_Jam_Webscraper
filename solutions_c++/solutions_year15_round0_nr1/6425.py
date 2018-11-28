/* 
 * File:   main.cpp
 * Author: fryday
 *
 * Created on 11 Апрель 2015 г., 15:43
 */

#include <iostream>
#include <vector>
using namespace std;


int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        int sm;
        cin >> sm;
        int ss = 0;
        int need = 0;
        for (int j = 0; j <= sm; j++)
        {
            char v;
            cin >> v;
            v -= '0';
            if (j == 0)
            {
                ss += v;
            }
            else {
                if (ss < j)
                {
                    need += j - ss;
                    ss = j;
                }
                  ss += v  ;
                
            }
        }
        cout << "Case #"<< i <<": "<<need << endl;
    }
    return 0;
}

