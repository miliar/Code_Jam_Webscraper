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


int a[10002];

int main()
{
    cout << setprecision(12) ;
    int T;
    cin >> T;
    for(int caseno=1;caseno<=T;caseno++) {
        int N,X;
        cin >> N >> X;
        for(int i=0;i<N;i++) cin >> a[i];
        sort(a, a+N);
        int c = 0;
        int first = 0;
        int last = N-1;
        while(first <= last) {
            if(first != last) {
                if(a[first] + a[last] <= X) {
                    c++;
                    first++;
                    last--;
                } else {
                    c++;
                    last--;
                }
            } else {
                c++;
                first++;
            }
        }
        cout << "Case #" << caseno << ": " << c << endl;
    }
    return 0;
}
