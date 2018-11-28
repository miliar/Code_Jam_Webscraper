/* Vipul Jain */

#include <bits/stdc++.h>

using namespace std;

#define ull unsigned long long
#define ill long long int
#define pii pair<double,double>
#define pb(x) push_back(x)
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FB(i,a,n) for(int i=(a);i>=(n);--i)
#define FI(it,x) for(it=x.begin();it!=x.end();++it)
#define V(x) vector<x>
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define Su(x) scanf("%llu",&x)
#define Sf(x) scanf("%f",&x)
#define Sd(x) scanf("%lf",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl
#define fi first
#define se second

int main()
{	
	int t;
    S(t);
    F(i, 1, t + 1) {
        cout << "Case #" << i << ": ";
        ill ans = -1;
        ill n;
        Sl(n);
        set<ill> visited;

        if (n == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        if (n == 1) {
            cout << 10 << endl;
            continue;
        }
        
        int times = 100000;
        ill N = n;
        set<int> dig;

        while (times--  && visited.count(N) == 0) {
           visited.insert(N);
           ill temp = N;
           while(temp) {
                dig.insert(temp % 10);
                temp /= 10;
           }
           if (dig.size() == 10) {
                ans = N;
                break;
           }
           N += n; 
        }

        if (ans == -1) {
            cout << "INSOMNIA" << endl;
        } else {
            cout << ans << endl;
        }
    }
    return 0;
}

