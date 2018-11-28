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
  	myfile.open ("salida-A-R1A-posta-large.txt");
	tint t;
	ifstream inFile("A-large-R1A.in");
	inFile>>t;
	forn(caso, t){
		string s;
		inFile>>s;
		string res="";
		if (s.size()==1){
			res=s;
		}else{
			res+=s[0];
			forsn(i, 1, s.size()){
				if (res[0]<=s[i]){
					res=s[i]+res;
				}else{
					res+=s[i];
				}
			}
		}
		myfile<<"Case #"<<caso+1<<": "<<res<<endl;
		
	}
}

