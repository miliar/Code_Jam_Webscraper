#include<iostream>
#include<fstream>
using namespace std;
int maxi(int a, int b) {
    if(a >= b)
        return a;
    return b;
}
int mini(int a, int b) {
    if(a <= b)
        return a;
    return b;
}
int main() {
    int t, kase=1, r, c, x;
    ifstream in;
    ofstream out;
    in.open("D-small-attempt1.in.txt");
    out.open("salidaDchico3.txt");
    bool flag=true;
    in >> t;
    while(t--) {
        in >> x >> r >> c;
        if(x == 1)
            flag = true;
        if(x == 2) {
            if((r * c) %2 == 0)
                flag = true;
            else
                flag = false;
        }
        if(x == 3) {
            if((r * c) % 3 == 0) {
                if(r == 1 || c == 1)
                    flag = false;
                else
                    flag = true;
            }
            else
                flag = false;
        }
        if(x == 4) {
            if((r * c) % 4 == 0) {
                if(r == 1 || c == 1) {
                    flag = false;
                }
                else
                    if(r == 2 || c == 2) {
                        flag = false;
                    }
                    else
                        if(r == 3 || c == 3) {
                            flag = true;
                        }
                        else
                            flag = true;
            }
            else
                flag = false;
        }
        if(flag)
            out << "Case #" << kase << ": " << "GABRIEL" << endl;
        else
            out << "Case #" << kase << ": " << "RICHARD" << endl;
        
        flag = true;
        
            
        kase++;
    }
    in.close();
    out.close();
}
