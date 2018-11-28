#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
 
using namespace std;
 
#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair
typedef long long ll;

string getVal(char a, char b){
    string c;
    if(a == '1'){
        c.pb(b);
    }else if(a == 'i'){
        if(b == '1')    c = "i";
        else if(b == 'i')   c = "-1";
        else if(b == 'j')   c = "k";
        else    c = "-j";
    }else if(a == 'j'){
        if(b == '1')    c = "j";
        else if(b == 'i')   c = "-k";
        else if(b == 'j')   c = "-1";
        else    c = "i";
    }else{
        if(b == '1')    c = "k";
        else if(b == 'i')   c = "j";
        else if(b == 'j')   c = "-i";
        else    c = "-1";
    }
    return c;
}

int main(){
	int T;
	cin>>T;
   
	for(int x=1;x<=T;x++){
		int L,X;
        cin>>L>>X;
        string s,t;
        cin>>s;
        t = s;
        REP(i,X-1) s+=t;
        //cout<<s<<endl;
        vector<string> dp(s.sz);
        dp[0] = s[0];
        REPEAT(i,1,s.sz){
            bool prevSignNeg=false;//,currSignNeg=false;
            char a,b;
            if(dp[i-1][0] == '-')  {
                prevSignNeg = true;
                a = dp[i-1][1];
            }else{
                a = dp[i-1][0];
            }
            b = s[i];
            string cal;            
            cal = getVal(a,b);
            //cout<<"a:"<<a<<" b:"<<b<<" c:"<<cal<<endl;
            if(cal.sz == 2){
                if(prevSignNeg){
                    if(cal[1] == '1')   dp[i].pb('1');
                    else    dp[i].pb(cal[1]);
                } 
                else{
                    dp[i].pb('-');
                    if(cal[1] == '1')   dp[i].pb('1');
                    else    dp[i].pb(cal[1]);
                }
            }else{
                if(!prevSignNeg){
                   if(cal[0] == '1')   dp[i].pb('1');
                   else    dp[i].pb(cal[0]);
                } 
                else{
                    dp[i].pb('-');
                    if(cal[0] == '1')   dp[i].pb('1');
                    else    dp[i].pb(cal[0]);
                }
            }
            //cout<<"a:"<<a<<" b:"<<b<<" c:"<<cal<<" dp:"<<dp[i]<<endl;
        }
        cout<<"Case #"<<x<<": ";
        if(s.sz < 3){
            cout<<"NO"<<endl;
        }
        else if(s.sz == 3){
            if(s == "ijk")  cout<<"YES"<<endl;
            else cout<<"NO"<<endl;
        }
        else if(dp[dp.sz-1] != "-1"){
            cout<<"NO"<<endl;
        }
        else{
            bool found = false;
            REP(i,dp.sz){
                //cout<<i+1<<" "<<dp[i]<<endl;
                if(dp[i] == "i"){
                    REPEAT(j,(i+1),dp.sz){
                        if(dp[j] == "k"){
                            cout<<"YES"<<endl;
                            found = true;
                            break;
                        }
                    }
                if(found) break;
                }
            }
            if(!found)
            cout<<"NO"<<endl;
        }
        //cout<<"---------------------------------------"<<endl;
	}
	return 0;
}
	
