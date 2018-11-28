#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <set>
#include <fstream>
using namespace std;

typedef vector<int> VI;
typedef long long LL;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
int main (int argc, char * const argv[]) {
	//strategia
	/*
	nie ma remisow
	w War Ken wybiera najmniejszy blok z tych ktore mu dadza wygrana,
	jesli nie ma takiego, to wybiera najmniejsza wartosc ze wszystkich, ktore ma
	 
	w War optymalna strategia dla Naomi to branie wszystkich dopoki sie da, jak ona ma 7, 7 a ken 8 to posiweca jedno 7 hmm... 
	w War optymalna Naomi - jedzdie od najwiekszego do najmniejszego!!! - chyba to
	w War optymalna Naomi - jak moze wzac to bierze a jak nie to oddaje najmniejszy/najwiekszy??
	 
	w deceitful war to jedzie po kolei od najwiekszego jego tak zeby go oszukac, i zeby wyjal swojego najwiekszego, przy jej najmniejszym
	
	!! w deceitful bierzemy nasz najmniejszy z tych, ktore moga zbic jego najmniejszego i mowimy mu ze ma wartosc 1!!! - optymalna strategia!
	w ten sposob on wyciagnie swojego najmnejszzego
	 potem bierzemy naszego najmniejszego i mowimy ze jest tylko ciut mniejszy od jego najwiekszego, w ten sposob on musi oddac swojego najwiekszego i moze sie bedzie dalo wziac po raz kolejny cos?? czy nie???
	 ^^^^ nie ma chyba takiej potrzeby
	w momencie, w ktorym nie mamy takiego najmnejszego juz nie da sie nic zrobic
	 
	*/

	fstream wejscie;
	
	wejscie.open("A-small-practice.in",ios::in);
	if( wejscie.good() == true )
	{
		cout << "Uzyskano dostep do wejscia!" << std::endl;
	} else cout << "Dostep do pliku wejscia zostal zabroniony!" << endl;
	
	fstream wyjscie;
	wyjscie.open("odpowiedziii.txt", ios::out);
	if( wyjscie.good() == true )
	{
		cout << "Uzyskano dostep do wyjscia!" << std::endl;
	} else cout << "Dostep do pliku wyjscia zostal zabroniony!" << endl;
	int t;
	int n;//num of blocks
	double block;
	wejscie>>t;
	FOR(num_of_test_case,1,t){
		vector<double> naomi,ken;
		wejscie>>n;
		naomi.resize(n);
		ken.resize(n);
		REP(x,n) wejscie>>naomi[x];
	
		REP(x,n) wejscie>>ken[x];
		
		sort(ALL(naomi));
		sort(ALL(ken));
		int war=0, deceitful=0;
		int wskaznik_naomi=0;
		FOREACH(it,ken){
		//szukam pierwszego wiekszego od *it w naomi
			FOR(it2,wskaznik_naomi,naomi.size()-1){
				if(naomi[it2]>*it){
					deceitful++;
					wskaznik_naomi=it2+1;
					break;
				}
			}
		}
		FORD(pozycja_naomi,naomi.size()-1,0){
			if(ken[ken.size()-1]>naomi[pozycja_naomi]){
				//ken=vector<double>(ken.begin(),ken.begin()+ken.size()-1);
				ken=vector<double>(ken.begin(),--ken.end());
			}
			else {
				war++;
				ken=vector<double>(ken.begin()+1,ken.end());
			}

		}
		
		wyjscie<<"Case #"<<num_of_test_case<<": "<<deceitful<<" "<<war<<endl;
	}

	return 0;
}
