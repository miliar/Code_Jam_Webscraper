#include <bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define pb push_back
#define mp make_pair
typedef long long ll;

const int MAX = 1001;
int n,k;
string s;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,tc(1);
	cin >> T;
	while(T--){
        cin >> s >> k;
        n = (int) s.size();
        int res = 0;
        for(int i=0;i<n;i++){
            if(n-i < k) break;
            if(s[i] == '-'){
                ++res;
                for(int j=i;j<i+k;j++)
                    s[j] = (s[j] == '+' ? '-' : '+');
            }
        }
        bool possible = true;
        for(int i=0;i<n;i++)
            if(s[i] == '-')
                possible = false;
        cout << "Case #" << tc++ << ": ";
        if(possible){
            cout << res << endl;
        }else cout << "IMPOSSIBLE" << endl;
	}
    return 0;
}
