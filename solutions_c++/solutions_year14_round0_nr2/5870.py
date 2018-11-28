#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <iomanip>

#define SORT(x) sort(x.begin(),x.end())
#define REVERSE(x) reverse(x.begin(),x.end())
#define mp(x,y) make_pair(x,y)

using namespace std;

typedef unsigned long long ull;
typedef vector<int> VI;
typedef vector<VI> VII;

int main()
{
    ios_base::sync_with_stdio(false);

    int T;
    double C,F,X;
	freopen("cookiesl.in","r",stdin);
	freopen("cookiel.out","w",stdout);

    cin>>T;
    int t=1;
    while(T--){

    cin>>C>>F>>X;

    double res = 0;
    double act = 2;

    while(1){

    double t1 = X/act;
    double t2 = ( C / act )+( X / ( F+act ) );

    if(t2 < t1 ){
    res+=(C/act);
    act+=F;
    }
    else{
    res+=X/act;
    break;
    }

    }
    cout<<"Case #"<<t<<": ";
    cout<<fixed;
    cout<<setprecision(7)<<res<<endl;
    t++;

    }

    return 0;
}
