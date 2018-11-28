#include <iostream>
#include <list>
#include <algorithm>
#include <fstream>
using namespace std;
void cufru( unsigned int  chuslo, list <unsigned int>* num)
{
	for (int i=0;chuslo>0;i++)
	{
	num->push_back(chuslo%10);
	chuslo=chuslo/10;
	}
}
int main()
{
	list <unsigned int> num2;
	list <unsigned int> num;
	bool n=true;
ifstream infile("A-large.in");
 int na = 0; 
 int m=1;
	unsigned int prognoz[105]; 
	while (infile >> prognoz[na]) ++na;
	  for (int c = 0; c < na; ++c) cout << prognoz[c] << ' ';
	  ofstream f;
	  f.open("out.txt");
	for (int i=0;i<10;i++)
		num2.push_back(i);
	unsigned int k;
		
	
for(int j=1;j<101;j++)
{	
for(int i=1;i<100;i++)
{k=i*prognoz[j];
cufru(k,&num);
num.sort();
num.unique();
if(num==num2)
	{f << "Case #"; 
	f << m ;
	f << ": ";
	f<< k ;
	f<< endl;
break;
}
}
if(num!=num2)
	{
		f << "Case #";
		f << m;
		f << ": ";
f << "Insomnia" ;
f << endl;
}
num.clear();
m++;
}

	
system("pause");
return 0;
}