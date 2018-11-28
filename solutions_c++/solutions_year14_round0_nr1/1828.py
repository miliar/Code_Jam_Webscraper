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
int a[4][4];
map<int,int> m;
void rd(){
    int x;
    cin>>x;
    x--;
    for(int i=0;i<4;i++)for(int j=0;j<4;j++)cin>>a[i][j];
    for(int i=0;i<4;i++)m[a[x][i]]++;
}

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
    {
        m.clear();
        rd();rd();
        cout<<"Case #"<<i<<": ";
        if(m.size()>7)
            cout<<"Volunteer cheated!";
        else if(m.size()<7)
            cout<<"Bad magician!";
        else
        {
            foreach(j,m)if(j->SS>1){cout<<j->FF;break;}
        }
        cout<<endl;
    }
    return 0;
}
