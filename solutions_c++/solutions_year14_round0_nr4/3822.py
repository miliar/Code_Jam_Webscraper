#include <iostream>
#include <cstdlib>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <string>
#include <cstdlib>
#include <set>

#define forn(i,n) for(int i = 0; i < (int)(n); i++)
#define forn1(i,n) for(int i = 1; i <= (int)(n); i++)
#define forsn(i,s,n) for(int i = (int)(s); i < (int)(n); i++)
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)


using namespace std;

int main()
{
	int test, n;
	double aux;
	int war, dwar;
	set <double> nao;
	set <double> ken;
	double naoA[1100];
	double kenA[1100];

	cin >> test;

	forn(t, test){
		cin >> n;
		forn(i,n){
 			cin >> aux;
			naoA[i] = aux;
			nao.insert(aux);
		}
		forn(i,n){
			cin >> aux;
			kenA[i] = aux;
			ken.insert(aux);
		}

		// War
		std::set<double>::iterator it;
		std::set<double>::iterator pos;
		war = 0;

		it = nao.begin();
		forn(i,n){
			double val = *it;
			pos = upper_bound(ken.begin(), ken.end(), val);
			if(pos != ken.end()){
				ken.erase(pos);
			}
			else{
				war++;
				ken.erase(ken.begin());
			}			
			it++;
		}
		
		nao.clear();
		ken.clear();

		//Deceitful War
		
		dwar = 0;

		sort(naoA, naoA + n);
		sort(kenA, kenA + n);
		
		int k = 0;
		forn(i,n){
			if(naoA[i] > kenA[k]){
				dwar++;
				k++;
			}
		}

		cout << "Case #" << (t+1) << ": " << dwar << " " << war << endl;
	}

	return 0;
}
