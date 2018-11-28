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
    ll n1, n2;
    while(t--){
        t2++;
        cin>>n1;
        bool digits[10];
        REP(i, 0, 9)digits[i] = false;
        int cnt = 0;

        if(n1 == 0)cnt = 11;

        n2 = n1;
        while(cnt < 10){
            string s = to_string(n2);
            REP(i, 0, s.length()-1){
                if(!digits[s[i]-'0']){
                    digits[s[i]-'0'] = true;
                    cnt++;
                }
            }
            n2 += n1;
        }

        cout << "Case #" << t2 << ": ";
        if(cnt == 10){
            cout << n2 - n1 << endl;
        }
        else
            cout << "INSOMNIA" << endl;
    }
    return 0;
}