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
	ios_base::sync_with_stdio(0);
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
	int t;//liczba przypadkow
	wejscie>>t;
	int kwadrat[4][4];//[numer_wiersza][numer_kolumny]
	int odpowiedz;
	FOR(numer_test_case,1,t){
		wejscie>>odpowiedz;
		REP(x,4)//wiersze
		REP(y,4)
		wejscie>>kwadrat[x][y];
		odpowiedz--;
		vector<int> mozliwosci,mozliwosci_2;
		mozliwosci.reserve(4);
		REP(x,4) mozliwosci.PB(kwadrat[odpowiedz][x]);
		
		wejscie>>odpowiedz;
		REP(x,4)//wiersze
		REP(y,4)
		wejscie>>kwadrat[x][y];
		odpowiedz--;
		REP(x,4){
			bool znalezione=0;
			REP(y,4) if(mozliwosci[y]==kwadrat[odpowiedz][x]) znalezione=1;
			if(znalezione) mozliwosci_2.PB(kwadrat[odpowiedz][x]);
		}
		wyjscie<<"Case #"<<numer_test_case<<": ";
		if(mozliwosci_2.size()>1) wyjscie<<"Bad magician!"<<endl;
		else if(mozliwosci_2.empty()) wyjscie<<"Volunteer cheated!"<<endl;
		else wyjscie<<mozliwosci_2[0]<<endl;
	}
	
	
    
	return 0;
}
