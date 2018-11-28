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

int main(){
    int t;cin>>t;int tcnt=1;
    while(t--){
        int rn,temp;
        vi v1,v2;
        cin>>rn;
        f(i,0,4){
            f(j,0,4){
                cin>>temp;
                if(i+1==rn)v1.pb(temp);
            }
        }
        cin>>rn;
        f(i,0,4){
            f(j,0,4){
                cin>>temp;
                if(i+1==rn)v2.pb(temp);
            }
        }
        sort(v1.begin(),v1.end());sort(v2.begin(),v2.end());
        int ans=-1, cnt=0;
        f(i,0,sz(v1)){
            f(j,0,sz(v2)){
                if(v1[i]==v2[j]){
                    cnt++;ans=v1[i];
                }
            }
        }
        cout<<"Case #"<<tcnt<<": ";
        tcnt++;
        if(cnt==1){
            cout<<ans<<endl;
        }
        if(cnt==0){
            cout<<"Volunteer cheated!"<<endl;
        }
        if(cnt>1){
            cout<<"Bad magician!"<<endl;
        }

    }
    cin>>t;
    return 0;

}
