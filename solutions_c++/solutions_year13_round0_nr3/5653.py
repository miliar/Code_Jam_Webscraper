#include <iostream>
#include <cmath>

using namespace std;

inline int isOk(int x){
	if(x%10 == 0 || x%10==1  || x%10==4 || x%10== 5 || x%10== 6 || x%10== 9)
		return true;
	else
		return false;
}

bool isPalindrome(int nb){
	int nbChiffres = 1 + (int)log10(abs(nb));

	for(int chiffre = 0; chiffre < nbChiffres/2 + 1; chiffre++){
		int x = (nb/((int)pow(10, chiffre)))%10;
		int y = (nb/((int)pow(10, nbChiffres - chiffre - 1)))%10;

		if(x != y){
			return false;
		}
	}

	return true;
}

int main(void){
	int nbCases;
	cin >> nbCases;

	int a, b;
	int nbChiffres;

	int *cases = new int[nbCases];
	fill(cases, cases + nbCases, 0);

	for(int caseIndex = 0; caseIndex < nbCases; caseIndex++){
		cin >> a;
		cin >> b;

		for(int nb = a; nb <= b; nb++){
			if(!isOk(nb))
				continue;

			if(fmod(sqrt(nb), 1) != 0)
				continue;

			if(isPalindrome(nb) && isPalindrome((int)sqrt(nb)))
				cases[caseIndex]++;
		}
	}

	for(int caseIndex = 0; caseIndex < nbCases; caseIndex++){
		cout << "Case #" << caseIndex + 1 << ": " << cases[caseIndex] << endl;
	}

	delete [] cases;

	return 0;
}