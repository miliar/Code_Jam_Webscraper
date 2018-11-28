#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 

using namespace std; 


#define PI acos(-1)
#define CLEAR(A) memset(A,0,sizeof(A))
#define SETMAX(A) memset(A,0x7f,sizeof(A))
#define SETM1(A) memset(A,-1,sizeof(A))
#define SQ(A) (A)*(A)

int main()
{
    cout << setprecision(9) ;
    int T;
    cin >> T;
    for(int i=1;i<=T;i++) {
        int X, R, C;
        cin >> X >> R >> C;
        if(X==1) {
            cout << "Case #" << i << ": GABRIEL" << endl;
        }
        if(X==2) {
            if((R==1 && C==1) || ((R*C)%2)) {
                cout << "Case #" << i << ": RICHARD" << endl;
            } else {
                cout << "Case #" << i << ": GABRIEL" << endl;
            }
        }
        if(X==3) {
            if((R<=2 && C<=2) || R==1 || C==1 || ((R*C)%3)) {
                cout << "Case #" << i << ": RICHARD" << endl;
            } else {
                cout << "Case #" << i << ": GABRIEL" << endl;
            }

        }
        if(X==4) {
            if((R<=3 && C<=3) || R<=2 || C<=2) {
                cout << "Case #" << i << ": RICHARD" << endl;
            } else {
                cout << "Case #" << i << ": GABRIEL" << endl;
            }
        }
    }
    return 0;
}
