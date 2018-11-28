#include <bits/stdc++.h>
using namespace std;

typedef    unsigned long long                 ull;
typedef    long long                          ll;
typedef    long double                        ld;
#define    Set(v,d)                           memset(v, d, sizeof(v))
#define    oo                                 100000007   //infinity
#define    F                                  first
#define    S                                  second
#define    pb                                 push_back
#define    sz(x)                              (int)(x.size())
#define    all(x)                             (x.begin()), (x.end())
#define    rall(x)                            (x.rbegin()), (x.rend())
typedef    vector<int>                        vi;
typedef    pair<int, int>                     ii;

const int N = 100005;
set<int>st;
bool complete(int Num){
    while(Num){
        st.insert(Num%10);
        Num /= 10;
    }
    if(st.size() == 10) return true;
    return false;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
    int T, cnt = 0;
    scanf("%d", &T);
    while(T--){
        int n;
        scanf("%d", &n);
        int Num = 0;
        for(int i=1; i<9000;i++){
            Num += n;
            if(complete(Num)){
                printf("Case #%d: %d\n", ++cnt, Num);
                goto there;
            }
        }
        printf("Case #%d: INSOMNIA\n", ++cnt);
    there:
        st.clear();
    }

    return 0;
}

