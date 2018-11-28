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
    cout << setprecision(11) ;
    int T;
    cin >> T;
    for(int caseno=0;caseno<T;caseno++) {
        double C, F, X;
        cin >> C >> F >> X;
        int n = X/C - 2/F;
        double ret = 0;
        for (int i=0; i < n; i++) {
            ret += C/(i*F+2);    
        }
        if (n<0) n=0;
        ret += X/(n*F+2);
        cout << "Case #" << caseno+1 << ": " << ret << endl;
    }
    return 0;
}
