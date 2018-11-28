#include <iostream>
#include <fstream>
using namespace std;
ifstream fin ("A-large.in");
ofstream fout ("output.txt");

bool visitati[10];
int T, N;

bool controlla (){
	//fout<<"sono in controlla"<<endl;
	//for (int y=0; y<10; y++) fout<<visitati[y]<<" ";
	//fout<<endl;
	for (int y=0; y<10; y++) if (visitati[y]==0) return false;
	return true;
	}

void conta (int numero){
	if (numero==0) fout<<"INSOMNIA";
else{
	bool tutto = 0;
	int moltip = 1;
	int num;
	int a = num = numero;
	for (int x=1; !tutto; x++){
	num = numero * x;
	moltip=1;
	for (a=(num/moltip)%10; num/moltip!=0; a = (num/moltip)%10) {
		//fout<<"sono qui "<<a<<endl;
		if (visitati[a]==0){
		visitati[a]=1;
		//fout<<x<<": ";
		tutto= controlla();
			}
		moltip=moltip*10;
		}
	if (tutto) {
				fout<<num;
				break;
				}
	}
	}
	return;
	}

int main(){
	fin>>T;
	for (int i=0; i<T ; i++){
		for (int j=0; j<10; j++) visitati[j]=0;
		fin>>N;
		fout<<"Case #"<<i+1<<": ";
		conta (N);
		fout<<endl;
		}
	return 0;
	}
