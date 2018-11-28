#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <iomanip>
#include <sstream>

using namespace std;

class solve{
	public:
		int P;
		int Q;
		string ans;
		bool impos();
		void run();
		
};

bool solve::impos()
{
	int qdiv = Q;
	
	while(qdiv%2==0)
	{
		qdiv=qdiv/2;
		
	}
	if(P%qdiv!=0)
		return false;
	else 
	{
		P=P/qdiv;
		Q=Q/qdiv;
	}
	return true;
}

void solve::run()
{
	int cnt=0;
	int ptemp;
	if(impos()==false)
		ans="impossible";
	else 
    {
         ptemp=P;
	     while(ptemp<Q)
	     {
		  ptemp=ptemp*2;
          cnt++;
          }
		  ostringstream convert;
		  convert << cnt;
          ans=convert.str();
    }
}

int main()
{
	solve probl;
	int k,T;
	int i,j;
	char slash;
	ifstream in;
	ofstream out;
	in.open("A1c-small-attempt0.in");
	out.open("out.out");
	in >> T;
	for(k=0;k<T;k++)
	{
		in >> probl.P;
		in >> slash;
		in >> probl.Q;
		//out << probl.Q;
		probl.run();
		out << "Case #" << k+1 << ": " << probl.ans << "\n";
	}
	in.close();
	out.close();
	return 0;
}
