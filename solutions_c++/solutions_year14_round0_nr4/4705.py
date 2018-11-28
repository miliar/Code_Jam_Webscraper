#include <iostream>
#include <set>

using namespace std;

#define EPSILON 0.00000001

bool alessthanb(double a, double b){
	double diff = a-b;
	return (-diff >= EPSILON);
}


int main(){
	ios::sync_with_stdio(false);

	int testCases,blocks,decScore=0,warScore=0,counter=1;
	set<double> naomi,ken;
	set<double> :: iterator nIt,keIt;
	double aux;

	cin >> testCases;
	while(testCases-- > 0){
		cin >> blocks;

		for(int i = 0 ; i < blocks ; i++){
			cin >> aux;

			naomi.insert(aux);
		}

		for(int i = 0 ; i < blocks ; i++){
			cin >> aux;

			ken.insert(aux);
		}

		nIt = naomi.begin();
		keIt = ken.begin();
		for(int i = 0 ; i < blocks ; i++){
			if(alessthanb(*nIt,*keIt)){
				nIt++;
			}else{
				decScore++;
				keIt++;
				nIt++;
			}

		}

		nIt = naomi.begin();
		keIt = ken.begin();
		for(int i = 0 ; i < blocks ; i++){
			if(alessthanb(*keIt,*nIt)){
				keIt++;
			}else{
				warScore++;
				keIt++;
				nIt++;
			}

		}
		cout << "Case #" << counter++ << ": " << decScore << " " << blocks-warScore << endl;
		decScore=0;
		warScore=0;
		naomi.clear();
		ken.clear();
	}

	return 0;
}