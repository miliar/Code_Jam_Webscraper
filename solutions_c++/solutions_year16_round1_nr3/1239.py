#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
#include <stack>

using namespace std;


int grafo[1001];
vector< vector < int > > grafo2;

int princ;
int curr[1001];
int esta[1001];
int N;

int longCycle(int i,int current ,int count){
//	cout << i << " ";
	if (i == princ and count != 1){
//		cout << "Llegue aqui con" << count << endl;
		return count - 1;
	}
	curr[current] = i;

	if (current == 0){
		return longCycle(grafo[i],current+1,count+1);
	}
	
	if (curr[current-1] == grafo[i]){
		//cout << " i  es = " << i << " anterior es" << curr[current-1] << endl;
		int aux = count;
		bool puedo = true;
		for (int j = 1; j <= N; j++){
			puedo = true;

			for (int k = 1; k < current; k++){
				if (j == curr[k] or j == i){
					puedo = false;
					break;
				}
			}

			if (puedo){
				aux = max(aux,longCycle(j,current+1, count+1));
//				cout << endl;
			}
			//cout << "retorne " << aux << endl;
		}
		puedo = true;
		return aux;
	}
	else{
		bool puedo = true;
		for (int k = 1; k < current; k++){
			if (grafo[i] == curr[k]){
				puedo = false;
				break;
			}
		}
		if (puedo){
			return longCycle(grafo[i],current+1,count+1);
		}
		else{
			return 0;
		}
	}

	return 0;

}


int main(){
	int Caso;
	cin >> Caso;
	int sol;
	int aux2;
	int aux;
	for (int c = 1; c <= Caso; c++){

		cin >> N;

		grafo2.clear();
		grafo2.resize(N+1);
		for (int i = 1; i <= N ; i++){
			cin >> aux;
			grafo[i] = aux;
			grafo2[aux].push_back(i);
		}

		sol = 0;
		for (int i = 1; i <= N ; i++){
			memset(curr,0,sizeof(curr));
			princ = i;
			aux2 = longCycle(i,0,1);
//			cout << endl;
			sol = max(aux2,sol);
		}

		cout << "Case #" << c << ": " << sol << endl;
	}
}