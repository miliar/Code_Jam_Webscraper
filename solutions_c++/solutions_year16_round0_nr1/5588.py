#include<iostream>
#include<fstream>
#include<math.h>
#include<algorithm>
#include<set>
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

string toString (tint number)
{
    ostringstream ostr;
    ostr << number;
    return  ostr.str();
}

tint res(tint n){
	if (n==0){
		return -1;
	}
	set<char> s;
	tint tot=0;
	while(s.size()<10 && tot<=n*100){
		tot+=n;
		string str=toString(tot);
		forn(i, str.size()){
			s.insert(str[i]);
		}
	}
	if (s.size()<10){
		return -1;
	}
	return tot;
}

int main (){
	ofstream myfile;
  	myfile.open ("salida-A-large.txt");
	tint t;
	ifstream inFile("A-large.in");
  	if (inFile.is_open()) {
  		inFile>>t;
    	//getline (inFile,t);
		forn(caso, t){
			tint n;
			//getline (inFile, n);
			inFile>>n;
			tint resul=res(n);
			if(resul==-1){
				myfile << "Case #"<<caso+1<<": "<<"INSOMNIA"<<endl;
			}else{
				myfile <<"Case #"<<caso+1<<": "<<resul<<endl;
			}
		}
		myfile.close();
	}else{
		cout<<"NOOO"<<endl;
	}
}

