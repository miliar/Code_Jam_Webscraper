// Enjoy your stay.

#include <bits/stdc++.h>

//#define long long long
#define double long double
#define LOOPVAR_TYPE long

#define all(x) (x).begin(), (x).end()
#define sz(x) ((LOOPVAR_TYPE)(x).size())
#define foreach(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define GET_MACRO(_1, _2, _3, NAME, ...) NAME
#define _rep(i, n) _rep2(i, 0, n)
#define _rep2(i, a, b) for(LOOPVAR_TYPE i = (LOOPVAR_TYPE)(a); i < (LOOPVAR_TYPE)(b); i++)
#define rep(...) GET_MACRO(__VA_ARGS__, _rep2, _rep)(__VA_ARGS__)

#define fir first
#define sec second
#define mp make_pair
#define mt make_tuple
#define pb push_back

const double EPS = 1e-9;
const double PI = acos(-1.0);
const long INF = 1070000000LL;
const long MOD = 1000000007LL;

using namespace std;

typedef istringstream iss;
typedef stringstream sst;
typedef pair<LOOPVAR_TYPE, LOOPVAR_TYPE> pi;
typedef vector<LOOPVAR_TYPE> vi;

#include <sys/time.h>
long getTime(){
	struct timeval t;
	gettimeofday(&t, NULL);
	return t.tv_sec * 1000000LL + t.tv_usec;
}

int N;
double V, X;
double R[111], C[111];

void main2(){
	cin >> N >> V >> X;
	vector<pair<double,double>> H, L;
	bool existH = 0, existL = 0, existE = 0;
	rep(i, N){
		cin >> R[i] >> C[i];
		if(abs(C[i] - X) <= 1e-6){
			existE = 1;
			H.pb(mp(C[i] - X, R[i]));
		}else if(C[i] > X){
			existH = 1;
			H.pb(mp(C[i] - X, R[i]));
		}else{
			existL = 1;
			L.pb(mp(X - C[i], R[i]));
		}
	}
	if(!existE && (!existH || !existL)){
		cout<<"IMPOSSIBLE"<<endl;
		return;
	}
	sort(all(H));
	reverse(all(H));
	sort(all(L));
	reverse(all(L));
	/*cout<<"H"<<endl;
	rep(i,sz(H)){
		cout<<H[i].fir<<" "<<H[i].sec<<endl;
	}
	cout<<"L"<<endl;
	rep(i,sz(L)){
		cout<<L[i].fir<<" "<<L[i].sec<<endl;
	}*/
	double lo = 0, hi = 1e9;
	rep(_,100){
		double mi = (lo + hi) / 2;
		//cout<<setprecision(16)<<mi<<endl;
		double maxV = 0;
		double hiE = 0;
		double loE = 0;
		rep(i,sz(H)){
			double vol = H[i].sec * mi;
			double E = vol * H[i].fir;
			maxV += vol;
			//cout<<"H "<<i<<" +"<<vol<<endl;
			hiE += E;
		}
		rep(i,sz(L)){
			double vol = L[i].sec * mi;
			double E = vol * L[i].fir;
			maxV += vol;
			//cout<<"L "<<i<<" +"<<vol<<endl;
			loE += E;
		}
		//cout<<mi<<" mv::"<<maxV<<endl;
		if(hiE > loE){
			double dif = hiE - loE;
			//cout<<mi<<" dif:"<<dif<<endl;
			rep(i,sz(H)){
				if(abs(H[i].fir) <= 1e-6){
					break;
				}
				double vol = H[i].sec * mi;
				double E = vol * H[i].fir;
				if(dif <= E){
					double minusVol = dif / H[i].fir;
					maxV -= minusVol;
					break;
				}else{
					maxV -= vol;
					dif -= E;
				}
			}
		}else{
			double dif = loE - hiE;
			rep(i,sz(L)){
				if(abs(L[i].fir) <= 1e-6){
					break;
				}
				double vol = L[i].sec * mi;
				double E = vol * L[i].fir;
				if(dif <= E){
					double minusVol = dif / L[i].fir;
					maxV -= minusVol;
					break;
				}else{
					maxV -= vol;
					dif -= E;
				}
			}
		}
		//cout<<"mv: "<<maxV<<" "<<(maxV>=V ? "OK" : "NG")<<endl;
		if(maxV >= V){
			hi = mi;
		}else{
			lo = mi;
		}
	}
	cout<<setprecision(16)<<hi<<endl;
}

int main(){
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	
	
	int T;
	cin >> T;
	long start = getTime(), pre = start;
	rep(tc, 1, T + 1){
		cout << "Case #" << tc << ": ";
		main2();
		long now = getTime();
		cerr << tc << "/" << T << ": " << (now - pre) / 1000000. << endl;
		if(tc == T){
			cerr << "Total: " << (now - start) / 1000000. << endl;
			cerr << "  Ave: " << (now - start) / 1000000. / T << endl;
		}
		pre = now;
	}
}
