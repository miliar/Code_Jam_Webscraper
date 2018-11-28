#include <bits/stdc++.h>
using namespace std;
#define repeat(x) for(int fl = 0;fl < int(x) ; fl ++)
#define repeat2(x) for(int fl2=0;fl2 < int(x) ;fl2++)
#define repeat3(x) for (int fl3 = 0;fl3 < int(x)  ;fl3 ++)
#define rep(a, b) for (int r = int(a); r <= int(b); r++)
template <typename T1, typename T2> inline std::ostream& operator << (std::ostream& os, const std::pair<T1, T2>& p){return os << "\033[1;32m(\033[0m" << p.first << ", " << p.second << "\033[1;32m)\033[0m";}template<typename T> inline std::ostream &operator << (std::ostream & os,const std::vector<T>& v){bool ___first359 = true;os << "\033[1;31m[\033[0m";os<<"\033[0;32m(";os<<v.size();os<<") \033[0m";for(unsigned int i = 0; i < v.size(); i++){if(!___first359)os << ", ";os << v[i];___first359 = false;}return os << "\033[1;31m]\033[0m";}template<typename T>inline std::ostream &operator << (std::ostream & os,const std::set<T>& v){bool first = true;os << "[";for (typename std::set<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii){if(!first)os << ", ";os << *ii;first = false;}return os << "]";}template<typename T1, typename T2>inline std::ostream &operator << (std::ostream & os,const std::map<T1, T2>& v){bool first = true;os << "[";for (typename std::map<T1, T2>::const_iterator ii = v.begin(); ii != v.end(); ++ii){if(!first)os << ", ";os << *ii ;first = false;}return os << "]";}
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
#define x first
#define y second
#define pb push_back
#define mk make_pair
#define inf (int)1e9 // 10^9 , change to 2 billion if need be
#define minf (int)-1e9 // -10^9
#define mil 1000000// 10 ^ 6
#define ri(x) cin >> x
#define rii(x, y) cin >> x >> y
#define riii(x, y, z) cin >> x >> y >> z
#define dri(x) int x; cin >> x
#define drii(x, y) int x, y; cin >> x >> y
#define foreach(v, c)  for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define trace1(x)							cerr << "\033[0;31m" << #x << ": " <<"\033[0m" << x << endl;
#define trace2(x, y)						cerr << "\033[0;31m" << #x << ": " <<"\033[0m" << x << "\033[0;31m"<<" | " << #y << ": "<<"\033[0m"  << y << endl;
#define trace3(x, y, z)						cerr << #x << ": " << "\033[0m" << x << "\033[0;31m" << " | " << #y << ": " <<"\033[0m" << y << "\033[0;31m" <<  " | " << #z << ": " <<"\033[0m" << z << endl;
#define trace4(a, b, c, d)       			cerr << #a << ": " <<"\033[0m" << a << "\033[0;31m" <<" | " << #b << ": "<<"\033[0m"  << b << "\033[0;31m" <<" | " << #c << ": "<<"\033[0m"  << c << "\033[0;31m" <<" | " << #d << ": "<<"\033[0m"  << d << endl;
#define trace5(a, b, c, d, e)    			cerr << #a << ": "<<"\033[0m"  << a << "\033[0;31m" <<" | " << #b << ": "<<"\033[0m"  << b << "\033[0;31m" <<" | " << #c << ": " <<"\033[0m" << c << "\033[0;31m" <<" | " << #d << ": "<<"\033[0m"  << d << "\033[0;31m" <<" | " << #e << ": " <<"\033[0m" << e << endl;
#define trace6(a, b, c, d, e, f) 			cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;








      


int main(){ios_base::sync_with_stdio(false);

		int t; cin>>t ;int ca = 0;
		while(t--) {++ca;
			cout << "Case #"<<ca<<": ";
			ll n; cin>>n;
			if(n == 0)
			{
				cout << "INSOMNIA\n";
				continue;
			}
			long long int x = 1; 
			vector<bool> seen(10, false);
			while(1){
				bool f = true;
				repeat(10) {
					if(seen[fl] == false){f = false; break;}
				}
				if(f)break;
				ll temp = (ll)n *(ll) x;
				while(temp != 0){
					seen[temp % 10] = true;
					temp /= 10;
				}
				++x;
			}
			cout << n*(x-1) << endl;
		}



















return 0;
}
