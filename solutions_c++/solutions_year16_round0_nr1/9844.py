#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>

using namespace std;

int viutudo(int num[]);

int main(){
    FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);

	int t;
	cin >> t;

	for (int i=0; i<t; i++){
        unsigned int n, n2;
        int cont=0;
        int num[10]={0}, vt=false;
        cin >> n;
        n2=n;
        if (n==0){
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
            continue;
        }
        while(!vt){
            do{
                num[n2%10] = true;
                n2/=10;
            }while(n2!=0);

            if(viutudo(num)==1){
                vt=true;
                cout << "Case #" << i+1 << ": " << n*cont << endl;
            }
            else{
                n2 = n*(++cont);
            }
        }
	}
	return 0;
}

int viutudo(int num[]){
    for (int i=0; i<10; i++){
        if (num[i] == 0) return 0;
    }
    return 1;
}
