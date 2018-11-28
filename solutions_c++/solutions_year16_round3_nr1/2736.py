#include<iostream>
#include<fstream>
#include<math.h>
#include<algorithm>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<sstream>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n); i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n); i++)
#define esta(x,v) (find((v).begin(),(v).end(),(x)) !=  (v).end())
#define index(x,v) (find((v).begin(),(v).end(),(x)) - (v).begin())
#define debug(x) cout << #x << " = "  << x << endl
#define pb push_back
#define mp make_pair

typedef long long tint;
typedef unsigned long long utint;
typedef long double ldouble;

typedef vector<int> vint;

int toNumber (string s)
{
	int Number;
	if ( ! (istringstream(s) >> Number) ) Number = 0; // el string vacio lo manda al cero
	return Number;
}

string toString (int number)
{
    ostringstream ostr;
    ostr << number;
    return  ostr.str();
}

int main (){
	ofstream myfile;
  	myfile.open ("salida-A-1C-MANDAR.txt");
	tint t;
	ifstream inFile("A-large.in");
	inFile>>t;
	string s="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	forn(_, t){
		tint n;
		inFile>>n;
		vector< pair<int, int> > v;
		int su=0;
		forn(i, n){
			int p;
			inFile>>p;
			su+=p;
			v.pb(mp(p, i));
		}
		myfile<<"Case #"<<_+1<<":";
		bool listo=true;
		sort(v.begin(), v.end());
		while(v[v.size()-1].first>0){
			myfile<<" ";
			if (v[v.size()-1].first==2 && v[v.size()-2].first==1 && v.size()>2 && v[v.size()-3].first==0){
				v[v.size()-1].first-=1;
				myfile<<s[v[v.size()-1].second]<<" ";
				v[v.size()-1].first-=1;
				v[v.size()-2].first-=1;
				myfile<<s[v[v.size()-1].second]<<s[v[v.size()-2].second]<<" ";
			}else if (v[v.size()-1].first-1>=v[v.size()-2].first){
				v[v.size()-1].first-=2;
				myfile<<s[v[v.size()-1].second]<<s[v[v.size()-1].second];
			}else if (v[v.size()-1].first==v[v.size()-2].first){
				if (v.size()>2 && v[v.size()-3].first==v[v.size()-2].first){
					v[v.size()-1].first-=1;
					myfile<<s[v[v.size()-1].second];
				}else{
					v[v.size()-1].first-=1;
					v[v.size()-2].first-=1;
					myfile<<s[v[v.size()-1].second]<<s[v[v.size()-2].second];
				}
			}
			sort(v.begin(), v.end());
		}
		myfile<<endl;
	}
}

