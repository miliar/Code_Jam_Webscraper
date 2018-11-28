#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>


using namespace std;

struct Biglietto {
	int ingresso;
	int persone;
	
	Biglietto () {}
	
	Biglietto (int _i, int _p) {
		ingresso = _i;
		persone = _p;
	}
};

bool operator< (Biglietto const &a, Biglietto const &b) {
	if ( a.ingresso != b.ingresso ) return ( a.ingresso < b.ingresso );
	
	assert (1 == 0);
}

int n, m;
long long int mod = 1000002013;

map<int,int> entrate, uscite; // quanti passeggeri entrano/escono alla fermata k
set<int> eventi; // fermate a cui succede qualcosa
priority_queue<Biglietto> biglietti; // biglietti delle persone entrate

long long int costo (int h, int numpersone) {
	// costo di un viaggio di h fermate per numpersone persone
	
	long long int k = h;
	long long int c = k*n - k*(k-1)/2;
	c %= mod;
	c *= numpersone;
	c %= mod;
	
	return c;
}

void solve() {
	
	entrate.clear();
	uscite.clear();
	eventi.clear();
	assert( biglietti.empty() );
	
	long long int costo_teorico = 0;
	long long int costo_vero = 0;
	
	scanf("%d %d",&n,&m);
	
	for (int i=0; i<m; ++i) {
		int o,e,p;
		scanf("%d %d %d",&o,&e,&p);
		
		if ( entrate.count(o) == 0 ) entrate[o] = 0;
		if ( entrate.count(e) == 0 ) entrate[e] = 0;
		entrate[o] += p;
		
		if ( uscite.count(e) == 0 ) uscite[e] = 0;
		if ( uscite.count(o) == 0 ) uscite[o] = 0;
		uscite[e] += p;
		
		eventi.insert(o);
		eventi.insert(e);
		
		costo_teorico += costo( e-o, p );
		costo_teorico %= mod;
	}
	
	for (set<int>::iterator i = eventi.begin(); i != eventi.end(); ++i) {
		int k = (*i);
		// alla fermata k succede qualcosa
		
		int in = entrate[k];
		int out = uscite[k];
		
		// entrano in tizi alla stazione k
		biglietti.push( Biglietto(k,in) );
		
		// escono out tizi alla stazione k
		while ( out > 0 ) {
			Biglietto biglietto = biglietti.top();
			biglietti.pop();
			
			if ( biglietto.persone <= out ) {
				// uso tutte le persone che hanno quel biglietto
				costo_vero += costo( k - biglietto.ingresso, biglietto.persone );
				out -= biglietto.persone;
			}
			else {
				// non uso tutte le persone che hanno quel biglietto
				costo_vero += costo( k - biglietto.ingresso, out );
				biglietti.push( Biglietto( biglietto.ingresso, biglietto.persone - out ) );
				out = 0;
			}
		}
	}
	
	long long int risposta = costo_teorico - costo_vero;
	risposta = ( risposta + mod ) % mod;
	printf("%lld\n", risposta);
}

int main() {
	
	int t;
	scanf("%d",&t);
	
	for (int i=0; i<t; ++i) {
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
