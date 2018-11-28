#include <bits/stdc++.h>
using namespace std;

#define DB(v) cerr << #v << ' ' << v << endl
#define where(v) cerr << #v << ": " << v << ' '
#define F first
#define S second
#define pb push_back
#define forup(i,a,b) for(int i = a;i <= (int)b;++i)


const int N = 1009;

vector <int> panck;

int main()
{
    ios_base::sync_with_stdio(NULL); cin.tie(NULL);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tests; cin >> tests;
    forup(test,1,tests)
    {
        panck.assign(N,0);
        int n; cin >> n;
        int val;
        int ans = 0;
        forup(i,1,n){
            cin >> val;
            ans = max(ans,val);
            panck[val]++;
        }
        int cur;
        forup(number,1,ans){
            cur = number;
            forup(i,number+1,N-2){
                if(panck[i] == 0){continue;}
                cur += panck[i] * (i/number);
                if(i % number == 0){cur -= panck[i];}
            }
            ans = min(ans,cur);
        }
        cout << "Case #" << test << ": " << ans << '\n';
    }
    return 0;
}
