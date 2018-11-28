#include <iostream>
#include <fstream>
using namespace std;

int potenza(const int base,const int esp)
{
	int ris= 1; // da ritornare
	for(int c=1; c<=esp; c++)
		ris= ris*base;
	return ris;
}// POST: return base, che 

void test(int K,int C,int S, ofstream &out)
{
	// int lung= potenza(K,C);
	for(int i=0; i<K; i++)
	{
		// out<< 1+ K*i+i <<' ';
		out<<i+1<<' ';
	}
	out<<endl;
	
}





main(){

ifstream in("input");
ofstream out("output");
if(in&&out)
{
	// T #test
	// K #tiles of original sequence
	// C complexity
	// S #students
	
	int T; in>>T;
	int  K,C,S;
	
	for(int i=1; i<=T; i++)
	{
		in>>K >>C >>S;
		out<<"Case #"<<i <<": ";
		test(K,C,S,out);
	}
	
}
else cout<<"errore files\n";


}
