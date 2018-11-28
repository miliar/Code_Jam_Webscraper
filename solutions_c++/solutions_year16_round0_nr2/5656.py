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

tint res(string s){
	tint cambios=0;
	char toy=s[0];
	forsn(i, 1, s.size()){
		if (s[i]!=toy){
			cambios++;
			toy=s[i];
		}
	}
	if (s[s.size()-1]=='-'){
		cambios++;
	}
	return cambios;
}

int main (){
	ofstream myfile;
  	myfile.open ("salida-B-large.txt");
	tint t;
	ifstream inFile("B-large.in");
  	if (inFile.is_open()) {
  		inFile>>t;
    	//getline (inFile,t);
		forn(caso, t){
			string s;
			//getline (inFile, n);
			inFile>>s;
			tint resul=res(s);
			myfile <<"Case #"<<caso+1<<": "<<resul<<endl;
		}
		myfile.close();
	}else{
		cout<<"NOOO"<<endl;
	}
}
