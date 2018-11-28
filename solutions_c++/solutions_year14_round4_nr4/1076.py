#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define forn(i,n) for(int i=0; i<(int)(n); i++)
#define forsn(i,s,n) for(int i=(int)(s); i<(int)(n); i++)
#define pb push_back

int M, N;
const int MAXN = 16;
int res = 0;
int cant = 0;
int server[MAXN];
string s[16];

struct Trie
{
Trie() {cantidad = 0;}
int cantidad; // o cualquier dato relevante en cada nodo, lo mas basico es un bool con esta/no esta
map<char, Trie> hijos;
};

int count_tries(vector<string> v){
	Trie este;
	int res = 0;
	forn(i,v.size()){
		Trie * prox;
		forn(j,v[i].size()){
			if(j==0) prox= &(este.hijos[v[i][j]]);
			else prox = &((*prox).hijos[v[i][j]]);
			if((*prox).cantidad==0)res++;
			(*prox).cantidad++;
		}
	}
	return res+1;
}

void calc_res(){
	vector<string> v[N];
	forn(i,M)v[server[i]].pb(s[i]);
	forn(i,N)if(v[i].size()==0)return;
	//forn(i,N){forn(j,v[i].size())cout<<v[i][j]<<endl;cout<<endl;}
	int cnt = 0;
	forn(i,N)cnt+=count_tries(v[i]);
	if(cnt>res){
		res=cnt;
		cant=1;
	}
	else if(cnt==res)cant++;
	//cout<<cnt<<' '<<res<<' '<<cant<<endl;
	//cout<<"-----------"<<endl;
	return;
}

void assign(int pos){
	forn(i,N){
		server[pos]=i;
		if(pos+1 < M)assign(pos+1);
		else calc_res();
	}
}
int main(){
	int t; cin>>t;
	forn(tc,t){
		cin>>M>>N;
		forn(i,M)cin>>s[i];
		res=0; cant=0;
		assign(0);
		printf("Case #%d: %d %d\n", tc+1, res, cant);
	}
}
