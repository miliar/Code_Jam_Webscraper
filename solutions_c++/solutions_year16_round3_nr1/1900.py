#include<bits/stdc++.h>
using namespace std;
//custom
#define endl ('\n')
#define space (" ")
#define __ ios_base::sync_with_stdio(false);cin.tie(0);
//utils
#define SET(a,b) (memset(a,b,sizeof(a)))
//for vectors
#define pb push_back
#define mp make_pair
typedef vector<int> vi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;
//data types
typedef long long ll;
//loops
#define REP(i,a,b) \
    for(int i = int(a);i <= int(b);i++)
#define MEMSET_INF 127 //2bill
#define MEMSET_HALF_INF 63 //1bill

#ifdef DEBUG
    #define debug(args...) {dbg,args; cerr<<endl;}
    #define _
#else
    #define debug(args...)  // Just strip off all debug tokens
    #define _ ios_base::sync_with_stdio(false);cin.tie(0);
#endif 
struct debugger
{
    template<typename T> debugger& operator , (const T& v)
    {    
        cerr<<v<<" ";    
        return *this;    
    }
} dbg;

int main(){
    _
    int t, t1, n;
    cin>>t;
    t1 = 1;
    while(t--){
        cin>>n;
        int A[n+1];
        set<ii> B;
        REP(i, 1, n){
            cin>>A[i];
            B.insert({-A[i], i});
        }

        cout << "Case #" << t1 << ": ";
        // Remove all extras
        bool all_same = false;
        while(!all_same){
            if(B.size() == 0)break;
            auto it1 = B.begin();
            auto it2 = B.rbegin();
            // debug("*it1, *it2: ", *it1, *it2);
            if(it1->first == it2->first)break;
            ii dec = *it1;
            B.erase(it1);
            cout << char('A' + dec.second - 1) << space;
            
            dec.first += 1;
            if(dec.first)
                B.insert(dec);
        }

        // Check if odd values 
        if(B.size() >= 3 && B.size()%2 == 1){
            // Odd no of values >= 3 remaining
            auto it1 = B.begin();
            ii dec = *it1;
            B.erase(it1);
            while(dec.first++){
                cout << char('A' + dec.second - 1) << space;
            }
        }

        // Check even values
        while(B.size() >= 2 && B.size()%2 == 0){
            // Pair up two highest values and remove them.
            auto it1 = B.begin();
            auto it2 = it1++;
            // debug(it1->first, it1->second, it2->first, it2->second);
            ii dec1 = *it1;
            ii dec2 = *it2;
            B.erase(it1);B.erase(it2);
            while(dec1.first++ && dec2.first++){
                cout << char('A' + dec1.second - 1);
                cout << char('A' + dec2.second - 1) << space;
            }
        }

        if(B.size() == 1){
            auto it1 = B.begin();
            ii dec = *it1;
            B.erase(it1);
            while(dec.first++){
                cout << char('A' + dec.second - 1) << space;
            }
        }
        cout << endl;

        if(B.size())cout << "Wrong answer: " << B.size() << endl;
        t1++;
    }
    return 0;
}