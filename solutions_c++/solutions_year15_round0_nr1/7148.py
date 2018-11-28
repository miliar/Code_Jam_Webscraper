//
//  ovation.cpp
//  Google
//

#include <iostream>
#include <iterator>
#include <queue>
#include <cmath>
#include <sstream>
#include <vector>

using namespace std;


int main()
{
    string in;
    int tstCase, maxS;
    
    cin >> tstCase;
    int people = 0, needed = 0;
    
    int t = 1;
    while(t <= tstCase){
        needed = people = 0;
        cin >> maxS >> in;
        int num;
        for (int i = 0; i < in.size(); i++) {
            num = in[i] - '0';
            
            if(people >= i && num != 0) {
                people += num;
            }else if (num != 0){
                needed += i-people;
                people += i-people + num;
            }
        }
        cout << "Case #" << t << ": " << needed << endl;
        t++;
    }
    return 0;
}


