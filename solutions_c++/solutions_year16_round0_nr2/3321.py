#include<bits/stdc++.h>
using namespace std;
int arrr[1000005];
#define ll long long int
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>
#define VP vector<pair<int,int> >
#define II pair<int,int> 
#define ll long long int
#define mem(in,val) memset(in,val,sizeof(in)) 
#define mp make_pair 
#define sol first
#define Y second
#define pb push_back
#define rep(i,in,b) for(int i=in;i<b;i++)
/*Use like- 
rep(i,0,n - 1)
*/
template<class T> T pwr(T b, T pr){T r=1,sol=b;while(pr){if(pr&1)r*=sol;sol*=sol;pr=(pr>>1);}return r;}
 
#define     inf             (0x7f7f7f7f)
char inp[105];
int main() { 
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout); 
    int Tcases;
    scanf("%d", &Tcases);
    for(int tc=1;tc<= Tcases;tc++) {
        cin>>inp;
        int n = strlen(inp);
        int ans = 0;
        while (true) {
            bool done = true;
            int k = 0;
            while (k < n && inp[k] == inp[0]) {
                ++k;
            }
            if (k < n) {
                ++ans;
                for (int i = 0, j = k - 1; i < j; ++i, --j) {
                    swap(inp[i], inp[j]);
                }
                for(int i=0;i< k;i++) {
                    inp[i] = '+' + '-' - inp[i];
                }
            } else {
                if (inp[0] == '-') {
                    ++ans;
                }
                break;
            }
        }
        printf("Case #%d: %d\n", tc, ans);
    }
 
    return 0;
}