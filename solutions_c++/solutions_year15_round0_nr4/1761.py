#include <iostream>
#include <fstream>
#include <string>

#define ifname "D-small-attempt1.in"
#define ofname "D-small-attempt1.out"

using namespace std;

int main()
{
    int T,test_case,X,R,C,temp;
    bool Gwin;
    
    ifstream is;
    ofstream os;
    is.open(ifname);
    os.open(ofname);
    
    is  >> T;
    for(test_case = 1; test_case <= T; ++test_case) {
        is >> X >> R >> C;
        
        if ( R > C ) {
            temp = R;
            R = C;
            C = temp;
        }
        
        if  ( X > 6 )
            Gwin = false;

        else if  ( C < X )
            Gwin = false;
            
        else if ( (R*C) < X )
            Gwin = false;
                        
        else if  ( (R*C) % X != 0 )
            Gwin = false;
            
        else {
            switch (X) {
                case 1:
                case 2:
                    Gwin = true;
                    break;
                    
                case 3:
                    if (R < 2) Gwin = false;
                    else Gwin = true;
                    break;
                    
                case 4:
                    if (R < 3) Gwin = false;
                    else Gwin = true;
                    break;
                    
                case 5:
                    if (R < 4) Gwin = false;
                    else Gwin = true;
                    break;
                    
                case 6:
                    if (R < 4) Gwin = false;
                    else Gwin = true;
                    break;
                    
                default:
                    Gwin = false;
            }
        }
        
        
        os << "Case #" << test_case << ": ";
        if (Gwin)
            os << "GABRIEL" << endl;
        else
            os << "RICHARD" << endl;
        
    }

    is.close();
    os.close();
    return 0;
}
