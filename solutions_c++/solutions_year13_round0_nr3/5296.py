#include <iostream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    int t;
    cin >> t;
    
    int i = 0;
    
    while(t--) {
        i++;
        
        int a, b, c = 0;
        cin >> a >> b;
        
        for (int j = a; j <= b; j++) {
            ostringstream os; 
            os << j;
            string s = os.str();
            bool p = true;
            
            for (int k = 0; k < s.length() / 2; k++) {
                if (s.at(k) not_eq s.at(s.length() - k - 1)) {
                    p = false;
                    break;
                }
            }
            
            if (p and sqrt(j) == floor(sqrt(j))) {
                int l = sqrt(j);
                os.str("");
                os << l;
                s = os.str();
                
                for (int k = 0; k < s.length() / 2; k++) {
                    if (s.at(k) not_eq s.at(s.length() - k - 1)) {
                        p = false;
                        break;
                    }
                }
                
                if (p)
                    c++;
            }
        }
        
        cout  << "Case #" << i << ": " << c;
            
        cout << endl;
    }
    
    return 0;
}