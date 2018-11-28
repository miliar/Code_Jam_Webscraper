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
#define B				begin()
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

VS digi;
int vals[1000];
string st;
string arr[] = {"2", "6", "4", "0", "1", "7", "9", "3", "8", "5"};

int gcount(string st) {
	int ret = INF;
	FOR(i,0,st.S) {
		ret = min(ret, vals[st[i]]);
	}
	if(ret == INF)ret = 0;
	return min(ret, 1);
}

int main() {
    
    // freopen("in.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
	digi.PB("TWO");
	digi.PB("SIX");
	digi.PB("FOUR");
	digi.PB("ZERO");
	digi.PB("ONE");
	digi.PB("SEVEN");
	digi.PB("NINE");
	digi.PB("THREE");
	digi.PB("EIGHT");
	digi.PB("FIVE");	
	
	int T;
	cin >> T;
	FOR(cas, 0 , T) {
		clr(vals, 0);
		cin >> st;
		string ans = "";		

		FOR(i,0, st.S) vals[st[i]]++;
		FOR(i,0,10) {
			
			while(true) {
				int v = gcount(digi[i]);
				if(!v)break;
				FOR(j,0,v)ans += arr[i];
				FOR(j,0,digi[i].S)vals[digi[i][j]] -= v;
			}			
		}
		SORT(ans);
		printf("Case #%d: ", cas+1);
		cout << ans << endl;
	}

	FOR(i,0,1000)assert(vals[i] == 0);

    return 0;
}

/*                       _        _                       _           _ 
         ___  ___  _   _| |    __| | ___ _ __   __ _ _ __| |_ ___  __| |
        / __|/ _ \| | | | |   / _` |/ _ \ '_ \ / _` | '__| __/ _ \/ _` |
        \__ \ (_) | |_| | |  | (_| |  __/ |_) | (_| | |  | ||  __/ (_| |
        |___/\___/ \__,_|_|___\__,_|\___| .__/ \__,_|_|   \__\___|\__,_|
        Mukit Hasan, Jahangirnagar University.*/
