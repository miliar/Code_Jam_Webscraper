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

int main(void)
{
	int a;
	cin>>a;
	for(int t = 1; t <= a; t++){
		int kde1, kde2, ci, pocet = 0, vys = 0;
		cin>>kde1;
		multiset<int> cisla;
		for(int i = 1; i <= 4; i++){
			for(int j = 1; j <= 4; j++){
				cin>>ci;
				if(i == kde1)
					cisla.insert(ci);
			}
		}
		cin>>kde2;
		for(int i = 1; i <= 4; i++){
			for(int j = 1; j <= 4; j++){
				cin>>ci;
				if(i == kde2 && cisla.find(ci) != cisla.end()){
					pocet++;
					vys = ci;
				}
			}
		}
		cout<<"Case #"<<t<<": ";
		if(!pocet)
			cout<<"Volunteer cheated!";
		else if (pocet == 1)
			cout<<vys;
		else
			cout<<"Bad magician!";
		cout<<endl;
	}
    return 0;
}