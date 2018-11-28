#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<set>
#include<map>
#include<string>
#include<sstream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<iomanip>
#include<queue>
#include<stack>

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))

#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define RREPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define RFOR(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define RFOREACH(it,c) for(VAR(it,(c).rbegin());it!=(c).rend();++it)
#define CLEAR(x) memset(x,0,sizeof x);

#define MP make_pair
#define MAPI(t1,t2) map<t1,t2>::iterator
#define RMAPI(t1,t2) map<t1,t2>::reverse_iterator
#define eps 1.0e-11
#define PAUSE system("Pause");
using namespace std;

void out(int i,string s){
    cout<<"Case #"<<i<<s<<endl;
}
int main(){
    int n;
    cin>>n;
    int count=0;
    string xwon=": X won";
    string owon=": O won";
    while(n--){
        count++;
        char ar[4][4];
        bool incomplete=false;
        REP(i,4){
        REP(j,4){
        cin>>ar[i][j];
        if(ar[i][j]=='.') incomplete=true;
        }
        }
        bool xw=false;
        bool ow=false;
        
        for(int i=0;i<4;i++){
            bool xr=true;
            bool xc=true;
            bool orr=true;
            bool oc=true;
            for(int j=0;j<4;j++){
                if(ar[i][j]=='X' || ar[i][j]=='T'){
                    xr&=true;
                }else{
                    xr&=false;
                }
                if(ar[j][i]=='X' || ar[j][i]=='T'){
                    xc&=true;
                }else{
                    xc&=false;
                }
                
                if(ar[i][j]=='O' || ar[i][j]=='T'){
                    orr&=true;
                }else{
                    orr&=false;
                }
                if(ar[j][i]=='O' || ar[j][i]=='T'){
                    oc&=true;
                }else{
                    oc&=false;
                }
            }
            
            if(xr || xc){
                xw=true;
                break;
            }
            if(orr || oc){
                ow=true;
                break;
            }
        }
        bool dx=true;
        bool do0=true;
        
        bool dx1=true;
        bool do1=true;
        
        for(int i=0;i<4;i++){
            if(ar[i][i]=='X' || ar[i][i]=='T'){
                dx&=true;
            }else{
                dx&=false;
            }
            if(ar[i][4-i-1]=='X' || ar[i][4-i-1]=='T'){
                dx1&=true;
            }else{
                dx1&=false;
            }
            if(ar[i][i]=='O' || ar[i][i]=='T'){
                do0&=true;
            }else{
                do0&=false;
            }
            if(ar[i][4-i-1]=='O' || ar[i][4-i-1]=='T'){
                do1&=true;
            }else{
                do1&=false;
            }
        }
        
        if(xw || dx || dx1){
            out(count,xwon); continue;
        }
        if(ow || do0 || do1){
            out(count,owon); continue;            
        }
        if(incomplete){
            out(count,": Game has not completed"); continue;
        }
        out(count,": Draw"); continue;            

        
    }
    
    return 0;
}

