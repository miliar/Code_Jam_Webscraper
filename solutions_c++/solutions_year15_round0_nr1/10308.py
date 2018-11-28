#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include <errno.h>
using namespace std;
/*GLOBAL*/
ifstream ifs;
ofstream ofs;
string s;
char c;
int T, S, ris, count, app;
int *audience;

/*FUNCTION*/
void stampa(int cas){
	ofs.open("output.txt", ios_base::app);	
	ofs << "Case #" <<cas+1<< ": " << ris  <<endl;
	ofs.close();
	return;
}

void elabora(int cas){
	ris=0;
	count=0;
	for(int j=0; j<S+1; j++){
		for(int k=0; k<j; k++){
			count += audience[k];
		}
		if(count+ris < j)	
			ris += j-(count+ris);
		count=0;
	}
	stampa(cas);
}

int main(){
	ifs.open("prova_rD_a.in");
    if(!ifs){
		cout<<"file non esiste!\n";
		return -1;
	}
	/*leggo numero di casi*/
	ifs >> T;
	for(int i =0; i<T; i++){
		ifs >> S;
		audience = new int[S+1];
		ifs >> app;
		for(int j=0; j<S+1; j++){
			audience[S-j]= app%10;
			app = app/10;
		}
		elabora(i);
		delete audience;
	}			
	return 0;
}
