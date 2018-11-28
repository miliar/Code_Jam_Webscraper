#include <iostream>
#include <vector>
#include <map>
#include <math.h>
#include <cmath>
#include <set>
#include <algorithm>
#include <stack>
#include <stdio.h>
#include <string>
using namespace std;

#define forsn(i,s, n) for(int i=(int)s; i<(int)(n); i++)
#define forn(i, n) forsn(i,0,n)
#define fore(i,n) forn(i,n.size())
#define fori(i, n) for(typeof n.begin() i=n.begin(); i!=n.end();i++)
#define RAYA cout<<"-----------------"<<endl;
#define dbg(x) cout<<#x<<":"<<(x)<<endl;

typedef long long int tint;
typedef long double ldouble;
typedef  pair <tint,tint> pii;
typedef  pair <string,string> pss;
typedef  pair <tint,pii> piii;
typedef  pair <piii,pss> piiiss;

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(n) n.begin(),n.end()

const tint INF=2000000000;

bool tab[4][4];
bool mat[4][4];


int main(){
	int T;
	cin>>T;
	forn(caso,T){
		int N; cin>>N;
		char c;
		int res=1000;
		forn(i,N)forn(j,N){
			cin>>c;
			if(c=='0'){tab[i][j]=false;
			}else{tab[i][j]=true;}
		}
		forn(mask,1<<(N*N)){
			int cont=0;
			forn(i,N*N)if(mask & (1<<i))cont++;
			forn(i,N)forn(j,N){
				mat[i][j]=tab[i][j] || (mask & (1<<(i+j*N)));
			}
			bool flag=true;
			/*forn(i,N){
				set<int> maq;
				forn(j,N)if(mat[i][j])maq.insert(j);
				set<int> tipos;
				fori(j,maq)forn(ii,N)if(mat[ii][*j])tipos.insert(ii);
				fori(ii,tipos)forn(j,N)if(mat[*ii][j])if(maq.find(j)==maq.end())flag=false;
				if(maq.size()!=tipos.size())flag=false;
			}*/
			vector<int> tipos(N);
			vector<int> maq(N);
			forn(i,N)forn(j,N)if(mat[i][j]){
				tipos[i]++;
				maq[j]++;
			}
			forn(i,N)if(tipos[i]==0)flag=false;
			forn(j,N)if(maq[j]==0)flag=false;
			forn(i,N)forn(j,N)if(mat[i][j])if(tipos[i]!=maq[j])flag=false;
			forn(i,N)forn(j,N)if(mat[i][j])forn(ii,N)if(mat[ii][j])if(tipos[i]!=tipos[ii])flag=false;
			forn(i,N)forn(j,N)if(mat[i][j])forn(jj,N)if(mat[i][jj])if(maq[j]!=maq[jj])flag=false;
			forn(i,N)forn(j,N)if(mat[i][j])forn(ii,N)if(mat[ii][j])forn(jj,N)if(mat[ii][jj]){
				if(!mat[i][jj])flag=false;
			}
			if(flag)res=min(res,cont);			
		}
		cout<<"Case #"<<caso+1<<": "<<res<<endl;
	}
    return 0;
}
