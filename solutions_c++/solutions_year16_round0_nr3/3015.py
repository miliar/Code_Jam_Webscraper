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

int J, cnt;
int a[11];

ll clc(ll n, int dig, int base){
    ll ret = 0;
    for(int i = 0; i < dig; i++){
        ret += (n % 10) * powl(base, i);
        n /= 10;
    }

    return ret;
}

void go(int pos, int n, ll num){
    if(pos == n){
        if(cnt < J && (num % 10) == 1){
            bool f = true;
            for(int i = 2; i <= 10; i++){
                bool ff = false;
                ll tmp = clc(num, n, i);
                //cout<<num<<" "<<i<<" "<<tmp<<endl;
                for(int j = 2; j <= sqrt(tmp); j++){
                    if(tmp % j == 0){
                        a[i] = j;
                        ff = true;
                        break;
                    }
                }
                if(ff == false){
                    f = false;
                    break;
                }
            }

            if(f){
                cnt++;
                printf("%lld", num);
                FORAB(i, 2, 11){
                    //cout<<clc(num, n, i)<<endl;
                    //cout<<clc(num, n, i) % a[i]<<endl;
                    printf(" %d", a[i]);
                }
                printf("\n");
            }
        }

        return;
    }

    go(pos + 1, n, num * 10);
    go(pos + 1, n, num * 10 + 1);
}

int main(){
    read(in);
    write(out);
	int tc, n, cs = 1;
	scan(tc);
	while(tc--){
        cnt = 0;
        scanf("%d%d", &n, &J);
		printf("Case #%d:\n", cs++);
		go(1, n, 1);
	}
    return 0;
}
