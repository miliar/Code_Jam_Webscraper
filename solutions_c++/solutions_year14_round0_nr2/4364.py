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

int main(void)
{
	int a;
	scanf(" %d",&a);
	for(int t = 1; t <= a; t++){
		scanf(" %lf %lf %lf",&C,&F,&X);
	//	printf("%f %f %f\n",C,F,X);
		double minule = 0;
		double najm = X/((double)2);
		double aktual;
		cout<<"Case #"<<t<<": ";
		for(int i = 0; i <= X; i++){
			aktual = minule + (C/(((double)2) + F * ((double) (i))));
			if(aktual + X / (((double)2) + F * ((double) (i + 1))) > najm){
				printf("%.7lf", najm);
				break;
			}
			else{
				najm = aktual + X / (((double)2) + F * ((double) (i + 1)));
			}
			minule = aktual;
		}
		cout<<endl;
	}
    return 0;
}