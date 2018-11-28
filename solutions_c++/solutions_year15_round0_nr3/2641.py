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

int state[8][3] = {{2,4,6}, {3,5,7}, {1,6,5}, {0,7,4}, {7,1,2}, {6,0,3}, {4,3,1}, {5,2,0}} ;

int main()
{
    cout << setprecision(9) ;
    int T;
    cin >> T;
    for(int i=1;i<=T;i++) {
        int L,X;
        cin >> L >> X;
        string s;
        cin >> s;
        string total;
        for(int j=0;j<X;j++) total += s;

        
        int initialState = 0;
        bool reachedTwo = false;
        bool reachedSix = false;
        for(int j=0;j<L*X;j++) {
            int newState = state[initialState][total[j]-'i'];
            if(newState == 2) {
                reachedTwo = true;
            }
            if(newState == 6 && reachedTwo) {
                reachedSix = true;
            }
            initialState = newState;
        }
        if(initialState == 1 && reachedSix) {
            cout << "Case #" << i << ": " << "YES" << endl;
        } else {
            cout << "Case #" << i << ": " << "NO" << endl;
        }
    }
    return 0;
}
