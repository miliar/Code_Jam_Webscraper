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
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <cstring>
#include <climits>
#include <iostream>
#include <cassert>
#define mod 1000000007
#define eps 1e-4
#define arsize 1000000000
#define INF 0x3f3f3f3f
#define NINF INT_MIN
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define size 1000001
#define fi(i,n) for(int i=0; i<(int)(n); ++i)
#define fii(i,u,n) for(int i=(int)(u); i<(int)(n); ++i)
#define fl(i,n) for(long int i=0; i<(long int)(n); ++i)
#define fli(i,u,n) for(long int i=(long int)(u); i<(long int)(n); ++i)
#define each(it,o) for(aut(it,0.begin()); it!=o.end(); ++it)
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define mset(m,v) memset(m,v,sizeof(m))
#define edge pair<int,int>
typedef long int li;
typedef long long int lli;
using namespace std;
/*ofstream fout ("test.out");
 ifstream fin ("test.in");
 int a, b;
 fin >> a >> b;
 fout << a+b << endl;*/
bool num[10];
void innum(long int x,bool num[])
{
    while(x)
    {
        long int t=x%10;
        x/=10;
        num[t]=1;
    }
}
bool isfoundall(bool num[])
{
    for(int i=0;i<10;++i)
        if(!num[i]) return 0;
    return 1;
}
int main()
{
    ifstream fin("/Users/priya/Desktop/A-large.in");
    ofstream fout("/Users/priya/Desktop/A-large.out");
    long int t; fin>>t;
    for(long int i=1;i<=t;++i)
    {
        long int n; fin>>n; memset(num,0,sizeof(num));
        if(n==0) fout<<"Case #"<<i<<":"<<" "<<"INSOMNIA"<<endl;
        else
        {
            long int temp=n;
        innum(n,num);
            bool f=1;
            while(f)
            {
                if(isfoundall(num)) f=0;
                else
                {
                    n+=temp;
                    innum(n,num);
                }
            }
            fout<<"Case #"<<i<<":"<<" "<<n<<endl;
        }
    }
    return 0;
}