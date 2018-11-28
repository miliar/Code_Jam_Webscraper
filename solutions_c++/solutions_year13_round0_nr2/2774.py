#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define forn(i,n) for(int i=0; i<(int)(n); i++)
const int MAXN = 128;
int tab[MAXN][MAXN];
int corte[MAXN][MAXN];

int main(){
	int t; cin>>t; int caso=0;
	while(t>0){
		t--; caso++;
		int n, m;
		cin>>n>>m;
		forn(i,n)forn(j,m)cin>>tab[i][j];

		memset(corte,0,sizeof(corte));		
		forn(i,n){
			int mx = -1;
			forn(j,m)mx=max(mx, tab[i][j]);
			forn(j,m)if(tab[i][j]==mx)corte[i][j]=1;
		}
		/*
		forn(i,n){
			forn(j,m)cout<<corte[i][j];
			cout<<endl;
		}*/
		string res1="YES";
		forn(j,m){
			int count = 0;
			int mx = -1;
			forn(i,n){
				count+=corte[i][j];
				mx=max(mx, tab[i][j]);
			}
			//if(count!=0 && count!=n)res1="NO";
			if(count!=n)forn(i,n)if(tab[i][j]!=mx)res1="NO";	
		} 


		memset(corte,0,sizeof(corte));		
		forn(j,m){
			int mx = -1;
			forn(i,n)mx=max(mx, tab[i][j]);
			forn(i,n)if(tab[i][j]==mx)corte[i][j]=1;
		}
		string res2="YES";
		forn(i,n){
			int count = 0;
			int mx = -1;
			forn(j,m){
				count+=corte[i][j];
				mx=max(mx, tab[i][j]);
			}
			//if(count!=0 && count!=m)res2="NO";
			if(count!=m)forn(j,m)if(tab[i][j]!=mx)res2="NO";	
		} 
	printf("Case #%d: ", caso);
	if(res1=="YES" || res2=="YES")printf("YES\n");
	else printf("NO\n");
	}
}
