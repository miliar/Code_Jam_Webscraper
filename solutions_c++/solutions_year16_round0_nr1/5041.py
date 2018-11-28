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

bool has(int v, int d) {
	
	string st = tos(v);
	int l = st.S;
	FOR(i,0,l)if(st[i]-'0' == d)return true;
	return false;
}

int cas; 
void solve(int N) {
	printf("Case #%d: ", ++cas);
	if(N == 0) {
		puts("INSOMNIA");
		return;
	}
	char done[12];
	clr(done, 0);
	int dcnt = 0;
	for(int i = 1; ; i++) {
		int mul = i * N;
		FOR(j,0,10)if(done[j]==0 && has(mul, j)==true) {
			done[j] = 1;
			dcnt++;
			if(dcnt == 10) {
				printf("%d\n", mul);
				return;
			}
		}
	}
}

void stdinp() {
	int T;
	cin >> T;
	FOR(t,0,T) {
		int N;
		cin >> N;
		solve(N);
	}
}

int main() {
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large-attempt0_out.txt", "w", stdout);
    cas = 0;
    
    stdinp();
    
    return 0;
}

/*                       _        _                       _           _ 
         ___  ___  _   _| |    __| | ___ _ __   __ _ _ __| |_ ___  __| |
        / __|/ _ \| | | | |   / _` |/ _ \ '_ \ / _` | '__| __/ _ \/ _` |
        \__ \ (_) | |_| | |  | (_| |  __/ |_) | (_| | |  | ||  __/ (_| |
        |___/\___/ \__,_|_|___\__,_|\___| .__/ \__,_|_|   \__\___|\__,_|
        Mukit Hasan, Jahangirnagar University.*/
