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
#include <string>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <memory.h>
#include <limits>
#include <ext/hash_map>
#include <algorithm>
using namespace std;

#define SZ(X) (int)(X).size()
#define ALL(X) (X).begin(),(X).end()
#define ALLR(X) (X).rbegin(),(X).rend()

typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;
#define EPS 1-e9


int main()
{
    freopen("A-large.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t,p=0;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<++p<<": INSOMNIA"<<endl;
            continue;
        }
        int g = n;
        int a[10];
        fill(a,a+10,0);
        bool ok = false;
        int i=1;
        while(ok == false)
        {
            int temp = n;
            while(temp)
            {
                a[temp%10]++;
                temp/=10;
            }
            bool flag = false;
            for(int j=0; j<10; j++)
            {
                if(a[j]==0)
                {
                    flag = true;
                    break;
                }
            }
            if(flag==false)
            {
                ok = true;
                cout<<"Case #"<<++p<<": "<<n<<endl;
                break;
            }
            n=g*(++i);
        }
    }
    return 0;
}
