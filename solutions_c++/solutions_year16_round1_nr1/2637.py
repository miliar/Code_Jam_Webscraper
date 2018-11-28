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

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A-out-large.txt", "w", stdout);

    int T;
    cin >> T;
    FOR(t,0,T) {
        string st;
        cin >> st;

        int l = st.S;

        string res = "";
        FOR(i,0,l) {
            string va = res + tos(st[i]);
            string vb = tos(st[i]) + res;
            res = max(va, vb);
        }

        printf("Case #%d: ", t+1);
        cout << res << endl;
    }    

    return 0;
}

/*                       _        _                       _           _
         ___  ___  _   _| |    __| | ___ _ __   __ _ _ __| |_ ___  __| |
        / __|/ _ \| | | | |   / _` |/ _ \ '_ \ / _` | '__| __/ _ \/ _` |
        \__ \ (_) | |_| | |  | (_| |  __/ |_) | (_| | |  | ||  __/ (_| |
        |___/\___/ \__,_|_|___\__,_|\___| .__/ \__,_|_|   \__\___|\__,_|
        Mukit Hasan, Jahangirnagar University.*/