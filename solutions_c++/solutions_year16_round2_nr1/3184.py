
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

bool m[2009];
string s;
string c[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
vector<int> res;

void mark(int x){
    res.push_back(x);
    for(int j = 0; j < c[x].length(); j++){
        for(int i = 0; i < s.length(); i++){
            if(s[i] == c[x][j] && m[i] == false){
                m[i] = true;
                break;
            }
        }
    }
}

int main()
{
    freopen("out.txt","w",stdout);
    freopen("in.txt","r",stdin);
    int t;
    cin>>t;
    for(int k = 1; k <= t; k++){
        cin>>s;
        int l = s.length();
        memset(m, 0, sizeof(m));
        res.clear();
        for(int i = 0; i < l; i++){
            if(m[i] != true){
                if(s[i] == 'Z') mark(0); 
                else if(s[i] == 'W') mark(2);
                else if(s[i] == 'U') mark(4);
                else if(s[i] == 'X') mark(6);
                else if(s[i] == 'G') mark(8);
            }
        }
        
        for(int i = 0; i < l; i++){
            if(m[i] != true){
                if(s[i] == 'F') mark(5);
                else if(s[i] == 'H') mark(3);
                else if(s[i] == 'S') mark(7);
            }
        }

        for(int i = 0; i < l; i++){
            if(m[i] != true){
                if(s[i] == 'O') mark(1);
                else if(s[i] == 'I') mark(9);
            }
        }
//        for(int i = 0; i < res.size(); i++) cout<<res[i]<<endl; 
        sort(res.begin(), res.begin()+res.size());
//        for(int i = 0; i < res.size(); i++) cout<<res[i]<<endl; 
        string ans = "";
        for(int i = 0; i < res.size(); i++){
            ans += res[i] + '0';
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}
