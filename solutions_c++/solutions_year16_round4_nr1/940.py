#include <bits/stdc++.h>
using namespace std;

int T,N,A,B,C;
int poss[3][22][3];
string win[3][22];

int main(){
	cin>>T;
	poss[0][0][0] = 1; win[0][0] = "R";
	poss[1][0][1] = 1; win[1][0] = "P";
	poss[2][0][2] = 1; win[2][0] = "S";
	for(int i=1; i<=13; i++){
		for(int j=0; j<3; j++){
			for(int k=0; k<3; k++){
				poss[j][i][k] += poss[j][i-1][k];
				poss[j][i][(k+2)%3] += poss[j][i-1][k];
			}
			string a = win[j][i-1];
			string b = win[(j+2)%3][i-1];
			if( a<b ) win[j][i] = a + b;
			else win[j][i] = b + a;
		}
	}
	for(int t=1; t<=T; t++){
		cin>>N>>A>>B>>C;
		bool p = false;
		for(int j=0; j<3; j++){
			if( poss[j][N][0] == A && poss[j][N][1] == B && poss[j][N][2] == C ){
				p = true;
				cout<<"Case #"<<t<<": "<<win[j][N]<<"\n";
				break;
			}
		}
		if( !p ) cout<<"Case #"<<t<<": IMPOSSIBLE\n";
	}
	return 0;
}
