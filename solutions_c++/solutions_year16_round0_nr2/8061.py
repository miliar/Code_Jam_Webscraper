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
    freopen("B-large.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t,p=0;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;
        int n=s.size(),cnt=0;
        bool flag = (s[n-1]=='-');
        for(int i=0; i<n-1; i++)
        {
            if(s[i]!=s[i+1])
                cnt++;
        }
        cnt+=flag;
        cout<<"Case #"<<++p<<": "<<cnt<<endl;
    }

    return 0;
}
