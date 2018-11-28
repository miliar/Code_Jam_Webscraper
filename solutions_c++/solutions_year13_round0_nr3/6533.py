#include <iostream>
#include <sstream>
#include <math.h>

using namespace std;

int t;
int res[1000];

bool is_pal (int a) {

    stringstream ss;
    stringstream ss2;
    ss << a;
    bool f = true;
    bool f2 = true;
    string s = ss.str ();
    
 //   cout << endl << endl << a << endl;
    
    for (int i=0; i<s.length()/2; i++) {
//        cout << s[i] << " " << s[s.length()-i-1] << endl;
        if (s[i] != s[s.length()-i-1])
            f = false;
    }
    
    if (!f) return false;
            
    ss2 << sqrt(a);
    s = ss2.str ();
            
    if (f) {
        for (int i=0; i<s.length()/2; i++)
            if (s[i] != s[s.length()-i-1])
                f2 = false;
    }
            
    return f2;
}

int calc (int a, int b) {
    
    int s = 0;
    for (int i=a; i<=b; i++) {
        
        if (res[i-1] == 1) s++;
        else if (res[i-1] == 0) {
            
            if (pow (round(sqrt(i)), 2) != i) res[i-1] = -1;
            else {
                if (is_pal(i)) {
       //             cout << i << " ";
                    res[i-1] = 1;
                    s++;
                } else res[i-1] = -1;
            }
        
        }
    }
    
    return s;
    
}

int main () {

    cin >> t;
    
    for (int i=0; i<t; i++) {
        int a, b;
        cin >> a >> b;
  //      cout << a << endl;
        cout << "Case #" << i+1 << ": " << calc (a, b) << endl;
    }
}
