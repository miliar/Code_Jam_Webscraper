#include <iostream>
#include <cmath>

using namespace std;


int main () {
int n=0, m=0, cases=0, htemp=0;
int trawnik[100][100];
int trawnikbuf[100][100];

cin >> cases;
for (int g=1; g<(cases+1);) {
//scanf("%d %d\n", &n, &m);
cin >> n >> m;
//printf("%d %d\n", n, m);
for (int i=0; i<n; i++) {
	for (int j=0; j<m; j++)
		cin >> trawnik[i][j];
}


//wypisywanie ina
/*
for (int i=0; i<n; i++) {
	for (int j = 0; j < m; j++)
	{
		cout << trawnik[i][j];
	}
cout << endl;
}
*/

// na chama wszystkie boki tne
for (int i=0; i<n; i++) {
	for (int j = 0; j < m; j++)
	{
		trawnikbuf[i][j] = 200;
	}
}


for (int i=0; i<n; i++) {
	for (int j = 0; j < m; j++){
		if (trawnikbuf[i][j]>trawnik[i][0]) trawnikbuf[i][j]=trawnik[i][0]; 
		if (trawnikbuf[j][i]>trawnik[0][i]) trawnikbuf[j][i]=trawnik[0][i]; 
	}
}



for (int i=0; i<n; i++) {
	for (int j = 0; j < m; j++){
		if (trawnikbuf[i][j]!=trawnik[i][j]) {
//			cout << "Case #" << g << ": NO\n";
			goto n1;
		}
	}
}

cout << "Case #" << g << ": YES\n";
goto koniec;

n1:
// na chama tne pion, dopasowuje poziom
for (int i=0; i<n; i++) {
	for (int j = 0; j < m; j++)
	{
		trawnikbuf[i][j] = 200;
	}
}


for (int j=0; j<m; j++) {
	htemp = 0;
	for (int t=0; t<m; t++) if (trawnik[t][j]>htemp) htemp = trawnik[t][j];
	for (int i = 0; i < n; i++){
		if (trawnikbuf[i][j]>trawnik[0][j]) trawnikbuf[i][j]=htemp; 
	}
}


for (int i=0; i<n; i++) {
	for (int j = 0; j < m; j++){
		if (trawnikbuf[i][j]!=trawnik[i][j]) for (int t=0; t<m; t++) {trawnikbuf[i][t]=trawnik[i][0]; }
	}
}

for (int i=0; i<n; i++) {
	for (int j = 0; j < m; j++){
		if (trawnikbuf[i][j]!=trawnik[i][j]) {
//			cout << "Case #" << g << ": NO\n";
			goto n2;
		}
	}
}



cout << "Case #" << g << ": YES\n";
goto koniec;


n2:
// na chama tne poziom, dopasowuje pion
for (int i=0; i<n; i++) {
	for (int j = 0; j < m; j++)
	{
		trawnikbuf[i][j] = 200;
	}
}



for (int i=0; i<n; i++) {
	htemp = 0;
	for (int t=0; t<m; t++) if (trawnik[i][t]>htemp) htemp = trawnik[i][t];
	for (int j = 0; j < m; j++){
		if (trawnikbuf[i][j]>trawnik[i][0]) trawnikbuf[i][j]=htemp;
//		printf("%d %d\n", i, j); 
	}
}


/*
for (int i=0; i<n; i++) {
	for (int j = 0; j < m; j++){
		if (trawnikbuf[i][j]>trawnik[i][0]) trawnikbuf[i][j]=trawnik[i][0]; 
	}
}
*/

for (int i=0; i<n; i++) {
	for (int j = 0; j < m; j++){
		if (trawnikbuf[i][j]!=trawnik[i][j]) for (int t=0; t<n; t++) {trawnikbuf[t][j]=trawnik[0][j]; }
	}
}


for (int i=0; i<n; i++) {
	for (int j = 0; j < m; j++){
		if (trawnikbuf[i][j]!=trawnik[i][j]) {
			cout << "Case #" << g << ": NO\n";
			goto koniec;
		}
	}
}

cout << "Case #" << g << ": YES\n";
goto koniec;















koniec:
/*
cout << endl;
for (int i=0; i<n; i++) {
	for (int j = 0; j < m; j++)
	{
		cout << trawnikbuf[i][j];
	}
cout << endl;
}
*/
g++;
}

return 0;
}
