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
#define EPS 1e-12
#define EXP 1e7


int main(){
	int T;
	cin>>T;
	for(int x=1;x<=T;x++){
		int X,R,C;
        cin>>X>>R>>C;
        if(R > C) swap(R,C);
        string gab="GABRIEL",ric="RICHARD";
        string ans;
        if(X==1){
            ans = gab;
        }else if(X==2){
            if((R*C)%2)
                ans = ric;
            else
                ans = gab;
        }else if(X==3){ //3 2 4  -- 3  3  3
            if((R*C)%3)
                ans = ric;
            else{
                if(R == 1)
                    ans = ric;
                else if(R == 2)
                    ans = gab;
                else{
                    ans = gab;
                }
            }
        }else{
            if((R*C)%4)
                ans = ric;
            else{
                if(R<=2)    ans = ric;
                else    ans = gab;
            }
        }
		
		cout<<"Case #"<<x<<": ";
		cout<<ans<<endl;
		}
	return 0;
	}
	
