#include <iostream>
#include <cstdlib>
#include<fstream> 
#include<cassert>  
#include<algorithm>
#define MAXN 100000
using namespace std;
int N;
int v[MAXN];
int visti[]={0,0,0,0,0,0,0,0,0,0};
void reset() {
	for(int i=0;i<10;i++)
		visti[i]=0;
}

void trovacifre(int numero){
	int cifra;
	while(numero>0) {
		cifra=numero%10;
		numero=numero/10;
		visti[cifra]=1;
	}
}


int main()
{
	ifstream in("input.txt");  
	assert(in);               
	ofstream out("output.txt");
	in>>N;  
	int numero;
	int x;
	for(int i=0;i<N;i++){
		in>>v[i];
		if(v[i]==0) {
			out<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}
		else{
			x=1;
			reset();
			
			while(visti[0]+visti[1]+visti[2]+visti[3]+visti[4]+visti[5]+visti[6]+visti[7]+visti[8]+visti[9]<10) {
				numero=x*v[i];
				trovacifre(numero);
				x++;
			}
			out<<"Case #"<<i+1<<": "<<numero<<endl;
		}
	}
	
	
	
	return 0;
}

