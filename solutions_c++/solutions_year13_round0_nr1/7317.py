#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <sstream>

using namespace std;

#define REP(i,a,b) 	for(int i=a;i<(int)b;i++)
#define all(x) 		(x).begin(),(x).end()
#define pb 			push_back
#define clr(x,y)	memset(x,y,sizeof x)
#define oo 			(1<<30)
#define bit(x)		_builtin_popcount(x)
#define mp			make_pair
#define fst			first
#define snd			second



int main(){
	int T;
	string s[4];
	cin>>T;
	REP(ii,0,T){
		REP(i,0,4) cin>>s[i];
		bool x=0,o=0;
		int p=0,X,O;
		//filas
		REP(i,0,4){
			O=0,X=0;
			REP(j,0,4)
				if(s[i][j]=='O') O++;
				else if(s[i][j]=='X') X++;
				else if(s[i][j]=='T') O++,X++;
				else p++;
			if(X==4){x=true;break;}
			else if(O==4){o=true;break;}
		}
		//Columnas
		REP(i,0,4){
			O=0,X=0;
			REP(j,0,4)
				if(s[j][i]=='O') O++;
				else if(s[j][i]=='X') X++;
				else if(s[j][i]=='T') O++,X++;
				else p++;
			if(X==4){x=true;break;}
			else if(O==4){o=true;break;}
		}
		//Diagonales
		X=O=0;
		REP(i,0,4){
			if(s[i][i]=='O') O++;
			else if(s[i][i]=='X') X++;
			else if(s[i][i]=='T') O++,X++;
			else p++;
			if(X==4){x=true;break;}
			else if(O==4){o=true;break;}
		}
		X=O=0;
		REP(i,0,4){
			if(s[i][3-i]=='O') O++;
			else if(s[i][3-i]=='X') X++;
			else if(s[i][3-i]=='T') O++,X++;
			else p++;
			if(X==4){x=true;break;}
			else if(O==4){o=true;break;}
		}
		if(x) cout<<"Case #"<<ii+1<<": X won\n";
		else if(o)cout<<"Case #"<<ii+1<<": O won\n";
		else if(p==0)cout<<"Case #"<<ii+1<<": Draw\n";
		else cout<<"Case #"<<ii+1<<": Game has not completed\n";
	}

    return 0;
}




