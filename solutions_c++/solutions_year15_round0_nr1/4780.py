#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int proc(int smax, int list[1001])
{
	int acum=list[0];
	int amigos=0;
	for(int i=1; i<=smax; i++)
	{
		if(acum<i && list[i]!=0)
		{
			amigos+=(i-acum);
			acum+=(i-acum);
		}
		acum+=list[i];
	}
	return amigos;
}
int parse_digit(char digit) {
    return digit - '0';
}

int main()
{
	ifstream input;
	input.open("A-large.in");
	ofstream output;
	output.open("out.txt");
	int casos;
	int smax;
	int lista[1001];
	input>>casos;
	for(int i=0; i<casos; i++)
	{
		input>>smax;
		char c;
		input.get(c);
		for(int j=0; j<=smax; j++)
		{
			input.get(c);
			lista[j]=parse_digit(c);
		}
		output<<"Case #"<<i+1<<": "<<proc(smax, lista)<<endl;
	}
	input.close();
	output.close();
	return 0;
}