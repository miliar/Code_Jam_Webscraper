#include<fstream>

using namespace std;

int main(int argc, char *argv[])
{

 	ifstream ip;
	ip.open(argv[1]);

	ofstream op;
	op.open("D-output.txt"); 
	
	int t;
	ip>>t;

	for(int iter=1; iter<=t; iter++)
	{
		op<<"Case #"<<iter<<": ";
		
		int x,r,c;
		
		ip>>x;
		ip>>r;
		ip>>c;
		
		if(x>r && x>c)					//Single dimensional check
		{
			op<<"RICHARD"<<endl;
		}
		else if(x>=7)					//Closed loop check
		{
			op<<"RICHARD"<<endl;
		}
		else if((r*c)%x != 0)			//Spillover check
		{
			op<<"RICHARD"<<endl;
		}
		else if((r==1||c==1)&&x>=3)						//Corner checks
		{
			op<<"RICHARD"<<endl;
		}
		else if((r==2||c==2)&&x>=4)
		{
			op<<"RICHARD"<<endl;
		}
		else if((r==3||c==3)&&x>=5)
		{
			op<<"RICHARD"<<endl;
		}
		else							//Maybe gabriel can win
		{
			op<<"GABRIEL"<<endl;
		}
		
		
	}

	
	return 0;
}
