///SACAR FREOPEN.
#include <iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<set>
#include<list>
#include<cstdlib>
#include<cstdio>
#include<iomanip>
#include<stack>
#include<queue>
#include<stdio.h>
#include<string.h>
#include<map>
#include<sstream>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define dforn(i,n) for(int i=n-1;i>=0;i--)
#define formn(i,m,n) for(int i=m;i<(int)n;i++)
#define dformn(i,m,n) for(int i=n-1;i>=m;i--)
#define mp make_pair
#define pb push_back

const double PI=acos(-1.0);

typedef long long tint;
typedef pair<int,int> pint;

int main(){
//freopen("Blarge.txt","r",stdin);
freopen("BlargeInput.txt","r",stdin);
freopen("BlargeOutput.txt","w",stdout);
	int TC;cin>>TC;
	formn(tc,1,TC+1){
		int n,m;cin>>n>>m;
		///n filas, m columnas.
		int t[n][m];
		forn(i,n) forn(j,m) cin>>t[i][j];
		
		bool ok[n][m];
		forn(i,n) forn(j,m) ok[i][j] = false;
		
		///Los menores de cada fila.
		forn(f,n){
			///Para la fila f.
			vector<int> indices;
			int biggest = -1;
			forn(c,m){
				if(t[f][c] > biggest){
					biggest = t[f][c];
					indices.clear();
					indices.pb(c);
				}
				else if(t[f][c] == biggest){
					indices.pb(c);
				}
			}
			forn(i,indices.size()) ok[f][indices[i]]=true;
		}
		
		///Los menores de cada columna.
		forn(c,m){
			///Para la columna c.
			vector<int> indices;
			int biggest = -1;
			forn(f,n){
				if(t[f][c] > biggest){
					biggest = t[f][c];
					indices.clear();
					indices.pb(f);
				}
				else if(t[f][c] == biggest){
					indices.pb(f);
				}
			}
			forn(i,indices.size()) ok[indices[i]][c]=true;
		}
		
		bool can= true;
		forn(i,n) forn(j,m) if(!ok[i][j]) can = false;
		//forn(i,n) {forn(j,m) {cout<<ok[i][j]<<" ";}cout<<endl;}
		
		if(can) cout<<"Case #"<<tc<<": "<<"YES" <<endl;
		else cout<<"Case #"<<tc<<": "<<"NO" <<endl;
	}
    return 0;
}
