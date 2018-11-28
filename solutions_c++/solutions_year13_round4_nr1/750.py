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

///TINTSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

const tint mod = 1000002013LL;

int main(){
freopen("Ain.txt","r",stdin);
freopen("Aout.txt","w",stdout);
	tint TC;cin>>TC;
	formn(tc,1,TC+1){
		tint n, m; cin>>n>>m;
		tint costoSinTrampa = 0;
		vector<pair<pair<tint,tint>,tint> > paradas;///<estacion , e/s, cant. gente>
		forn(i,m){
			tint u,v,p; cin>>u>>v>>p;
			paradas.pb(mp(mp(u,0),p));
			paradas.pb(mp(mp(v,1),p));
			tint delta = v - u;
			tint costoActual = ((2*n - delta + 1) * (delta))/2;
			costoActual %= mod;
			costoActual *= p;
			costoActual %= mod;
			costoSinTrampa += costoActual;
			costoSinTrampa %= mod;
		}
//cout<<"costoSinTrampa: "<<costoSinTrampa<<endl;
		sort(all(paradas));
		
		tint precio = 0;
		///proceso la primer subida de gente.
		pair<pair<tint,tint>,tint> p0 = paradas[0];
		tint eP = p0.first.first;
		tint genteAca = p0.second;
		vector<pair<tint,tint> > boletos;///<precio , cantidad>
		///en boletos mantengo los boletos en cada momento del recorrido,
		///ordnados de menor a mayor costo.
		boletos.pb(mp(n,genteAca));
		for(tint i = 1; i<2*m; i++){
			///proceso la parada i. Puede ser la misma que la anterior. Sube/baja gente.
			pair<pair<tint,tint>,tint> pA =paradas[i];
			tint eA = pA.first.first;
			tint sb = pA.first.second;
			tint gA = pA.second;
//cout<<eA<<" "<<sb<<" "<<gA<<endl;
			///primero updateo los boletos viejos que llegaron hasta aca.
			tint delta = eA - eP;
			forn(j,boletos.size()){
				///<precio , cantidad>
				tint precioBoleto = boletos[j].first;
				tint genteConEsteBoleto = boletos[j].second;
				tint costoViajeEntreEstaciones = ((2*precioBoleto - delta + 1LL)*(delta))/2;
				costoViajeEntreEstaciones %= mod;
				costoViajeEntreEstaciones *= genteConEsteBoleto;
				costoViajeEntreEstaciones %= mod;
				precio += costoViajeEntreEstaciones;
				precio %= mod;
				tint nuevoPrecioBoleto = precioBoleto - delta;
				boletos[j].first = nuevoPrecioBoleto;
			}
/*cout<<"precio: "<<precio<<endl;
cout<<"boletos: "<<boletos.size()<<endl;
forn(ii,boletos.size()){
	cout<<boletos[ii].first<<" "<<boletos[ii].second<<endl;
}
cout<<endl;*/
			if(sb == 0){
				///gA gente que sube con boletos de precio n.
				boletos.pb(mp(n,gA));
			}
			else{///sb == 1
				///gA gente que baja.
				tint falta = gA;
				///tengo que sacar a gA gente.
				tint k = boletos.size() - 1;
				while(falta > 0){
					///tengo que sacar gente del ultimo boleto.
					if(boletos[k].second >= falta){
						///saco de aca lo que queda
						boletos[k].second -= falta;
						if(boletos[k].second == 0) boletos.pop_back();
						break;///termine.
					}
					else{
						///saco todos los de aca y sigo.
						falta -= boletos[k].second;
						boletos.pop_back();
						k--;
					}
				}
				///ya updatie todo en el caso de gente que baja.
			}
			
			///updateo la estacion vieja.
			eP = eA;
			precio %= mod;
		}
//cout<<"costosintrampa, precio=: "<<costoSinTrampa<<" "<<precio<<endl;
		tint res = costoSinTrampa - precio;
		res %= mod;
		res += mod;
		res %= mod;
		cout<<"Case #"<<tc<<": "<<res<<endl;
	}
    return 0;
}
