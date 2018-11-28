//include
//------------------------------------------
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//math
//-------------------------------------------
template<class T> inline T sqr(T x) {return x*x;}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

int main(){
	int T;
	cin >> T;
	for(int t = 0; t< T; t++){
		string s;
		cin >> s;
		
		
		int size = s.size();
						int flag = 0;
				for(int k = 0; k< size; k++){
					if(s[k] == '-'){
						flag = 1;
					}
				}
				
				if(flag == 0){
					cout << "Case #" << t + 1 << ": " << "0" << endl;
					
					
				}else{
		
		list<string> q;
		list<int> q2;
		list<string> d;
		q.PB(s);
		q2.PB(0);
		d.PB(s);
		while(1){
			string ts = q.front();
			q.pop_front();
			int n = q2.front();
			q2.pop_front();
			int f =0;
			for(int i = 0; i < size; i++){
				//上i+1子をひっくり返したものをttsに入れる
				string tts  = ts.substr(i+1);
										dump(tts);

				for(int k= 0; k < i+1; k++){
					if(ts[k] == '-'){
						dump(tts);
						tts = "+" + tts;
					}else{
												dump(tts);

						tts = "-" + tts;
					}
					dump(tts);
				}
				
				
				
				
				if(find(d.begin(),d.end(),tts) == d.end()){
					q.PB(tts);
					q2.PB(n + 1);
					d.PB(tts);
				}
				
				int flag = 0;
				for(int k = 0; k< size; k++){
					if(tts[k] == '-'){
						flag = 1;
					}
				}
				
				if(flag == 0){
					cout << "Case #" << t + 1 << ": " << n+1 << endl;
					f= 1;
					break;
				}
					
			}
			if(f == 1){
				break;
			}
				
		}
			
		}
			
			
		
		//cout << "Case #" << t + 1 << ": " << endl;

		
	}
}
	
