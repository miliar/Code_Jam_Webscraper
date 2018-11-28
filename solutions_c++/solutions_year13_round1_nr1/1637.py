#include <iostream>

using namespace std;

int main(int argc, char** argv) {
    int cases;
    cin >> cases;
    
    for (int i = 1; i <= cases; i++) {
        unsigned long long r = 0, t = 0;
        cin >> r;
        cin >> t;
        
        unsigned long long remain = t;
        unsigned long long ir, orr;
        unsigned long long n;
        for(n = 1; remain > 0;) {
            unsigned long long area = 0;
            orr = r + (n * 2 -1);
            ir = r + (n -1) * 2;
            
//            cout << "next ring"<<endl;
            if(remain < orr) {
                break;
            }
            area = (orr * orr ) - (ir * ir);
            
//            cout <<"area: " <<area << " n:" << n <<endl;
            if(remain < area) {
                break;
            }
            
            n++;
            remain -=area;
//            cout << "remain " << remain <<endl;
        }
        
        cout << "Case #" << i<<": " << n  - 1 <<endl;
    }
}