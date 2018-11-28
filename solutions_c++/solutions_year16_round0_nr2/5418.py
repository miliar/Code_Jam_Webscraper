
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


int main()
{
    freopen("out.txt","w",stdout);
    freopen("in.txt","r",stdin);
    int t;
    cin>>t;
    for(int i = 1; i <= t; i++){
        string s;
        cin>>s;
        int res = 0;
        if(s.length() == 1){
            if(s[0] == '+') cout<<"Case #"<<i<<": "<<res<<endl;
            else cout<<"Case #"<<i<<": "<<res+1<<endl;
        }
        else{
            for(int j = 0; j < s.length()-1; j++){
                if(s[j] != s[j+1]) res++;
            }
            if(s[s.length()-1] == '-') res++;
            cout<<"Case #"<<i<<": "<<res<<endl;
        }
    }
    return 0;
}
