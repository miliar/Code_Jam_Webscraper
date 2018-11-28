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

map<tint, tint> m;

tint esPrimo(tint n){
	//if ()
	for(tint d=2; d*d<=n; d++){
		if (n%d==0){
			return d;
		}
	}
	return 1;
}

int main (){
	ofstream myfile;
  	myfile.open ("salida-C-prueba.txt");
  	myfile<<"Case #1:"<<endl;
	int a[16];
	a[0]=1;
	a[15]=1;
	int mande=0;
	forsn(i, 1, 14){
		a[i]=0;
	}
	forn(a1, 2){
	forn(a2, 2){
	forn(a3, 2){
	forn(a4, 2){
	forn(a5, 2){
	forn(a6, 2){
	forn(a7, 2){
	forn(a8, 2){
	forn(a9, 2){
	forn(a10, 2){
	forn(a11, 2){
	forn(a12, 2){
	forn(a13, 2){
	forn(a14, 2){
		a[1]=a1;
		a[2]=a2;
		a[3]=a3;
		a[4]=a4;
		a[5]=a5;
		a[6]=a6;
		a[7]=a7;
		a[8]=a8;
		a[9]=a9;
		a[10]=a10;
		a[11]=a11;
		a[12]=a12;
		a[13]=a13;
		a[14]=a14;
		bool si=true;
		vector<tint> divs;
		forsn(base, 2, 11){
			tint num=0;
			tint pot=1;
			forn(i, 16){
				num+=(a[15-i]*pot);
				pot*=base;
			}
			if (base==2){
				cout<<"VOY POR (BASE 2)  "<<num<<endl;
			}
			if (base==10){
				cout<<"VOY POR base 10..  "<<num<<endl;
			}
			tint div=esPrimo(num);
			if (div==1){
				si=false;
				break;
			}else{
				divs.pb(div);
			}
		}
		if(si && mande<50){
			string s="";
			forn(i, 16){
				s+=toString(a[i]);
			}
			forn(i, divs.size()){
				s+=(" " + toString(divs[i]));
			}
			myfile<<s<<endl;
			mande++;
		}
	}	
	}	
	}	
	}	
	}	
	}	
	}	
	}	
	}	
	}	
	}	
	}	
	}
	}
}

