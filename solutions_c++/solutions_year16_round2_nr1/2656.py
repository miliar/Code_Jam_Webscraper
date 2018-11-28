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

string solve(string s){
	map<int, tint> m;
	forn(i, 10){
		m[i]=0;
	}
	map<char, tint> d;
	forn(i, s.size()){
		d[s[i]]++;
	}
	m[0]=d['Z'];
	d['Z']-=m[0];
	d['E']-=m[0];
	d['R']-=m[0];
	d['O']-=m[0];
	m[6]=d['X'];
	d['S']-=m[6];
	d['I']-=m[6];
	d['X']-=m[6];
	m[8]=d['G'];
	d['E']-=m[8];
	d['I']-=m[8];
	d['G']-=m[8];
	d['H']-=m[8];
	d['T']-=m[8];
	m[3]=d['H'];
	d['T']-=m[3];
	d['H']-=m[3];
	d['R']-=m[3];
	d['E']-=m[3];
	d['E']-=m[3];
	m[4]=d['R'];
	d['F']-=m[4];
	d['O']-=m[4];
	d['U']-=m[4];
	d['R']-=m[4];
	m[5]=d['F'];
	d['F']-=m[5];
	d['I']-=m[5];
	d['V']-=m[5];
	d['E']-=m[5];
	m[2]=d['W'];
	d['T']-=m[2];
	d['W']-=m[2];
	d['O']-=m[2];
	m[1]=d['O'];
	d['O']-=m[1];
	d['N']-=m[1];
	d['E']-=m[1];
	m[7]=d['V'];
	d['S']-=m[7];
	d['E']-=m[7];
	d['V']-=m[7];
	d['E']-=m[7];
	d['N']-=m[7];
	m[9]=d['I'];
	d['N']-=m[9];
	d['I']-=m[9];
	d['N']-=m[9];
	d['E']-=m[9];
	string ret="";
	forn(i, 10){
		forn(j, m[i]){
			ret+=toString(i);
		}
	}
	return ret;
}

int main (){
	ofstream myfile;
  	myfile.open ("salida-A-R1B-posta-LARGE.txt");
	tint t;
	ifstream inFile("A-large-1B.in");
	inFile>>t;
	forn(caso, t){
		string s;
		inFile>>s;
		myfile<<"Case #"<<caso+1<<": "<<solve(s)<<endl;
	}
}

