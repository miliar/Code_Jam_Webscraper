/*  Towhidul Islam
    University Of Dhaka
    Problem Name :
    Algorithm Used :
*/

#include<bits/stdc++.h>

typedef long long ll;

#define SSTR(x)         dynamic_cast< ostringstream & >( \
                        (ostringstream() << dec << x )).str()
#define pb              push_back
#define mem(a, x)       memset(a, x, sizeof a)
#define PI              acos(-1)
#define all(a)          a.begin(), a.end()
#define ff              first
#define ss              second
#define read(in)        freopen("in.txt", "r", stdin)
#define write(out)      freopen("out.txt", "w", stdout)
#define INF             1<<30
#define eps             1e-9
#define FORN(i, n)      for(int i = 0; i < n; i++)
#define FORAB(i, x, n)  for(int i = x; i < n; i++)
#define FORD(i, x, n)   for(int i= n - 1; i >= x; i--)
#define scan(n)         scanf("%d", &n)
#define print(n)        printf("%d\n", n)
#define tor             vector
#define dbg(x)          cout<<#x<<" : "<<x<<endl
#define chkwhere        cout<<"LOL\n"
#define pii             pair<int, int>
#define MOD             1000000007
#define MAX             100007

using namespace std;

string s[10] = {"GGG", "GGL", "GLG", "GLL", "LGG", "LGL", "LLG", "LLL"};
int main(){
    read(in);
    write(out);

	int tc, cs = 1, c, k, s;
	scan(tc);
	while(tc--){
        scanf("%d%d%d", &k, &c, &s);
		printf("Case #%d:", cs++);
        if(k == 1){
            printf(" 1\n");
        }
        else{
            if(s == 1){
                puts(" IMPOSSIBLE");
            }
            else{
                if(c == 1){
                    if(s < k) puts(" IMPOSSIBLE");
                    else{
                        FORAB(i, 1, k + 1) printf(" %d", i);
                        puts("");
                    }
                }
                else{
                    if(s >= k - 1){
                        FORAB(i, 2, k + 1) printf(" %d", i);
                        puts("");
                    }
                    else{
                        puts(" IMPOSSIBLE");
                    }
                }
            }
        }
	}
    return 0;
}
