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
    int t, t2 = 0;
    cin>>t;
    while(t--){
        t2++;
        string s;
        cin>>s;
        int n = s.length();

        int total = 0, last = n-1;

        while(true){
            int find = -1;
            REP(i, 0, last){
                if(s[i] == '-'){
                    find = i;
                }
            }
            if(find == -1)break;

            REP(i, 0, find){
                if(s[i] == '-')s[i] = '+';
                else s[i] = '-';
                last = find-1;
            }
            total++;
        }

        cout << "Case #" << t2 << ": ";
        cout << total << endl;
    }
    return 0;
}