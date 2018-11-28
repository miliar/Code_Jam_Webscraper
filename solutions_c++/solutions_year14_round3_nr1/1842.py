//                                                  به نام خداوند بخشنده ی مهربان
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <fstream>
#include <complex>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <deque>
#include <cmath>
#include <map>
#include <set>

# define xx first
# define yy second
# define pb push_back
# define pp pop_back
# define eps 1e-9
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vint;

int main(){
    ios_base::sync_with_stdio(false);
    freopen("ops.in","r",stdin);
    freopen("ans.out","w",stdout);
    int q;cin>>q;
    for(int t=1 ; t<=q ; t++){
        string  s;cin>>s;
        cout<<"Case #"<<t<<": ";
        ll x,y;x=y=0;
        int pos=0;
        while(s[pos]!='/'){
            x*=10;
            x+=s[pos]-'0';
            pos++;
        }
        pos++;
        while(pos<(int)s.size()){
            y*=10;
            y+=s[pos]-'0';
            pos++;
        }
        int gg=__gcd(x,y);
        x/=(int)gg;y/=(int)gg;
        int age=0;
        bool mark=false,flag=false;
        while(y!=x){
            while(y>x && y%2==0){
                y/=2;
                if(!mark)age++;
            }
            mark=true;
            if(y>x){
                cout<<"impossible\n";
                flag=true;
                break;
            }
            else if(x==y)
                break;
            else
                x-=y;
        }
        if(!flag)
            cout<<age<<endl;
    }
    return 0;
}
