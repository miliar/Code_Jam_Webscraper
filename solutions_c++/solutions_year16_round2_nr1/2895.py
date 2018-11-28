#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

static char digit[10]={'0','1','2','3','4','5','6','7','8','9'};
static int ndigits[10];
static int nz, nw, nu, nx, ng, no, nr, nf, ns, ni;

void decode(string s){
	//clear ndigits
	for(int i=0; i<10; i++){
		ndigits[i]=0;
	}
	nz=0; nw=0; nu=0; nx=0; ng=0; no=0; nr=0; nf=0; ns=0; ni=0;
	//refill ndigits
	int ls=s.length();
	for(int i=0; i<ls; i++)
		switch(s[i]){
			case 'Z': nz++; break;
			case 'W': nw++; break;
			case 'U': nu++; break;
			case 'X': nx++; break;
			case 'G': ng++; break;
			case 'O': no++; break;
			case 'R': nr++; break;
			case 'F': nf++; break;
			case 'S': ns++; break;
			case 'I': ni++; break;
		}
	ndigits[0]=nz; nr-=nz; no-=nz;
	ndigits[2]=nw; no-=nw;
	ndigits[4]=nu; nf-=nu; no-=nu; nr-=nu;
	ndigits[6]=nx; ns-=nx; ni-=nx;
	ndigits[8]=ng; ni-=ng;
	ndigits[1]=no;
	ndigits[3]=nr;
	ndigits[5]=nf; ni-=nf;
	ndigits[7]=ns;
	ndigits[9]=ni;
}

int main(){
	cout<<"launching function main"<<endl;
	ifstream file("A-large.in");
	ofstream outputfile("myoutput.txt");
	int T, phone_num;
	string read_num;
	file>>T;
	getline(file,read_num);	for(int t=0;t<T;t++){
		//read input
		read_num.clear();
		getline(file,read_num);
		//solve
		decode(read_num);
		//write output
		outputfile<<"Case #"<<(t+1)<<": ";
		for(int i=0; i<10; i++){
			for(int k=0; k<ndigits[i]; k++)
				outputfile<<digit[i];
		}
		outputfile<<endl;
	}
	file.close();
	outputfile.close();
}

