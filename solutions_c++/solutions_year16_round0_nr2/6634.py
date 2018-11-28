#include <iostream>
#include <fstream>
using namespace std;
string comprimir(string cadena)
{
	for(int i=1;i<cadena.size();)
	{
		if(cadena[i]==cadena[i-1])
			cadena.erase(i,1);
		else
			i++;
	}
	return cadena;
}
int main()
{
	int cp;
	string cadena;
	ifstream I("B.in");
	ofstream O("B.out");
	I>>cp;
	for(int i=1;i<=cp;i++)
	{
		I>>cadena;
		cadena=comprimir(cadena);
		O<<"Case #"<<i<<": ";
		if(cadena=="+")
		{
			O<<"0"<<endl;
			continue;
		}
		if(cadena=="-")
		{
			O<<"1"<<endl;
			continue;
		}
		if(cadena[0]=='+' and cadena.size()%2==0)
			O<<cadena.size()<<endl;
		if(cadena[0]=='+' and cadena.size()%2==1)
			O<<cadena.size()-1<<endl;
		if(cadena[0]=='-' and cadena.size()%2==0)
			O<<cadena.size()-1<<endl;
		if(cadena[0]=='-' and cadena.size()%2==1)
			O<<cadena.size()<<endl;
		
	}
	return 0;
}