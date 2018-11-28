#include <iostream>
#include <vector>
#include <cmath>
#include <cstring>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    ifstream in("input.in");
    ofstream out("output.out");
    int T;
    in >> T;
    for(int t = 1; t <= T; t++) {
        int x, r, c;
        in >> x >> r >> c;
        string ans;
        if(x == 1)
            ans = "GABRIEL";
        else if(x == 2){
            if(r*c% 2 == 0){
                ans = "GABRIEL";
            }
            else {
                ans = "RICHARD";
            }
        }
        else if(x == 3){
            if(r*c % 3 == 0){
                if(min(r, c) == 1){
                    ans = "RICHARD";
                }
                else ans = "GABRIEL";
            }
            else ans = "RICHARD";
        }
        else if(x == 4){
            if(r*c%4 == 0){
                if(min(r, c) == 1){
                    ans = "RICHARD";
                }
                else if(min(r,c) == 2){
                    ans = "RICHARD";
                }
                else if(min(r,c) == 3){
                    ans = "GABRIEL";
                }
                else ans = "GABRIEL";
            }
            else ans = "RICHARD";
        }
        out << "Case #" << t << ": " << ans << "\n";
    }
    return 0;
}
