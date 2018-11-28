#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <memory.h>
#include <time.h>
#define sz(x) int((x).size())
#define FOR(i,a,b) for(ll(i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(ll(i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int(i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (ll(i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second
#define file freopen("input.txt","r",stdin)
#define file2 freopen("output.txt", "w",stdout)
using namespace std;
typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
#define mod 1000000007
#define inf 1e9
const int N = 100005;
int a[101][101];
int main()
{
    file;
    file2;
    int t;
    cin >> t;
    rep(qwerty, t)
    {
        int n;
        cin >> n;
        C(a);
        bool flag = true;
        rep(k,n)
        {
            string s;
            cin>>s;
            int number=1;
            int strlengthq=1;
            a[k][strlengthq]=1;
            char ch[101];
            for(int i=1; i<s.size(); i++)
            {
                if(s[i]==s[i-1]) number++;else
                {
                    a[k][strlengthq]=number; number=1;

                     if(k==0)
                        ch[strlengthq]=s[i-1];

                     if(k!=0)
                         if(ch[strlengthq]!=s[i-1]) flag=false;
                    strlengthq++;

                }
            }
            if(k==0)
                ch[strlengthq]=s[s.size()-1];

            if(k!=0)
                if(ch[strlengthq]!=s[s.size()-1]) flag=false;

            a[k][strlengthq]=number;
            a[k][0]=strlengthq;
        }

        for(int k=1; k<n; k++)
            if(a[k][0]!=a[k-1][0]) flag=false;

        for(int k=1; k<n; k++)
            for(int j=1; j<=a[k][0]; j++)
                if((a[0][j]==0 && a[k][j]==0) || (a[0][j]!=0 && a[k][j]!=0)) ;
                    else flag=false;
        printf("Case #%d: ", qwerty  + 1);
        if(!flag){ printf("Fegla Won\n"); continue;}

        int d[101];
        for(int i=1; i<=a[0][0]; i++) d[i]=0;

        for(int k=0; k<n; k++)
            for(int j=1; j<=a[k][0]; j++)
                d[j]+=a[k][j];

        for(int i=1; i<=a[0][0]; i++)
        {
            double ost =  double(d[i])/ double(n) - d[i]/n;
            d[i]=d[i]/n;
            if(ost>0.5) d[i]++;
        }
        int vidpovid=0;

        for(int i=0; i<n; i++)
            for(int j=1; j<=a[i][0]; j++)
                vidpovid+=abs(d[j]-a[i][j]);
        printf("%d\n",vidpovid);
    }
}
