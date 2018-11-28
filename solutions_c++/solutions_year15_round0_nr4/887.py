#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv)
{
	ifstream inf("in.txt",ios_base::in);
	ofstream ouf("out.txt",ios_base::out);
	
	int T;
	inf>>T;
	for(int x=1;x<=T;++x)
	{
		int X,R,C;
		inf>>X>>R>>C;
		if(R<C) swap(R,C);
		
		bool y;
		if(X>=7) y=false;
		else if(X==1) y=true;
		else if(X==2) y= ((R*C)%2==0);
		else if(X==3) y= ((R*C)%3==0)&&(C>=2);
		else if(X==4) y= ((R*C)%4==0)&&(C>=3);
		else if(X==5) y= ((R*C)%5==0)&&(C>=3);
		else if(X==6) y= ((R*C)%6==0)&&(C>=4);
		
		if(y)
			ouf<<"Case #"<<x<<": GABRIEL"<<endl;
		else
			ouf<<"Case #"<<x<<": RICHARD"<<endl;
	}
	
	inf.close();
	ouf.close();
	return 0;
}