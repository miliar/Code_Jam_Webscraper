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

double a[1002];
double b[1002];

int main()
{
    cout << setprecision(9) ;
    int T;
    cin >> T;
    for(int caseno=0;caseno<T;caseno++) {
        int n;
        cin >> n;
        for(int i=0;i<n;i++) cin >> a[i];
        for(int i=0;i<n;i++) cin >> b[i];
        sort(a, a+n);
        sort(b, b+n);
        int p1 = 0;
        int p2 = 0;
        int c1 = 0;
        while(p1 < n) {
            if(a[p1] < b[p2]) p1++;
            else {
                p1++;
                p2++;
                c1++;
            }
        }
        p1 = n-1;
        p2 = n-1;
        int c2 = 0;
        while(p1 >= 0) {
            if(a[p1] > b[p2]) {
                c2++;
                p1--;
            } else {
                p1--;
                p2--;
            }
        }
        cout << "Case #" << caseno+1 << ": " << c1 << " " << c2 << endl;
    }
    return 0;
}
