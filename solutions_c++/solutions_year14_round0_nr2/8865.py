#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>

using namespace std;
# define f(i,a,b) for(int i=a;i<b;i++)
# define tt <<"\t"<<
# define Clear(x) memset(x,0,sizeof(x))
# define fill(x,a) memset(x,a,sizeof(x))
# define pb push_back
# define mp make_pair
# define X first
# define Y second
# define inf (~(1<<31))
# define linf (~(1LL<<63LL))
# define sqr(x) ((x)*(x))
# define sz(x) ((int)x.size())

typedef unsigned long long ull;
typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector< vector <int > > vvi;

double C,F,X;
double t1,t2,ans;

double fn(int farms){
    double ret=0;
    double currate=2;
    double temptime=0;
    for(int i=0;i<farms;i++){
        temptime=C/currate;
        ret+=temptime;
        currate=currate+F;
    }
    ret+=X/currate;
    return ret;
}
int main(){
    int t;cin>>t;int tcnt=1;
    while(t--){

        cin>>C>>F>>X;
        int lo=0;int hi=10000000;
        int a,b;
        while(hi-lo>3){
            a=(hi-lo)/3+lo;
            b=2*((hi-lo)/3)+lo;
            t1=fn(a);t2=fn(b);
            if(t1<t2){
                hi=b;
            }
            else{
                lo=a;
            }

        }
        ans=linf;
        for(int i=lo;i<=hi;i++){
            ans=min(ans, fn(i));
        }
        cout<<"Case #"<<tcnt<<": ";
        printf("%.8f\n",ans);
        tcnt++;
    }
    return 0;

}
