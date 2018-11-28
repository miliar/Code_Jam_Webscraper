#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int T[100];
int r,p,s;
vector <char> Res;

vector <char> Sumuj(vector <char> V1,vector <char> V2){
	int i;
	vector <char> V;
	for(i=0; i<V1.size(); i++) V.push_back(V1[i]);
	for(i=0; i<V2.size(); i++) V.push_back(V2[i]);
	return V;
}

vector <char> Try(int n,char typ){
	int i;
	vector <char> V1,V2;
	if(n==0) {
		V1.push_back(typ);
		return V1;
	}
	if(typ == 'P') {
		V1 = Try(n-1,typ);
		V2 = Try(n-1, 'R');
	}
	if(typ == 'R') {
		V1 = Try(n-1,typ);
		V2 = Try(n-1, 'S');
	}
	if(typ == 'S') {
		V1 = Try(n-1,typ);
		V2 = Try(n-1, 'P');
	}
	if(V1<V2) return Sumuj(V1,V2);
	else return Sumuj(V2,V1);
}

bool OK(){
	int i,a,b,c;
	a = b = c = 0;
	for(i=0; i<Res.size(); i++){
		if(Res[i] == 'P') a++;
		if(Res[i] == 'R') b++;
		if(Res[i] == 'S') c++;
	}
	if(a==p && b == r && c == s) return true;
	return false;
}

void Wypisz(int j){
	int i;
	printf("Case #%d: ", j+1);
	for(i=0; i<Res.size(); i++){
		printf("%c", Res[i]);
	}
	printf("\n");
}

int main(){
	int n,t,i;
	scanf("%d", &t);
	for(i=0; i<t; i++){
		scanf("%d%d%d%d", &n,&r,&p,&s);
		Res = Try(n,'P');
		if( OK() ){
			Wypisz(i);
			continue;
		}
		Res = Try(n,'R');
		if( OK() ){
			Wypisz(i);
			continue;
		}
		Res = Try(n,'S');
		if( OK() ){
			Wypisz(i);
			continue;
		}
		printf("Case #%d: IMPOSSIBLE\n", i+1);
	}
	return 0;
}
