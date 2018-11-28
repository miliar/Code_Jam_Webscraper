#include <iostream>
#include <fstream>
#include <string>

//#define ifname "A-small-attempt1.in"
//#define ofname "A-small-attempt1.out"

#define ifname "A-large.in"
#define ofname "A-large.out"

using namespace std;

int main()
{
    int T,test_case,S,i,stand,friends;
    string A;
    
    ifstream is;
    ofstream os;
    is.open(ifname);
    os.open(ofname);
    
    is  >> T;
    for(test_case = 1; test_case <= T; ++test_case) {
        is >> S >> A;
        
        friends = 0;
        stand = (A[0] - '0');
        for(i = 1; i<= S; ++i) {
            if (stand < i) {
                friends += (i - stand);
                stand += (i - stand);
            }
            stand += (A[i] - '0');
        }        
        
        os << "Case #" << test_case << ": ";
        os << friends << endl;
    }

    is.close();
    os.close();
   
    return 0;
}
