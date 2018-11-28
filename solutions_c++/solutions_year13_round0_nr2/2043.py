#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstdlib>

#define _for(i,n) for(int i = 0; i<n; i++)
#define _forlor(i,n) for(int i=n-1; i>=0; i--)
#define max(a,b) a<b?b:a
#define tmax 100

using namespace std;

int tabla [tmax][tmax];
int T, N, M;


bool amo[2] = {true, true},
	ofo[2] = {true, true};

bool verif( int n, int m ) 
{
	int c = tabla[n][m];
	amo[0] = amo[1] = ofo[0] = ofo[1] = true;
	//ofo
	_for(i,M){
		if (tabla[n][i] > c )
		{
			int pos = m-i;
			pos = pos/abs(pos) + 1;
			pos = pos/2;
			ofo[pos] = false;
// 			if(!(ofo[0] || ofo[1]))
// 				goto brra;
		}
	}
	_for(i,N){
		if (tabla[i][m] > c)
		{
			int pos = n-i;
			pos = pos/abs(pos) + 1;
			pos = pos/2;
			amo[pos] = false;
// 			if(!(amo[0] || amo[1]))
// 				goto brra;
		}
	}
brra:
	return (amo[0] && amo[1]) || (ofo[0] && ofo[1]);
}

int main(){
	freopen("in.in", "r", stdin);
	freopen("out.in", "w", stdout);

	cin>>T;

	_for(t,T){
// 		if(t = 25)
// 			cout<<"";
		cin>>N>>M;
		_for(n,N){
			_for(m,M){
				cin>>tabla[n][m];
			}
		}
// 
// 		_for(n,N){
// 			_for(m,M){
// 				cout<<tabla[n][m]<<" ";
// 			}
// 			cout<<endl;
// 		}
		
		bool wachda = true;
		_for(n,N){
			_for(m,M){
				if(!(wachda = verif(n,m))){
					goto baraka;
				}
			}
		}
baraka:
		string s = (wachda?"YES":"NO");
		cout<<"Case #"<<(t+1)<<": "<<s<<endl;
	}

	return 0;
}