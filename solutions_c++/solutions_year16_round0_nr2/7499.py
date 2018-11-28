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
        string s;
        cin >> s;
        int j = s.size() - 1;
        while (s[j] == '+') {
            j--;
        }
        int counter = 0;
        FB(k, j - 1, 0) {
            if (s[k] != s[k + 1]) {
                counter++;
            }
        }

        if (counter == 0 && s[0] == '+') {
            cout << 0 << endl;
        } else {
            cout << counter + 1 << endl;
        }
    }
    return 0;
}

