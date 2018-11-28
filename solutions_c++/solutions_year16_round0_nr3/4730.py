#include<iostream>
#include<cmath>
#include<iomanip> //Per quan vulguis fer 'cout' currats (p.e. amb 4 decimals)
#include<vector>
#include<map>
#include<queue>
#include<fstream> //Per a fer que l'entrada i/o la sortida siguin fitxers
#include<algorithm>
#include<string>
#include<stack> //Poc útil
#include<numeric> //Poc útil
#include<set>
#include<sstream> //Per entrades complicades on no+ amb el cin no es pot
#include<list> //Poc útil

//cout.setf(ios::fixed);
//cout.precision(11);
// for(iMII it=M.begin();it!=M.end();++it) , per recorre map
//sort(V.begin(), V.end(), greater<int>());  // o reverse(V.begin, V.end)

#define INF 1000000000
#define LINF 1000000000000000000LL
#define EPS 1e-9
#define debug(x) cerr << #x << " = " << x << endl //Si vols saber el valor d'una variable fas debug(a);
#define FOR(x,y) for(int x=0;x<y;x++)             //En general el 'cerr' va bé per debuguejar (p.e. cerr<<"Hey!"<<endl;
#define FORU(x,y) for(int x=1;x<=y;x++)           //Pq així saps el que has de borrar abans d'enviar i si te l'oblides a vegades no passa res
using namespace std;


typedef long long ll;
typedef pair<int,int> PII;
typedef vector<PII> VP;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<ll> VL;
typedef vector<VL> VVL;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef map<int,int> MII;
typedef MII::iterator iMII; //L'iterador més utiltizat
//Personalitza'l al teu gust! ^^ espero que t'agradi

int N;
int J;
int comptador;
vector<long long> ispr;
vector<int> V;

void jamcoins(int i) {

    if ( i == N-1) {
        if (comptador >= J) return;
        vector<int> B(9);
        vector<int> NUM(9);
        for (int b = 2; b < 11; ++b) {
            long long num = 0;
            for (int k = 0; k < N; ++k) {
                num *= b;
                num += V[k];
            }
            //cout << num << endl;
            for(long long pr = 2; pr*pr <= num and B[b-2] == 0; ++pr) {
                if (num%pr == 0) {
                    B[b-2] = pr;
                }
                
            }
            if (B[b-2] == 0){
                return;
            }
//           cout << ' ' << num;
        }
//        cout << endl;
 //       cout << comptador << endl;
        for (int k = 0; k < N; ++k) cout << V[k];
        for (int j = 0; j < 9; ++j) {
            cout <<' ' << B[j];
        }
        cout << endl;
        ++comptador;
        return;
    }
    V[i] = 0;    
    jamcoins(i+1);
    V[i] = 1;
    jamcoins(i+1);

}

int main(){
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);

    int T; cin >> T;
    cin >> N;
     cin >> J;
    cout << "Case #" << T << ": " << endl;
    V = vector<int> (N);
     V[0] = 1;
     V[N-1] = 1;
     comptador = 0;
     jamcoins(1);
     /*
     ispr = vector<long long> (1);
    ispr[0]=ispr[1]=1;
    for (long long i=2; i*i<ispr.size(); ++i) if (ispr[i] == 0) {
    	for (long long j=2*i; j<ispr.size(); j+=i) ispr[j]=i;
    }
    /*while (comptador < J) {
        for (int i = 1; i < N-1; ++i) {
            V[i] = rand()%2;
        }
        
        vector<int> B(9);
        for (int b = 2; b < 11; ++b) {
            long long num = 0;
            for (int k = 0; k < N; ++k) {
                num *= b;
                num += V[k];
            }
            if (ispr[num] == 0){
                continue;
            } else {
                B[b-2] = ispr[num];
            }
  //          cout << ' ' << num;
        }
//        cout << endl;
        for (int k = 0; k < N; ++k) cout << V[k];
        for (int j = 0; j < 9; ++j) {
            cout <<' ' << B[j];
        }
        cout << endl;
        ++comptador;    
    }*/

}


