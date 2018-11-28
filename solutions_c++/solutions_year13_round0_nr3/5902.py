#include <cstring>
#include <string>
#include <string.h>
#include <map>
#include <deque>
#include <iterator>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <list>

using namespace std;

#define FST first
#define SND second
#define MP make_pair
#define PB push_back

typedef long long LL;
typedef long double LD;

typedef stringstream SS;
typedef pair<long,int> PLI;
typedef pair<int ,int> PII;
typedef vector<PLI> VPLI;
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<string> VVS;
typedef vector<double> VD;

#define ALL(x) (x).begin(),(x).end()
#define FOR1(i,n) for(int i=0;i<(n);i++)
#define FOR2(i,n,m)for(int i=n;i<=(m);++i)
#define FORD(i,n,m) for(int i=n;i>=(int)(m);--i)
#define FORI(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define SIZE(a) ((int)((a).size()))
#include <iostream>
#include <cmath>

string toString(long double n)
{
    SS s;
    s<<fixed<<setprecision(0)<<n;
    return s.str();
}


long double isSquare(long double a)
{
     cout<<fixed<<setprecision(4);
	long double x0, x1;
	string s;
    x0 = 0.5*a;
	x1 = 0.5*(x0 + (a/x0));
		while (abs (x1 - x0)> 0.0001)
		{
			x0 =x1;
			x1 =0.5*(x0 + (a/x0));
		}

    return x1;
}

bool isPal(long double n1)
{
    string r1,r2;
    r1=toString(n1);
    r2=r1;
    reverse(r2.begin(),r2.end());
    if(r1==r2)
        return true;
    else
        return false;
}

int main()
{

 freopen("input.in","rt",stdin);
 freopen("output.out","wt",stdout);

    string s1;
    int N;
    long double a,b,current,n,f,c1=0;
    cin>>N;
    FOR1(nn,N)
    {
        cin>>a>>b;
        f=modfl(isSquare(b),&n);
        cout<<fixed<<setprecision(0);
        current=n*n;

        while(current>=a)
        {

            if(isPal(current) && isPal(n) )
            {
                 c1++;
            }

            current=current-(2*n-1);
            n--;
        }
        cout<<"Case #"<<nn+1<<": "<<c1<<endl;
        c1=0;
    }
}





