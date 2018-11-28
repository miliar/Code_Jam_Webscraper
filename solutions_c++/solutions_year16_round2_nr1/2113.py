#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
#include <string>
#include <map>


using namespace std;

int letras[28];
vector<string> nombres;
map <string,int> real;

int main(){
	int casos;
	scanf("%d",&casos);
	string s;
	nombres.push_back("ZERO");
	nombres.push_back("TWO");
	nombres.push_back("EIGHT");
	nombres.push_back("FOUR");
	nombres.push_back("THREE");
	nombres.push_back("SIX");
	nombres.push_back("FIVE");
	nombres.push_back("SEVEN");
	nombres.push_back("ONE");
	nombres.push_back("NINE");

	real["ONE"] = 1;
	real["TWO"] = 2;
	real["THREE"]= 3;
	real["FOUR"]= 4;
	real["FIVE"] =  5;
	real["SIX"] = 6;
	real["SEVEN"] = 7;
	real["EIGHT"] = 8;
	real["NINE"] = 9;
	real["ZERO"] = 0;
	vector<string> numero;
	vector<int> sol;
	bool sigo;

	for (int c = 1; c <= casos; c++){

		cin >> s;

		memset(letras,0,sizeof(letras));
		numero.clear();

		for (int i = 0 ; i < s.size();i ++){
			letras[s[i]-'A'] += 1;
		}


		for (int i = 0; i < 10;i ++){

			while(true){
				sigo = true;

				for (int j = 0; j < nombres[i].size();j++){
					if (letras[nombres[i][j] - 'A'] == 0){
						sigo = false;
						break;
					}
				}

				if (sigo == false){
					break;
				}

				numero.push_back(nombres[i]);
				

				for (int j = 0; j < nombres[i].size();j++){
					letras[nombres[i][j] - 'A'] -= 1;
				}
			}

		}

		sol.clear();
		for (int i = 0; i < numero.size();i ++){
			sol.push_back(real[numero[i]]);
		}


		sort(sol.begin(),sol.end());


		printf("Case #%d: ",c);

		for (int i = 0; i < numero.size();i ++){
			cout << sol[i];
		}
		cout << endl;
	}
}