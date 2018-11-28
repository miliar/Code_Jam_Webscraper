#include<bits/stdc++.h>

using namespace std;

#define FOR(i,a,b)   	for(int (i)=(a);(i)<(b);(i)++)
#define PB           	push_back
#define INF          	(1 << 26)
#define DEBUG(___x)     cout<<#___x<<" = ["<<___x<<"]"<<endl
#define SORT(___a)      sort(___a.begin(),___a.end())
#define RSORT(___a)     sort(___a.rbegin(),___a.rend())
#define PI           	3.141592653589793238
#define MP           	make_pair
#define PII          	pair<int,int>
#define ALL(___v)       (___v).begin(), (___v).end()
#define VS           	vector<string>
#define VI           	vector<int>
#define S            	size()
//#define B				begin()
#define E				end()
#define print(___v)     {cout<<"[";if(___v.S)cout<<___v[0];FOR(___i,1,___v.S)cout<<","<<___v[___i];cout<<"]\n";}
#define clr(___x, ___v)	memset(___x, ___v , sizeof ___x);
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

int tu(int val) {return (1 << val);}
bool iset(int mask, int id) {if((mask & tu(id) ) != 0)return true;return false;}
void doset(int &mask, int id) {mask |= tu(id);}
void dounset(int &mask, int id) {mask = mask & (~tu(id));}

typedef long long 					bint;
template<typename T> string tos( T a ) 	{ stringstream ss; string ret; ss << a; ss >> ret; return ret;}

int tab[500][500];

char multf(char a, char b, int sb) {
    if(b == 1)return a*sb;
    
    char r = tab[b][a];
    r *= sb;
    return r;
}

int N;
int main() {
    
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out_C_small.txt", "w", stdout);
    
    string st = "ijk";
    FOR(i,0,3) FOR(j,0,3) {
        char ca = st[i]; char cb = st[j];
        if(ca == cb)tab[ca][cb] = -1;
        else {
            char r; int s = 1;
            char dd[500];clr(dd,0);dd[ca] = dd[cb] = 1;
            FOR(k,0,3)if(dd[st[k]] == 0) {
                r = st[k];break;
            }
            
            if(ca == 'j' && cb == 'i')s = -1;
            if(ca == 'k' && cb == 'j')s = -1;
            if(ca == 'i' && cb == 'k')s = -1;
            
            r *= s;
            tab[ca][cb] = r;
        }
    }
    
    int T;
    cin >> T;
    FOR(t,0,T) {
        int L, X; string vv, st="";
        cin >> L >> X >> vv;
        FOR(i,0,X)st += vv;
        N = st.S;
        
        int r, s; r = s = 1; int cnt = 0;
        for(int i = 0; i < N; i++) {
            r = multf(st[i], r, s);
            if(r < 0) {
                r = -r; s = -1;
            }
            else s = 1;
            
            if(cnt == 0 && r == (int)('i') && s==1) {
                cnt++;
                r = s = 1;
            }
            else if(cnt == 1 && r == (int)('j') && s==1) {
                cnt++;
                r = s = 1;
            }
        }
        if(cnt == 2 && r == (int)('k') && s==1) {
            cnt++;
            r = s = 1;
        }
        
        printf("Case #%d: %s\n",1+t, (cnt == 3 ? "YES":"NO"));
    }
    
    return 0;
}

/*                       _        _                       _           _ 
         ___  ___  _   _| |    __| | ___ _ __   __ _ _ __| |_ ___  __| |
        / __|/ _ \| | | | |   / _` |/ _ \ '_ \ / _` | '__| __/ _ \/ _` |
        \__ \ (_) | |_| | |  | (_| |  __/ |_) | (_| | |  | ||  __/ (_| |
        |___/\___/ \__,_|_|___\__,_|\___| .__/ \__,_|_|   \__\___|\__,_|
        Mukit Hasan, Jahangirnagar University.*/
