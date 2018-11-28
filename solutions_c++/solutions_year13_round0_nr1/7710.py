#include <cstdio>
char tab[4][4];

bool czySaPuste(){
	for(int i=0;i<=3;i++) {
		for(int j=0;j<=3;j++)
			if (tab[i][j]=='.')
				return true;
		
	}

	return false;
}

bool sprawdzSkos1(char zaw){
	for(int i=0;i<=3;i++) {
		if(tab[i][i]!=zaw && tab[i][i]!='T')
			return false;
	}	
	return true;
}

bool sprawdzSkos2(char zaw){
	for(int i=0;i<=3;i++) {
		if(tab[3-i][i]!=zaw && tab[3-	i][i]!='T')
			return false;

	}
	return true;
}

bool sprawdzWiersz(char zaw, int k){
	for(int i=0;i<=3;i++) {
		if(tab[k][i]!=zaw && tab[k][i]!='T')
			return false;

	}
	return true;
}


bool sprawdzKolumne(char zaw, int k){

	for(int i=0;i<=3;i++) {
		if(tab[i][k]!=zaw && tab[i][k]!='T')
			return false;

	}
	return true;



}

bool czyWygral(char zaw){
	for (int i=0;i<=3;i++)
		if(sprawdzWiersz(zaw, i)==true)
			return true;
	for (int i=0;i<=3;i++)
		if(sprawdzKolumne(zaw, i)==true)
			return true;
	
	if (sprawdzSkos1(zaw))	
		return true;
	if (sprawdzSkos2(zaw))
		return true;	
	return false;
}

void solve(int x){
	for (int i=0;i<=3;i++)
		scanf("%s",tab[i]);
	
	if(czyWygral('X'))
		printf("Case #%d: X won\n", x);
	else if(czyWygral('O'))
		printf("Case #%d: O won\n", x);
	else if(czySaPuste())
		printf("Case #%d: Game has not completed\n", x);
	else
		printf("Case #%d: Draw\n", x);
}

int main() {

	int a;
	scanf("%d", &a);
	for (int i=0;i<a;i++)
		solve(i+1); 
}
