#include <iostream>
#include <string>
#include <fstream>
using namespace std;

const int N=100;
const string input="A-small-attempt1.txt";

typedef short unsigned int tTabla[N][4][4];

typedef struct{
	tTabla tabla1;
	int elec1[N];
	tTabla tabla2;
	int elec2[N];
}tMagic;

typedef short unsigned int tFila[4];

void cargar(tMagic & magic);
void analizar(tMagic magic, int cont, ofstream & flujo);

int main()
{
	ofstream flujo;
	flujo.open("salida.txt");
	tMagic magic;
	cargar(magic);
	for(int z=0; z<N; z++)analizar(magic,z, flujo);
	flujo.close();
	return 0;
}

void cargar(tMagic & magic)
{
	ifstream flujo;
	flujo.open(input.c_str());
	int auxi;
	if(flujo.is_open())
	{
		flujo>>auxi;
		for(int z=0; z<N; z++)
		{
		flujo>>magic.elec1[z];
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				flujo>>magic.tabla1[z][i][j];
			}
		}
		flujo>>magic.elec2[z];
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				flujo>>magic.tabla2[z][i][j];
			}
		}
		}

	}
	else cout<<"Error"<<endl;
	flujo.close();

}

void analizar(tMagic magic, int cont, ofstream & flujo)
{
	tFila fila1, fila2;
	int pos=0;
	bool ok=false, fail=false, cheat=false;
	for(int i=0; i<4; i++)
	{
		fila1[i]=magic.tabla1[cont][magic.elec1[cont]-1][i];
		fila2[i]=magic.tabla2[cont][magic.elec2[cont]-1][i];
	}
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			if(fila1[i]==fila2[j] && ok==false)
			{
				ok=true;
				pos=i;
			}
			else if(fila1[i]==fila2[j] && ok==true)
			{
				fail=true;
			}
		}
	}
	if(ok==false && fail==false)cheat=true;

	if(cheat==true)flujo<<"Case #"<<cont+1<<": "<<"Volunteer cheated!"<<endl;
	else if(fail==true)flujo<<"Case #"<<cont+1<<": "<<"Bad magician!"<<endl;
	else if(ok==true)flujo<<"Case #"<<cont+1<<": "<<fila1[pos]<<endl;
}