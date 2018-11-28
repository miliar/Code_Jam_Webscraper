#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <cstring>

using namespace std;
void troca(char c[], int pos);
int tudomais(char str[], int tam);

int main(){

    FILE *fin = freopen("B-small-attempt0.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-small-attempt0.out", "w", stdout);


	int T;
	cin >> T;

	for (int t=0; t<T; t++){
        int  cont=0;
        char s[100];
        cin>>s;
        int tam = strlen(s);

        int i, j;
        while(tudomais(s, tam)==0){
            for (i=1; i<tam; i++){
                if (s[i]!=s[0]) break;
            }
            for (j=0; j<i; j++){
                troca(s, j);
            }
            cont++;
        }
        cout << "Case #" << t+1 << ": " << cont << endl;

	}
	return 0;
}

void troca(char c[], int pos){
    if (c[pos]=='+') c[pos]='-';
    else c[pos]='+';
}

int tudomais(char str[], int tam){
    for(int i=0; i<tam; i++){
        if (str[i]=='-') return 0;
    }
    return 1;
}
