#include<bits/stdc++.h>

using namespace std;

#define FOR(i,a,b)      for(int (i)=(a);(i)<(b);(i)++)
#define PB              push_back
#define INF             (1e8)+7
#define DEBUG(___x)     cout<<#___x<<" = ["<<___x<<"]"<<endl
#define SORT(___a)      sort(___a.begin(),___a.end())
#define RSORT(___a)     sort(___a.rbegin(),___a.rend())
#define MP              make_pair
#define PII             pair<int,int>
#define ALL(___v)       (___v).begin(), (___v).end()
#define VS              vector<string>
#define VI              vector<int>
#define S               size()
#define print(___v)     {cout<<"[";if(___v.S)cout<<___v[0];FOR(___i,1,___v.S)cout<<","<<___v[___i];cout<<"]\n";}
#define clr(___x, ___v) memset(___x, ___v , sizeof ___x);
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

int tu(int val) {return (1 << val);}
bool iset(int mask, int id) {if((mask & tu(id) ) != 0)return true;return false;}
void doset(int &mask, int id) {mask |= tu(id);}
void dounset(int &mask, int id) {mask = mask & (~tu(id));}

typedef long long                   bint;
template<typename T> string tos( T a )  { stringstream ss; string ret; ss << a; ss >> ret; return ret;}

int AR[100];

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A-out-large.txt", "w", stdout);

    int T, N;
    scanf("%d", &T);
    FOR(cas,1,T+1) {
        scanf("%d", &N);
        FOR(i,0,N) {
            cin >> AR[i];
        }

        printf("Case #%d:", cas);
        while(true) {
            int mx = 0;
            int cnt = 0;
            VS d;

            FOR(i,0,N) {
                mx = max(mx, AR[i]); 
                if(AR[i] > 0)cnt++;
            }

            if(cnt == 0)break;
            else if(cnt <= 2) {
                FOR(i,0,N) {
                    if(AR[i] > 0) {
                        char ch = i+'A';
                        d.PB(tos(ch));
                        AR[i]--;
                    }
                }
            }
            else {
                FOR(i,0,N) {
                    if(AR[i] == mx) {
                        char ch = i+'A';
                        d.PB(tos(ch));
                        AR[i]--;
                        break;
                    }
                }
            }

            printf(" ");
            FOR(i,0,d.S)cout<<d[i];
        }        
        cout << endl;
    }

    return 0;
}

/*                       _        _                       _           _
         ___  ___  _   _| |    __| | ___ _ __   __ _ _ __| |_ ___  __| |
        / __|/ _ \| | | | |   / _` |/ _ \ '_ \ / _` | '__| __/ _ \/ _` |
        \__ \ (_) | |_| | |  | (_| |  __/ |_) | (_| | |  | ||  __/ (_| |
        |___/\___/ \__,_|_|___\__,_|\___| .__/ \__,_|_|   \__\___|\__,_|
        Mukit Hasan, Jahangirnagar University.*/