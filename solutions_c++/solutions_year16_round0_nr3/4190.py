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

bint BS[11][35];

void precalc() {
	FOR(i,2,11)FOR(j,0,35) {
		if(j == 0)BS[i][j] = 1;
		else BS[i][j] = BS[i][j-1] * (bint)(i);
	}
}

bint val(string st, int base) {
	bint ret = 0;
	int l = st.S;
	for(int i = l-1; i >= 0; i--) {
		bint v = BS[base][l-i-1]*(bint)(st[i]-'0');
		ret += v;
	}
	return ret;
}

string rand_str(int l) {
	string ret = "1";

	FOR(i,0,l-2) {
		if(rand()% 2 == 0)ret = "0" + ret;
		else ret = "1" + ret;
	}
	while(ret.S < l-1)ret = "0" + ret;
	ret = "1"+ret;
	assert(ret.S == l);
	return ret;
}

const int PLM = 10000007;
char pm[PLM];
vector<bint> primes;

void sieve() {
	clr(pm, 1);
	pm[0] = pm[1] = 0;
	bint lm = sqrt(PLM);
	for(bint i = 2; i <= lm; i++) if(pm[i]) {
		for(bint k = i * i; k < PLM; k += i)pm[k] = 0;
	}

	primes.PB(2);
	for(bint i = 3; i <= PLM; i += 2) if(pm[i])primes.PB(i);
}

bint isp(bint v) {
	bint lm = sqrt(v);
	for(int i = 0; i < primes.S ; i++) {
		if(primes[i] > lm){
			// if(v == 1100011010000011) DEBUG(primes[i]);
			break; 
		}
		//assert(primes[i] >= 2);
		if(v % primes[i] == 0 && primes[i] != v)return primes[i];
	}
	return -1;
}

int main() {
    
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C_out_small.txt", "w", stdout);

    precalc();
    sieve();

    int T;
    cin >> T;
    FOR(xt,0,T) {

    	set<string> sst;
	    
    	int N, lagbe;
    	cin >> N >> lagbe;

    	printf("Case #%d:\n", xt+1);

	    while(lagbe) {
	    	string st = rand_str(N);
	    	if(sst.count(st))continue;
	    	bool good = true;
	    	vector<bint> ans;

	    	FOR(i,2,11) {
	    		bint v = val(st, i);
	    		assert(v >= 0);
	    		int dv = isp(v);
	    		if(dv < 0) {
	    			good = false; break;
	    		}
	    		else ans.PB(dv);
	    	}

	    	if(good) {
	    		cout << st;
	    		FOR(i,0,ans.S)cout << " " << ans[i];
	    		cout << endl;
	    		
	    		sst.insert(st);
	    		lagbe--; 
	    	}
	    } 
	}
    
    return 0;
}

/*                       _        _                       _           _ 
         ___  ___  _   _| |    __| | ___ _ __   __ _ _ __| |_ ___  __| |
        / __|/ _ \| | | | |   / _` |/ _ \ '_ \ / _` | '__| __/ _ \/ _` |
        \__ \ (_) | |_| | |  | (_| |  __/ |_) | (_| | |  | ||  __/ (_| |
        |___/\___/ \__,_|_|___\__,_|\___| .__/ \__,_|_|   \__\___|\__,_|
        Mukit Hasan, Jahangirnagar University.*/
