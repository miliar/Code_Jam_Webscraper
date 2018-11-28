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

struct data{
    char N;
    int cnt;
    data(char n, int c){
        N = n;
        cnt = c;
    }
};

bool comp(const data &p, const data &q){
    return p.cnt > q.cnt;
}

vector<data>a;

bool isSafe(int cur, vector<data>tmp){
    FORAB(i, 0, tmp.size()){
        if(cur < tmp[i].cnt * 2) return false;
    }
    return true;
}

int main(){
    read(in);
    write(out);
	int tc, n, cs = 1, tmp;
	scan(tc);
	while(tc--){
        scan(n);
        int cur = 0;
        FORAB(i, 0, n){
            scan(tmp);
            cur += tmp;
            a.pb(data(i+'A', tmp));
        }
        //FORAB(i, 0, n) cout<<a[i].N<<endl;

        printf("Case #%d:", cs++);

        while(cur > 0){
            sort(all(a), comp);
            vector<data>t = a;
            t[0].cnt -= 1;
            if(isSafe(cur - 1, t)){
                printf(" %c", t[0].N);
                cur -= 1;
                a = t;
            }
            else{
                t = a;
                t[0].cnt -= 2;
                if(isSafe(cur - 2, t)){
                    printf(" %c%c", t[0].N, t[0].N);
                    cur -= 2;
                    a = t;
                }
                else{
                    t = a;
                    t[0].cnt -= 1;
                    t[1].cnt -= 1;
                    if(isSafe(cur - 2, t)){
                        printf(" %c%c", t[0].N, t[1].N);
                        cur -= 2;
                        a = t;
                    }
                }
            }
        }
        puts("");
        a.clear();
	}

    return 0;
}
