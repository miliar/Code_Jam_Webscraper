
/*===============*\
|  ID: TMANDZU    |
|    LANG: C++    |
\*===============*/
//Tornike Mandzulashvili
//std::ios_base::sync_with_stdio (false);

#include <bits/stdc++.h>

#define endl '\n'
#define EPS (1e-9)
#define Pi 3.14159265358979
#define INF 1000000500
#define pb push_back
#define mp make_pair
#define S size()
#define MX(aa,bb) (aa>bb?aa:bb)
#define MN(aa,bb) (aa<bb?aa:bb)
#define fi first
#define se second
#define PI pair < int , int >
#define VI vector < int >
#define DID (long long)
#define ll long long
#define AL(a) (a).begin(),(a).end()

using namespace std;

const int T = 25;

set <string> M,A,B,words[T];
int NUM,N;
set <int> nums[T];
map <string,int> MAP;
int d[10000],D[10000];

void renull(){
    for (int i = 0; i <T;i++)
        words[i].clear(), nums[i].clear();
    A.clear();
    B.clear();
    M.clear();
    NUM = N = 0;
    MAP.clear();
    memset(D,0,sizeof(D));
    memset(d,0,sizeof(d));
}

int main(){
    freopen("bil.in","r",stdin);
    freopen("bil.out","w",stdout);


    int tests;
    scanf("%d\n",&tests);
    for (int t = 1; t <= tests;  t++)
    {
        renull();
        scanf("%d\n",&N);
        string s = "";
        while (1){
            char ch = getchar();
            if (ch == ' '){
                A.insert(s);
                s = "";
            }else
            if (ch == '\n'){
                A.insert(s);
                s = "";
                break;
            }
            else
                s+=ch;
        }
        s = "";
        while (1){
            char ch = getchar();
            if (ch == ' '){
                B.insert(s);
                s = "";
            }else
            if (ch == '\n'){
                B.insert(s);
                s = "";
                break;
            }
            else
                s+=ch;
        }
        N-= 2;
        for (int i = 0; i < N;i++){
            string s = "";
            while (1){
                char ch = getchar();
                if (ch == ' '){
                    words[i].insert(s);
                    s = "";
                }else
                if (ch == '\n'){
                    words[i].insert(s);
                    s = "";
                    break;
                }
                else
                    s+=ch;
            }
        }

        for (string s : A)
            M.insert(s);
        for (string s : B)
            M.insert(s);
        for (int i = 0; i <N; i++)
            for (string s : words[i])
                M.insert(s);

        for (string s : M){
            if (!MAP.count(s))
            MAP[s]=++NUM;
        }
        for (string s : A)
            d[MAP[s]]|=1;

        for (string s : B)
            d[MAP[s]]|=2;

        for (int i = 0; i <N; i++)
            for (string s : words[i])
                nums[i].insert(MAP[s]);

        int ans = INF;
        for (int mask=0; mask < (1<<N); mask++){
            int cur = 0;
            for (int i = 0; i <= NUM;i++)
                D[i]=d[i];
            for (int i = 0; i < N; i++){
                bool is = (mask&(1<<i)) > 0;
                for (int x : nums[i]){
                    if (is)
                        D[x]|=1;
                    else
                        D[x]|=2;

                }
            }
            for (int i = 0; i <= NUM;i++)
            cur += D[i]==3;
            ans = min(ans, cur);
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
}








