
#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vI;
typedef vector<string> vS;
typedef pair<int, int> pI;
typedef map<int, int> mI;
typedef map<string, int> mSI;
typedef set<int> sI;
typedef set<pI> spI;
typedef priority_queue<int> qmax;
typedef priority_queue<int, vector<int>, greater<int> >qmin;
typedef map<int, int>::iterator mI_it;
typedef set<int>::iterator sI_it;

#define TWO(k)  (1<<(k))
#define LTWO(k) (((LL)(1)<<(k)))
#define MIN(a,b) ( (a)<(b)?(a):(b) )
#define MAX(a,b) ( (a)>(b)?(a):(b) )
#define LS(x) 	 ((x)<<1)
#define RS(x) 	 (((x)<<1)+1)
#define MP make_pair
#define PB push_back
#define F0(i, n) for( int (i) = 0; (i) < (n); (i)++)
#define F1(i, n) for( int (i) = 1; (i) <= (n); (i)++)
#define zero(i) memset((i),0,sizeof((i)))

int digit;
bool s[10];

bool help(int x){
    int n = x; 
    while(n > 0){
        if(s[n%10] == false){
            digit--;
            if(digit == 0) return true;
            s[n%10] = true;
        }
        n /= 10;
    }
    return false;
}


int main()
{
    //freopen("out.txt","w",stdout);
    //freopen("in.txt","r",stdin);
    int t;
    cin>>t;
    int x = 0;
    while(t--){
        x++;
        int n;
        cin>>n;
        if(n == 0) cout<<"Case #"<<x<<": "<<"INSOMNIA"<<endl;
        else{
            memset(s, 0, sizeof(s));
            digit = 10;
            int p = 1;
            while(true){
                //cout<<"p*n="<<p*n<<endl;
                if(help(p * n) == true){
                    cout<<"Case #"<<x<<": "<<p*n<<endl;
                    break;
                }
                p++;
            }
        }
    }
    return 0;
}
