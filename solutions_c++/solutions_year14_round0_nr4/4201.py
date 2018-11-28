#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
using namespace std;
unsigned const int PRIME = 100000009;
unsigned int POWER = 47;
char vzor[1002];
char kmp[1002];
char text[10002];
int dynamika[1002];
int Ndynamika[1002];
int i,j,k,n,m,K,zaciatok;
unsigned int hash2(char * s, int dlzka){
    unsigned int h = 0;
    while(dlzka--){
        h*=POWER;
        h+=(s[dlzka]);
    }
    return h;
}
unsigned int hash3(char * s, int dlzka){
    unsigned int h = 0;
    while(dlzka--){
        h*=POWER;
        h+=(s[0]);
        s=s+1001;
    }
    return h;
}
int max(int a, int b){
    if(a>=b) return a;
    return b;
}
int min(int a, int b){
    if(a<=b) return a;
    return b;
}

vector<int> cisla1, cisla2;

int CONST = -1000000001;
double C = 5, F = 5, X = 5;
int N;
		vector<double> Naomi, Ken;

bool otestuj(int kde){
	if(kde == N)
		return true;
	for(int i = 0; i < N - kde; i++){
		if(Naomi[N - i - 1] < Ken[N - kde - 1 - i])
			return false;
	}
	return true;
}

int main(void)
{
	int a;
	scanf(" %d",&a);
	for(int t = 1; t <= a; t++){
		scanf("%d",&N);
		Naomi.clear();
		Ken.clear();
		for(int i = 0; i < N; i++){
			scanf(" %lf",&C);
			Naomi.push_back(C);
		}
		for(int i = 0; i < N; i++){
			scanf(" %lf",&C);
			Ken.push_back(C);
		}
		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());
		int aktualK = 0;
		int mozO = 0;
		for(int i = 0; i < N; i++){
			while(aktualK < N && Ken[aktualK] < Naomi[i]){
				aktualK++;
			}
			if(aktualK != N){
				mozO++;
				aktualK++;
			}
			else 
				break;
		}
		mozO = N - mozO;

		int mozP = 0;
		for(int i = 0; i <= N; i++){
			if(otestuj(i)){
				mozP = N - i;
				break;
			}

		}

		cout<<"Case #"<<t<<": ";
		cout<<mozP<<" "<<mozO;
		cout<<endl;
	}
    return 0;
}