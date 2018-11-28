#include<fstream>
using namespace std;
bool Check(char *xo,char t)
{
	char *txo;
	txo=new char [17];
	for(int i=1;i<=16;i++)
		if(xo[i]!='T')
			txo[i]=xo[i];
		else
			txo[i]=t;
	for(int r=1;r<=4;r++)
		if((txo[4*r-3]==t)&&(txo[4*r-2]==t)&&(txo[4*r-1]==t)&&(txo[4*r]==t))
			return true;
	for(int c=1;c<=4;c++)
		if((txo[c]==t)&&(txo[c+4]==t)&&(txo[c+8]==t)&&(txo[c+12]==t))
			return true;
	if((txo[1]==t)&&(txo[6]==t)&&(txo[11]==t)&&(txo[16]==t))
		return true;
	if((txo[4]==t)&&(txo[7]==t)&&(txo[10]==t)&&(txo[13]==t))
		return true;
	else
		return false;
}
int main()
{
	ifstream ind;
	ofstream outd;
	ind.open("A-large.in");
	outd.open("A-small-practice.out");
	int num;
	ind>>num;
	for(int y=1;y<=num;y++)
	{
		outd<<"Case #"<<y<<": ";
		char *xo;
		xo=new char [17];
		for(int i=1;i<=16;i++)
			ind>>xo[i];
		bool result=Check(xo,'X');
		if(result)
			outd<<"X won\n";
		else
		{
			result=Check(xo,'O');
			if(result)
			outd<<"O won\n";
			else
			{
				bool has=false;
				for(int i=1;i<=16;i++)
					if(xo[i]=='.')
					{
						i=17;
						has=true;
					}
				if(has)
					outd<<"Game has not completed\n";
				else
					outd<<"Draw\n";
			}
		}
	}
	return 0;
}