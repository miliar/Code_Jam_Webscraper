#define FROM_FILE
#define TO_FILE

//-Wl,--stack,52800000
#include <ctime>
#include <iostream>
#include <list>
#include <map>
#include <vector>
#include <bitset>
#include <algorithm>
#include <iomanip>
#include <set>
#include <fstream>
#include <cassert>
#include <queue>
#include <stack>
#include <cmath>
#include <cstring>
#include <complex>

using namespace std;

#define foreach(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define MP make_pair
#define PB push_back
#define FF first
#define SS second
#define All(n) (n).begin(), (n).end()

typedef long long int lli;
typedef unsigned long long int ull;
typedef pair<int,int> pii;
typedef pair<lli,lli> pll;
typedef vector<int> vi;

#ifdef FROM_FILE
ifstream fin("in.txt");
#define cin fin
#endif

#ifdef TO_FILE
ofstream fout("out.txt");
#define cout fout
#endif

//const int MAXN=;
//const int MOD=1000*1000*1000 + 7;
//const lli INF=1000000000000000000ll;

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
    {
        long double c,f,x,s=2;
        cin>>c>>f>>x;
        long double t1=0;
        while(1)
        {
            long double t2=t1;
            t2+=c/s;
            t2+=x/(s+f);
            if(t1+x/s<=t2)
                break;
            t1+=c/s;
            s+=f;
        }
        cout<<"Case #"<<z<<": "<<setprecision(10)<<fixed<<t1+x/s<<endl;
    }
    return 0;
}
