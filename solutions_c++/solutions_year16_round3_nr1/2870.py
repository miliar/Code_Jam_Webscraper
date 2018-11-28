#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
#include <string>
#include <map>
#include <utility>

#define ff first
#define ss second

using namespace std;

vector< pair<int,int> > partidos;

bool func (pair<int,int> i, pair<int,int> j) { return (i.ff >= j.ff); }

int main(){
	int casos;
	int N;
	scanf("%d",&casos);
	int aux1;
	for (int c = 1; c <= casos; c++){

		scanf("%d",&N);

		aux1 = 0;
		partidos.clear();
		for (int i = 0; i < N; i++){
			scanf("%d",&aux1);
			partidos.push_back(make_pair(aux1,i));
		}

		sort(partidos.begin(),partidos.end(),func);

		printf("Case #%d: ",c);


		while(partidos[0].ff != 0){
//			printf("%d %c\n",partidos[0].ff,partidos[0].ss + 'A');
			if (partidos[0].ff == partidos[1] .ff and partidos[2].ff != 1){
				printf("%c%c ",partidos[0].ss + 'A',partidos[1].ss + 'A');
				partidos[0].ff -= 1;
				partidos[1].ff -= 1;
			}
			else{
				printf("%c ",partidos[0].ss + 'A');
				partidos[0].ff -= 1;
			}

			sort(partidos.begin(),partidos.end(),func);
		}

		printf("\n");
	}
}