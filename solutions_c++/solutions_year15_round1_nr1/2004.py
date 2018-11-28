#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <ctime>

#define CC(x) cout << (x) << endl
#define PB(x) push_back(x)
#define fp(i,f,t) for(int i=f; i<t; i++)
#define fm(i,f,t) for(int i=f; i>t; i--)
#define MP(x,y) make_pair(x,y)
using namespace std;

int main(){
    long t=0;
    cin >> t;
    for(int _case=1; _case<=t; _case++){
        long m[1000];
        long n, ans1=0, ans2=0, bigdiff=0;
        cin >> n;
        for(long i=0; i<n; i++){
            cin >> m[i];
            if(i==0) continue;
            if(m[i]<m[i-1]){
                ans1+=m[i-1]-m[i];
                bigdiff = max(bigdiff, m[i-1]-m[i]);
            }
        }
        long cm = 0;
        for(long i=0; i<n-1; i++){
            if(m[i] > bigdiff){
                ans2+=bigdiff;
            }
            else{
                ans2+=m[i];
            }
        }
        cout << "Case #"<< _case <<": " << ans1 << " " << ans2 << endl;;
    }
    return 0;
}
