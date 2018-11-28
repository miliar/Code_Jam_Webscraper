#include <stdio.h>
#include <string.h>

int casos,r,n,cuentas[103][103],cuentass[100],indice[100];
char palabras[100][102];

int min(int x,int y){if(x<y)return x;return y;}
int max(int x,int y){if(x>y)return x;return y;}
int abs(int x){if(x < 0)return -x;return x;}
void lee(){
	int j;
	scanf("%d",&n);
	palabras[0][0] = getchar();
	for(int i = 0;i<n;i++){
		j = 0;
		palabras[i][j] = getchar();
		while(palabras[i][j++] != '\n'){
			palabras[i][j] = getchar();
		}
	}
}
char checaiguales(){
	for(int i = 0;i<n;i++)
		if(palabras[i][indice[i]] != palabras[0][indice[0]])
			return '0';
	return palabras[0][indice[0]];
}
int cuentaLetras(){
	int cuenta,mini=1000,maxi=-1;
	for(int i = 0;i < n;i++){
		cuenta=1;
		while(palabras[i][indice[i]] == palabras[i][indice[i]+1]){
			cuenta++;indice[i]++;
		}
		mini = min(mini,cuenta);
		maxi = max(maxi,cuenta);
		cuentass[i] = cuenta;
		indice[i]++;
	}
	for(int i = 0;i < n;i++){
		for(int j = mini;j <= maxi;j++){
			cuentas[j][i] = abs(cuentass[i]-j);
			if(i >0) cuentas[j][i] += cuentas[j][i-1];
		}
	}
	int caca = 1000;
	for(int i = mini;i<=maxi;i++) caca = min(caca,cuentas[i][n-1]);
	return caca;
}
void reset(){
	r = 0;
	memset(indice,0,sizeof(indice));
}
int main(){
	freopen("in.txt","r",stdin);
	char c;
	scanf("%d",&casos);
	for(int i = 1;i<=casos;i++){
		lee();
		c = checaiguales();
		while(c >= 'a' && c <= 'z'){
			r += cuentaLetras();
			c = checaiguales();
		}
		printf("Case #%d: ",i);
		if(c == '0') printf("Fegla Won\n");
		else printf("%d\n",r);
		reset();
	}
	return 0;
}
