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

const int MAXN=1000 + 10;
//const int MOD=1000*1000*1000 + 7;
//const lli INF=1000000000000000000ll;

double a[MAXN];
double b[MAXN];
int n;
int s1(deque<double> d)
{
    int ans=0;
    for(int i=n-1;i>=0;i--)
    {
        if(a[i]>d.back()){
            d.pop_front();
            ans++;
        }
        else
            d.pop_back();
    }
    return ans;
}

int s2(deque<double> d)
{
    int ans=0;
    for(int i=0;i<n;i++)
    {
        if(a[i]>d.front())
        {
            d.pop_front();
            ans++;
        }
        else
            d.pop_back();
    }
    return ans;
}

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
    {
        cout<<"Case #"<<z<<": ";
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>a[i];
        sort(a,a+n);
        for(int i=0;i<n;i++)
            cin>>b[i];
        sort(b,b+n);
        deque<double> d(b,b+n);
        cout<<s2(d)<<' '<<s1(d)<<endl;
    }
    return 0;
}
