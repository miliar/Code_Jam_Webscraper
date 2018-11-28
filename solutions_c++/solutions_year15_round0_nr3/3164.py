#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int mat[5][5];
void start()
{
	int mataux[5][5]= {
	0, 0, 0, 0, 0,
	0, 1, 2, 3, 4,
	0, 2, -1, 4, -3,
	0, 3, -4, -1, 2,
	0, 4, 3, -2, -1
	};
	for(int i=0; i<5; i++)
		for(int j=0; j<5; j++)
			mat[i][j]=mataux[i][j];
}
int abs(int a)
{
	if(a>0)return a;
	else return -a;
}

int operate(int a, int b)
{
	int res=mat[abs(a)][abs(b)];
	if((a>0 && b>0) || (a<0 && b<0))return res;
	else return -res;
}
int disoperate(int a, int tot)
{
	int res;
	for(int i=1; i<5; i++)
	{
		if(abs(tot)==abs(operate(a, i)))
		{
			res=i;
			break;
		}
	}
	return (operate(a, res)==tot)?res:-res;
}
int parse_digit(char digit) {
    return (digit - 'i')+2;
}
bool proc(string cadena)
{
	if(cadena.length()<3)return false;
	int tot=1;
	for(int l=0; l<cadena.length(); l++)
	{
		tot=operate(tot, parse_digit(cadena[l]));
	}
	int toti=parse_digit(cadena[0]), totj=parse_digit(cadena[1]),
		totk=disoperate(operate(parse_digit(cadena[0]),parse_digit(cadena[1])),tot);
	int acumi=1, acumj=1, acumk=1;
	for(unsigned int i=0; i<cadena.length(); i++)
	{
		acumi=operate(acumi, parse_digit(cadena[i]));
		if(acumi==2)
		{
			acumj=1;
			for(unsigned int j=i+1; j<cadena.length(); j++)
			{
				acumj=operate(acumj, parse_digit(cadena[j]));
				if(acumj==3)
				{
					totk=disoperate(operate(acumi,acumj),tot);
					if(totk==4)return true;
				}
			}
		}
	}
	return false;
}
int main()
{
	start();
	ifstream input;
	input.open("C-small-attempt1.in");
	ofstream output;
	output.open("outbb.txt");
	int casos;
	int longitud, rep;
	input>>casos;
	for(int i=0; i<casos; i++)
	{
		cout<<i<<endl;
		input>>longitud>>rep;
		string cadena, aux="";
		input>>cadena;
		for(int j=0; j<rep; j++)aux+=cadena;
		output<<"Case #"<<i+1<<": "<<(proc(aux)? "YES":"NO")<<endl;
	}
	input.close();
	output.close();
	return 0;
}