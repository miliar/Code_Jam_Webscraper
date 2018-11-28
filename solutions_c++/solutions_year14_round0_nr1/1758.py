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
    for (int caseno=0;caseno<T;caseno++) {
        int rownum;
        cin >> rownum;
        int a,b,c,d;
        int e,f,g,h;
        for(int i=0;i<4;i++) {
            int a1,b1,c1,d1;
            cin >> a1 >> b1 >> c1 >> d1;
            if (i+1 == rownum) {
                a = a1;
                b = b1;
                c = c1;
                d = d1;
            }
        }
        cin >> rownum;
        for(int i=0;i<4;i++) {
            int a1,b1,c1,d1;
            cin >> a1 >> b1 >> c1 >> d1;
            if (i+1 == rownum) {
                e = a1;
                f = b1;
                g = c1;
                h = d1;
            }
        }
        
        int num = -1;
        int cnt = 0;
        if (a == e || a == f || a == g || a == h) {
            cnt++;
            num = a;
        }
        if (b == e || b == f || b == g || b == h) {
            cnt++;
            num = b;
        }
        if (c == e || c == f || c == g || c == h) {
            cnt++;
            num = c;
        }
        if (d == e || d == f || d == g || d == h) {
            cnt++;
            num = d;
        }
        
        if(cnt == 0) {
            cout << "Case #" << caseno+1 << ": Volunteer cheated!" << endl;
        } else if (cnt == 1) {
            cout << "Case #" << caseno+1 << ": " << num << endl;
        } else {
            cout << "Case #" << caseno+1 << ": Bad magician!" << endl;
        }
    }

    return 0;
}
